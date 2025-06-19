export PYTHONPATH=/home/new_drive_2/YOLO-Mamba/:$PYTHONPATH

yolo obb_pose mode=train model=/home/new_drive_2/YOLO-Mamba/ultralytics/cfg/models/12/yolo12s-obb-pose.yaml data=/home/new_drive_2/YOLO-Mamba/ultralytics/cfg/datasets/obb_pose.yaml batch=16 epochs=500 imgsz=1150 workers=0 device=0 conf=0.4 iou=0.5 lr0=0.0001 patience=150