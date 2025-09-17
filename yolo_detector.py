from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Dictionary to store the track history
track_history = {}

def draw_boxes_and_line(frame, boxes, object_id):
    """Draw detected bounding boxes and tracking line on the image frame"""
    # Create annotator object
    annotator = Annotator(frame)
    
    # Initialize the list of positions if not already done
    if object_id not in track_history:
        track_history[object_id] = []

    for box in boxes:
        class_id = box.cls
        class_name = model.names[int(class_id)]
        coordinator = box.xyxy[0]
        confidence = box.conf
        
        # Track the center of the bounding box
        center_x = int((coordinator[0] + coordinator[2]) / 2)
        center_y = int((coordinator[1] + coordinator[3]) / 2)
        
        # Add center coordinates to track history
        track_history[object_id].append((center_x, center_y))
        
        # Draw bounding box
        annotator.box_label(
            box=coordinator, label=class_name, color=((255, 0, 0))
        )
        
        # Draw tracking line if there are at least 2 points
        if len(track_history[object_id]) > 1:
            for i in range(1, len(track_history[object_id])):
                pt1 = track_history[object_id][i - 1]
                pt2 = track_history[object_id][i]
                cv2.line(frame, pt1, pt2, (0, 255, 0), 2)  # Draw line between previous and current positions

    return annotator.result()

def detect_object(frame):
    """Detect object from image frame"""
    results = model.track(frame)

    # Filter for 'cat' class
    cats = [box for result in results for box in result.boxes if result.names[int(box.cls)] == 'cat']

    for result in results:
        frame = draw_boxes_and_line(frame, cats, object_id="cat")

    return frame

if __name__ == "__main__":
    video_path = "CatZoomies.mp4"
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        # Read image frame
        ret, frame = cap.read()

        if ret:
            # Detect and track the cat
            frame_result = detect_object(frame)

            name_text = "Nattajak-Clicknext-Internship-2024"
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.7
            font_thickness = 2
            
            # Get text size
            (text_width, text_height), baseline = cv2.getTextSize(name_text, font, font_scale, font_thickness)
            
            # Set text position to the top-right corner
            text_x = frame_result.shape[1] - text_width - 10
            text_y = text_height + 10
            
            # Add text to the frame
            cv2.putText(frame_result, name_text, (text_x, text_y), font, font_scale, (0, 0, 255), font_thickness, cv2.LINE_AA)

            # Show result
            cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
            cv2.imshow("Video", frame_result)
            cv2.waitKey(30)

        else:
            break

    cap.release()
    cv2.destroyAllWindows()
