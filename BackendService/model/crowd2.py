import random

import cv2
import numpy as np
from ultralytics import YOLO


# Vals to resize video frames | small frame optimise the run
frame_wid = 640
frame_hyt = 480


def draw_bbox_crowd2(model,frame):
    #  resize the frame | small frame optimise the run
    # frame = cv2.resize(frame, (frame_wid, frame_hyt))

    # Predict on image
    detect_params = model.predict(source=[frame], conf=0.45, save=False)

    # Convert tensor array to numpy
    DP = detect_params[0].numpy()
    

    if len(DP) != 0:
        count = 0
        for i in range(len(detect_params[0])):
            count = count + 1

            boxes = detect_params[0].boxes
            box = boxes[i]  # returns one box
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bbox = box.xyxy.numpy()[0]

            cv2.rectangle(
                frame,
                (int(bbox[0]), int(bbox[1])),
                (int(bbox[2]), int(bbox[3])),
                (0,0,225),
                3,
            )
            top_left = (int(bbox[0]), int(bbox[1]))
            bottom_right = (int(bbox[2]), int(bbox[3]))
            x, y = top_left[0], top_left[1]
            w, h = bottom_right[0] - \
            top_left[0], bottom_right[1] - top_left[1]
            ROI = frame[y:y+h, x:x+w]
            # print(ROI.any())
            if (ROI.any()):
                blur = cv2.GaussianBlur(ROI, (51, 51), 0)
                frame[y:y+h, x:x+w] = blur
            # Display class name and confidence
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(
                frame,
                "Person" + " " + str(round(conf, 3)) + "%",
                (int(bbox[0]), int(bbox[1]) - 10),
                font,
                1,
                (255, 255, 255),
                2,
            )
    return frame,count