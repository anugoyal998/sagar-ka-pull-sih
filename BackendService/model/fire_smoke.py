import cv2

classes = ["default","fire","background","smoke"]

def draw_bbox_fire_smoke(results,img):
    fire = False
    for r in results:
        # print(r.boxes)
        data = r.boxes
        labels = data.cls.numpy()
        confidence = data.conf.numpy()
        bboxes = data.xyxy.numpy()
        print(labels, confidence, bboxes)
        for i, (label, conf, bbox) in enumerate(zip(labels,confidence,bboxes)):
            if int(label) == 1 or int(label) == 3:
                fire = True
                cv2.rectangle(img,(int(bbox[0]),int(bbox[1])),(int(bbox[2]),int(bbox[3])),(0,255,0),2)
                cv2.putText(img,str(classes[int(label)]),(int(bbox[2]),int(bbox[1]) + 50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
                
    return fire, img
        # data = r.data
        # bboxes = data.boxes
        # labels = data.cls
        # conf = data.conf
        
        # for i, (label, conf, bbox) in enumerate(zip(labels,conf,bboxes)):
        #     if int(label) == 1 or int(label) == 3:
        #         pass
    