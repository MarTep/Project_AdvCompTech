import cv2
import numpy as np


def detect_objects(img):
    # Load Network
    net = cv2.dnn.readNet("dnn_model/yolov4.weights", "dnn_model/yolov4.cfg")
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(832, 832), scale=1 / 255)


    # Detect selected classes
    classes_allowed = [0, 1, 2, 3, 5, 6, 7]


    # Detect Objects
    object_boxes = []
    object_names = []
    classes_dict = {
        "0": "person",
        "1": "bicycle",
        "2": "car",
        "3": "motorbike",
        "5": "bus",
        "6": "train",
        "7": "truck",
    }
    class_ids, scores, boxes = model.detect(img, nmsThreshold=0.4)

    for class_id, score, box in zip(class_ids, scores, boxes):
        if score < 0.5:
            # Skip detection with low confidence
            continue

        if class_id in classes_allowed:
            object_boxes.append(box)
            object_names.append(class_id)

    vehicle_count = len(object_boxes)

    temp_counter = 0
    for box in object_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        id_index = str(object_names[temp_counter])
        cv2.putText(img, classes_dict.get(id_index),
                    (x, y-5), 0, 1, (100, 200, 0), 1)

        temp_counter += 1

    cv2.putText(img, "Vehicles: " + str(vehicle_count),
                (20, 50), 0, 2, (100, 200, 0), 3)
    return img

    
