# 🔍 YOLO Image Search Engine  
*A Computer Vision powered visual search application using YOLOv11 + Streamlit*

---

## 🚀 Overview

This project allows users to **search images based on objects detected using YOLOv11**.

Instead of detecting objects every time, the application:

1. Runs inference once over a folder of images
2. Saves the structured metadata (class → count → confidence → bounding boxes)
3. Allows fast search and filtering based on:
   - Object classes (Person, Apple, Car, …)
   - Object count thresholds
   - Logical search mode (OR / AND)

> Example: **Find images that have (person AND bicycle)**  
> Example: **Show images that contain (apple OR banana), with ≤ 3 apples**

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🔎 Search Engine | Query images based on object detections |
| 🧠 Metadata Indexing | Stores detections as JSON → fast searching |
| ⚙️ YOLOv11 Powered | Supports any YOLO model (custom weights included) |
| 🖼️ Grid Display | Dynamically displays matching images |
| ✅ Bounding Boxes Toggle | Annotated vs. original images view |
| 📦 Export | Download search results as JSON |
| 💡 Streamlit UI | Simple and interactive front-end |

---

## 🧠 How It Works (Architecture)

User Input → Run YOLO Inference → Generate Metadata → Search & Filter → Display Results


Metadata stored per image:

```json
{
  "image_path": "...",
  "detections": [
    {"class": "person", "confidence": 0.91, "bbox": [x1, y1, x2, y2], "count": 3}
  ],
  "class_counts": {"person": 3, "car": 1}
}

🗂️ Project Structure
yolo_image_search/
│── app.py                # Streamlit UI
│── requirements.txt      # Python dependencies
│── instruction.txt       # (optional) setup notes
│
├── src/
│   ├── inference.py      # YOLO model inference
│   ├── utils.py          # Metadata save/load helpers
│   └── config.py         # Load YAML config
│
├── configs/
│   └── default.yaml      # Configurations (extensions, confidence threshold)
│
└── ui-flow-*.png         # UI flow diagrams

🔧 Installation & Setup
✅ 1. Clone the repository
git clone https://github.com/Sawarnshivam/yolo_image_search.git
cd yolo_image_search

✅ 2. Create virtual environment (optional, recommended)
python -m venv venv
.\venv\Scripts\activate

✅ 3. Install dependencies
pip install -r requirements.txt

✅ 4. Run the application
streamlit run app.py

📌 Usage Guide
Option 1 — Process new images

Specify image directory path

Specify YOLO weight file (e.g., yolo11m.pt)

App detects objects & saves metadata automatically

Option 2 — Load existing metadata

Load .json metadata file generated earlier

Fast search without detection overhead

Search Controls

Select classes to search

Choose search mode:
✅ OR mode → match ANY class
✅ AND mode → match ALL selected classes

Filter using count thresholds (≤ X objects)

⚠️ File Size Notice

Large assets are NOT included in the repository:

yolo11m.pt (YOLO model weights)

/data/ folder (raw images, processed metadata)

Add your model weights manually to project root.

🛠️ Tech Stack
Component	Technology
Model	Ultralytics YOLOv11
UI	Streamlit
Language	Python
Visualization	PIL / ImageDraw
Metadata format	JSON
🔥 UI Flow (screenshots)
UI Flow Diagrams
<img width="3840" height="2160" alt="ui-flow-1" src="https://github.com/user-attachments/assets/2dc95442-3131-4585-b9ec-edd6064669c8" />
<img width="3840" height="2160" alt="ui-flow-2" src="https://github.com/user-attachments/assets/fb749fb7-239d-4184-88e1-97bf8b7512cc" />
<img width="3840" height="2160" alt="ui-flow-3" src="https://github.com/user-attachments/assets/fb1241de-407d-4227-aa43-6e9f41674cce" />





⭐ Future Enhancements (idea list)

ZIP export of annotated results

Search by text prompt (Multimodal RAG Extension)

Add vector DB (FAISS) for similarity search

If this project helped you, consider giving it a ⭐ on GitHub 🙌
