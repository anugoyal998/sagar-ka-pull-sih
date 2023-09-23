from PIL import Image
from super_gradients.training import models
from super_gradients.common.object_names import Models
import torchvision.transforms as transforms
import torch
import cv2
from super_gradients.training.models.detection_models.yolo_base import YoloXPostPredictionCallback

preprocess = transforms.Compose([
    transforms.Resize([640, 640]),
    transforms.PILToTensor()
])

model = models.get(Models.YOLOX_L, pretrained_weights="coco")
model = model.to("cuda" if torch.cuda.is_available() else "cpu")

# model_predictions = model.predict("/content/drive/MyDrive/sih/Crowd localization and counting.mp4")

# model_predictions.save("/content/drive/MyDrive/sih/Crowd-output-yolo_nas_l.mp4")

def draw_bbox(predictions,img):
  for prediction in predictions:
    class_names = prediction.class_names
    labels = prediction.prediction.labels
    confidence = prediction.prediction.confidence
    bboxes = prediction.prediction.bboxes_xyxy

    print(len(bboxes))

    for i, (label, conf, bbox) in enumerate(zip(labels, confidence, bboxes)):
      if class_names[int(label)] == 'person':
        cv2.rectangle(img,(int(bbox[0]),int(bbox[1])),(int(bbox[2]),int(bbox[3])),(0,255,0),2)


video = cv2.VideoCapture("Rush hour at train station in India.mp4")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)
# result = cv2.VideoWriter('output-yolo-nas.avi',
#                          cv2.VideoWriter_fourcc(*'MJPG'),
#                          10, size)

while video.isOpened():
  success, img = video.read()
  if success:
    predictions = model.predict(img)
    draw_bbox(predictions,img)
    # result.write(img)
    cv2.imshow("Frame",img)

  if cv2.waitKey(1) & 0xFF == ord('s'):
    break

video.release()
# result.release()
cv2.destroyAllWindows()