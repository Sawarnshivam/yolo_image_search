# YOLOv11 Search Application 🔍

> A Computer Vision powered image search system built using **YOLOv11** for object detection and **Streamlit** for the web user interface.

This application allows users to process large collections of images, extract object metadata automatically, and perform advanced searches based on object classes and specific count thresholds.

---

## 🔥 Key Features

* **Automated Inference:** Run object detection using YOLOv11 on entire folders of images.
* **Structured Metadata:** Automatically saves detection results (classes, bounding boxes, confidence scores) as JSON.
* **Efficient Loading:** Load previously processed metadata instantly without re-running computationally expensive inference.
* **Advanced Search Capabilities:**
    * Filter by specific **classes** (objects).
    * Set **object count thresholds** (e.g., "exactly 1 banana", "less than 3 spoons").
    * Toggle match modes: **ANY** (OR) vs **ALL** (AND).
* **Visual Results:** Responsive image grid display with bounding boxes.
    * *Matching objects* highlighted in green.
    * *Non-matching objects* shown faded (optional).
* **Data Export:** Export filtered search results as `search_results.json` for further analysis.

---

## 🌍 Real-World Use Cases

This system is highly useful wherever image datasets are large and manual searching is time-consuming or impossible.

| Domain | Application |
| :--- | :--- |
| **Surveillance / Security** | Search CCTV footage for specific persons, vehicles, or suspicious items during investigations. |
| **Retail Analytics** | Analyze product shelf states or crowd presence using store camera data. |
| **Traffic Monitoring** | Detect and count cars, bikes, and pedestrians for smart city analysis. |
| **Wildlife Monitoring** | Identify and track specific animal species from forest camera trap images. |
| **Medical Imaging** | Organize and filter medical scans based on detected features (cells, abnormalities). |
| **Digital Asset Management** | Quickly find personal or event photos containing specific people, pets, or objects. |
| **Forensics** | Filter crime scene image collections for specific objects (e.g., weapons, evidence type). |

---

## 📦 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Object Detection** | [YOLOv11](https://docs.ultralytics.com/) (PyTorch) |
| **Frontend UI** | [Streamlit](https://streamlit.io/) |
| **Image Processing** | Pillow (PIL) |
| **Data Storage** | JSON (Structured Metadata) |

---

## 🚀 Installation & Running

### Prerequisites
Ensure you have Python 3.8+ installed.

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```
### 2. Launch the Application
```bash

streamlit run app.py
```
### 3. Initial Setup
Once the web interface loads:

Upload or specify the path to your image folder.

Select your desired YOLOv11 model weights (e.g., yolo11n.pt, yolo11x.pt).

📖 Usage Workflow
### 1. Processing Images
- Choose your dataset folder and run YOLO inference.

- The app will generate and save metadata in processed/<dataset>/metadata.json.

- Note: On subsequent visits, you can just load this metadata directly without waiting for inference.

### 2. Searching
Use the sidebar to configure your search filters:

- Select Classes: Choose which objects to look for (e.g., 'person', 'car').

- Set Count Filters: Define rules like "Person count ≥ 1" AND "Car count = 0".

- Choose Search Mode:
  --
| Mode | Meaning |
| :--- | :--- |
| ANY (OR) | Image is shown if it contains at least one of the selected classes. |
| ALL (AND) | Image is shown only if it contains all selected classes simultaneously. |


### 3. Viewing & Exporting
- Browse the responsive grid of matching images.

- View precise bounding boxes on detected objects.

- Click the Export button to download your current filtered view as a JSON file.

## 📂 Metadata Structure
The application saves detection data in a structured JSON format for quick retrieval:
```json

{
  "image_path": "images/vacation/img_001.jpg",
  "detections": [
    {
      "class": "banana",
      "confidence": 0.85,
      "bbox": [100, 150, 200, 300],
      "count": 1
    },
    {
      "class": "bowl",
      "confidence": 0.92,
      "bbox": [50, 200, 350, 400],
      "count": 1
    }
  ],
  "class_counts": {
      "banana": 1,
      "bowl": 1
  }
}
