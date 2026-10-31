YOLO Object Detection App
A Streamlit-based object detection application that uses the YOLOv8n
model from Ultralytics and OpenCV to detect a user-selected object in a
webcam feed or an uploaded video.
Features
- Choose between Webcam and Upload Video as the input source.
- Upload video files in .mp4, .avi, or .mov format.
- Select one object class from the COCO dataset (for example, person,
  car, bicycle, or dog).
- Adjust the confidence threshold using a slider.
- Display the processed video frames in the Streamlit interface.
- Draw bounding boxes and confidence labels around detections that
  match the selected class and threshold.
Technologies Used
- Python --- application programming language
- Streamlit --- web interface
- Ultralytics YOLOv8 --- object detection model
- OpenCV --- video capture and frame processing
Project File
YOLO-Object-Detection/
├── Yolo_project.py
└── README.md
The application loads yolov8n.pt when it starts. If the model weights
are not available locally, Ultralytics may download them automatically.
Requirements
- Python 3.8 or later (use a Python version supported by your
  installed Ultralytics release)
- A working webcam if you choose the webcam input
- Internet access on the first run if the YOLOv8n weights need to be
  downloaded
Installation
1. Clone or download this project.
2. Open a terminal in the project directory.
3. (Recommended) Create and activate a virtual environment:
   python -m venv venv
   Windows:
   venv\Scripts\activate
   macOS/Linux:
   source venv/bin/activate
4. Install the required packages:
   pip install streamlit opencv-python ultralytics
Run the Application
Run the following command from the project directory:
streamlit run Yolo_project.py
Streamlit will display a local URL in the terminal (usually
http://localhost:8501). Open that URL in your browser.
How to Use
1. Start the application.
2. Select Webcam or Upload Video.
3. If you select Upload Video, choose an .mp4, .avi, or .mov
   file.
4. Choose the object class you want the model to detect.
5. Set the confidence threshold. A higher value makes the detection
   filter stricter.
6. Select Start Detection.
7. View the video frames with bounding boxes and confidence labels for
   matching detections.
Detection Details
The app uses the COCO class list and the corresponding class index to
filter YOLO detections. A detection is drawn only when:
- Its predicted class matches the selected object class.
- Its confidence score is greater than the selected confidence
  threshold.
The displayed confidence score is formatted to two decimal places.
Notes and Limitations
- The webcam is opened with OpenCV using camera index 0; this refers
  to the default camera available to the machine running the Streamlit
  app.
- Webcam capture occurs on the machine running the Python application,
  not necessarily on the browser user's device when the app is hosted
  remotely.
- Processing speed depends on the computer, video resolution, and
  available hardware.
- The current interface processes frames until the video ends or the
  webcam capture stops. It does not currently provide a pause or
  stop-detection control.
- The code is configured to detect one selected COCO class at a time.
- This README describes the functionality present in the supplied
  script; it does not imply that additional features such as detection
  history, video export, or multi-class selection are implemented.
Troubleshooting
The video does not open - Check that the uploaded file is in a
supported format. - Try another video file. - For webcam input, check
that a camera is connected and available.

The YOLO model cannot load - Check your internet connection if the
model weights have not yet been downloaded. - Confirm that the installed
ultralytics package is working and that yolov8n.pt is accessible.

A selected object is not detected - Try lowering the confidence
threshold. - Check that the object is visible in the frame. Detection
results depend on image quality, lighting, object size, and the model's
capabilities.
License
No license is specified in the supplied project script. Add a license
file if you intend to distribute the project and want to define reuse
permissions.
