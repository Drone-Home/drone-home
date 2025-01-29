from ultralytics import YOLO

model0 = YOLO("yolov11_custom.pt")
model0.predict(source = "0", show=True, save=True, conf=0.7, line_width=2,
               save_crop = False, save_txt = False, show_labels = True, show_conf = True, classes=[0])
