

from ultralytics import YOLO


# model = YOLO("/home/music/runs/obb_pose/train22/weights/best.pt")
model = YOLO("/home/new_drive_2/YOLO-Mamba/runs/obb_pose/train3/weights/best.pt")
metrics = model.val(batch=16, imgsz=1150, workers=0, device=0, conf=0.4, iou=0.5, nms=True, agnostic_nms=True, data="/home/new_drive_2/ultralytics-main/ultralytics/cfg/datasets/obb_pose.yaml")

print(f"metrics.box.map: {metrics.box.map:.3f}")
print(f"metrics.box.map50: {metrics.box.map50:.3f}")
print(f"metrics.box.map75: {metrics.box.map75:.3f}")
print(f"metrics.box.map90: {metrics.box.map75:.3f}")
print(f"metrics.box.maps: {metrics.box.maps}")

print(f"metrics.pose.map: {metrics.pose.map:.3f}")
print(f"metrics.pose.map50: {metrics.pose.map50:.3f}")
print(f"metrics.pose.map75: {metrics.pose.map75:.3f}")
print(f"metrics.pose.map90: {metrics.pose.map75:.3f}")
print(f"metrics.pose.maps: {metrics.pose.maps}")
