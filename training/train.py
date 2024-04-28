from ultralytics import YOLO

#load model
model = YOLO('yolov8n.yaml')  # build a new model from YAML
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

#use the model
results = model.train(data="D:/Code/SeniorProj/license-plate-yolov8/training/dataset/data.yaml", epochs=5, device=0) #train