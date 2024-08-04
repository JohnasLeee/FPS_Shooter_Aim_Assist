from ultralytics import YOLO

# Load the trained model weights
model = YOLO(r'runs/detect/data/custom_data.yaml/weights/best.pt')  # Adjust the path to your trained model weights

# Evaluate the model on a validation dataset
if __name__ == '__main__':
    results = model.val(data='data/custom_data.yaml', imgsz=640)
    print(results)