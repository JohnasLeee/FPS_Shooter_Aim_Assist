import torch
from ultralytics import YOLO

# Check if GPU is available
if torch.cuda.is_available():
    print("GPU is available")
else:
    print("GPU is not available")

# Load the model.
model = YOLO('yolov8n.pt') # pretrained model that i download

# Training.
if __name__ == '__main__':
    results = model.train(
       data='data\custom_data.yaml', # .yaml file 
       imgsz=640,
       epochs=100, # epoch number 
       batch=8, 
       name='data\custom_data.yaml',
       plots=True,
       )

