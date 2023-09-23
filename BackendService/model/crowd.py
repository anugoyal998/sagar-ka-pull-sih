import torchvision.transforms as transforms
from super_gradients.training import models
from super_gradients.common.object_names import Models
import torch
import cv2

preprocess = transforms.Compose([
    transforms.Resize([640, 640]),
    transforms.PILToTensor()
])

crowd_model = models.get(Models.YOLOX_L, pretrained_weights="coco")
crowd_model = crowd_model.to("cuda" if torch.cuda.is_available() else "cpu")


def draw_bbox_crowd(predictions, img):
    for prediction in predictions:
        class_names = prediction.class_names
        labels = prediction.prediction.labels
        confidence = prediction.prediction.confidence
        bboxes = prediction.prediction.bboxes_xyxy
        count = 0
        print(len(bboxes))
        for i, (label, conf, bbox) in enumerate(zip(labels, confidence, bboxes)):
            if class_names[int(label)] == 'person':
                count = count+1
                # crop_obj = img[int(bbox[0]):int(bbox[1])+int(bbox[0]),int(bbox[2]):int(bbox[3])+int(bbox[2])]

                # blur_img = cv2.blur(img,roi)
                # img[int(bbox[0]):int(bbox[0])+int(bbox[1]),int(bbox[2]):int(bbox[3]):int(bbox[3])+int(bbox[4])] = blur_img
                cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(
                    bbox[2]), int(bbox[3])), (0, 255, 0), 2)

                top_left = (int(bbox[0]), int(bbox[1]))
                bottom_right = (int(bbox[2]), int(bbox[3]))
                x, y = top_left[0], top_left[1]
                w, h = bottom_right[0] - \
                    top_left[0], bottom_right[1] - top_left[1]
                ROI = img[y:y+h, x:x+w]
                print(ROI.any())
                if (ROI.any()):
                    blur = cv2.GaussianBlur(ROI, (51, 51), 0)
                    img[y:y+h, x:x+w] = blur
                # print(bbox[0])
                # print(bbox[1])
                # print(bbox[2])
                # print(bbox[3])
    return count
