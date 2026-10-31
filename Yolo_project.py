import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# COCO Classes
COCO_CLASSES = [
    "person","bicycle","car","motorcycle","airplane","bus","train","truck","boat",
    "traffic light","fire hydrant","stop sign","parking meter","bench","bird","cat",
    "dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack","umbrella",
    "handbag","tie","suitcase","frisbee","skis","snowboard","sports ball","kite","baseball bat",
    "baseball glove","skateboard","surfboard","tennis racket","bottle","wine glass","cup",
    "fork","knife","spoon","bowl","banana","apple","sandwich","orange","broccoli","carrot",
    "hot dog","pizza","donut","cake","chair","couch","potted plant","bed","dining table",
    "toilet","tv","laptop","mouse","remote","keyboard","cell phone","microwave","oven",
    "toaster","sink","refrigerator","book","clock","vase","scissors","teddy bear","hair drier","toothbrush"
]

# UI
st.title("YOLO")

# Input source
source = st.radio("Select Input Source", ["Webcam", "Upload Video"])

uploaded_file=None
if source =="Upload Video":
    uploaded_file=st.file_uploader("Upload Video",type=["mp4","avi","mov"])

# Class selection
selected_class = st.selectbox("Select Object to Detect", COCO_CLASSES)
selected_class_index = COCO_CLASSES.index(selected_class)

# Confidence
confidence_threshold = st.slider("Confidence Threshold", 0.1, 1.0, 0.65)

# Display window
frame_window = st.image([])

# Start button
start = st.button("Start Detection")

if start:

    cap = None

    # Webcam
    if source == "Webcam":
        cap = cv2.VideoCapture(0)

    # Video Upload
    elif uploaded_file is not None:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            video_path=tfile.name
            
            cap = cv2.VideoCapture(video_path)


    else:
        st.warning("please provide video")
        st.stop()

    if not cap.isOpened():
        st.error("Error opening video")
        st.stop()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for result in results:
            for box in result.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])

                if cls == selected_class_index and conf > confidence_threshold:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                        # Draw bounding box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

                        # Label
                    cv2.putText(frame, f"{selected_class} {conf:.2f}",
                                (x1, y1 - 10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255, 0, 0),2)

            # Convert to RGB for Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame)

    cap.release()
