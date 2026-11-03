"""Run once: converts yolov8n.pt to ONNX and places it where the website loads it.
    pip install ultralytics onnx
    python export_model.py
"""
import shutil
from pathlib import Path
from ultralytics import YOLO

path = YOLO("yolov8n.pt").export(format="onnx", imgsz=640, opset=12)
Path("models").mkdir(exist_ok=True)
shutil.copy(path, "models/yolov8n.onnx")
print("Done: models/yolov8n.onnx")
