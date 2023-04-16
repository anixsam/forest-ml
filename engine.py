import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True) 

def get_animal():
    img = 'image.jpg'
    # Inference
    results = model(img)
    # number_of_objects = len(results.xyxy[0])
    name_of_object_detected = results.pandas().xyxy[0]['name']
    # print(name_of_object_detected)
    # Results, change the flowing to: results.show()
    # results.show()
    count = 0
    animals = ""
    for i in name_of_object_detected:
        if i in ['elephant', 'zebra', 'giraffe', 'bear', 'cow' , 'cat']:
            count += 1
            animals = i;
    return { "animal" : animals , "count" : count }
