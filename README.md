# YOLO Object Finder (web version)

A static website version of the Streamlit app. YOLOv8n runs in the browser with
ONNX Runtime Web, so the webcam works for every visitor once deployed on HTTPS.

## 1. Create the model file (once)
```
pip install ultralytics onnx
python export_model.py
```
This creates `models/yolov8n.onnx` (about 12 MB).

## 2. Test locally
```
python -m http.server 8000
```
Open http://localhost:8000

## 3. Deploy (pick one)
- **Vercel / Netlify:** import the folder or its GitHub repo. No build command, publish the root folder.
- **GitHub Pages:** push the folder (including `models/yolov8n.onnx`) to a repo, then Settings > Pages > deploy from the main branch.

Webcam access needs HTTPS (all three hosts provide it) or localhost.
