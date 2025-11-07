from ultralytics import YOLO
from pathlib import Path
import torch
from .config import load_config

class YOLOv11Inference:
    def __init__(self, model_name, device=None):
        # auto-select; default to CPU when CUDA isn't available
        if device is None:
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.device = device

        self.model = YOLO(model_name)
        if self.device != 'cpu':          # <-- guard to avoid CUDA on CPU-only builds
            self.model.to(self.device)

        config = load_config()
        self.conf_threshold = config["model"]["conf_threshold"]
        self.extensions = config["data"]["image_extension"]

    def process_image(self, image_path):
        results = self.model.predict(
            source=image_path,
            conf=self.conf_threshold,
            device=self.device  # 'cpu' if no CUDA
        )

        # process results
        detection = []
        class_counts = {}

        for result in results:
            for box in result.boxes:
                cls = result.names[int(box.cls)]
                conf = float(box.conf)
                bbox = box.xyxy[0].tolist()

                detection.append({
                    'class' : cls,
                    'confidence' : conf,
                    'bbox' : bbox,
                    'count' : 1
                })

                class_counts[cls] = class_counts.get(cls, 0) + 1

        for det in detection:
            det['count'] = class_counts[det['class']]

        return {
            'image_path' : str(image_path),
            'detections' : detection,
            'total_objects' : len(detection),
            'unique_class' : list(class_counts.keys()), # [0, 1, 2]
            'class_counts' : class_counts # {0 : 3, 1 : 10, 2, : 1}
        }


    def process_directory(self, directory):
        metadata = []

        patterns = [f"*{ext}" for ext in self.extensions]

        image_paths = []
        for pattern in patterns:
            image_paths.extend(Path(directory).glob(pattern))

        for img_path in image_paths:
            try:
                metadata.append(self.process_image(img_path))
            except Exception as e:
                print(f"Error processing {img_path}: {str(e)}")
                continue
        # print(metadata)
        return metadata
