from ultralytics import YOLO
import cv2

class VehicleDetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)
        self.vehicle_classes = [2, 3, 5, 7]  
        # car=2, motorcycle=3, bus=5, truck=7

    def detect(self, frame):
        results = self.model(frame)[0]
        vehicles = []

        for box in results.boxes:
            cls = int(box.cls[0])
            if cls in self.vehicle_classes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                vehicles.append((x1, y1, x2, y2))

        return vehicles