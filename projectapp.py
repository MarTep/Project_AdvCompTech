from cv2 import Mat
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
import cv2
import requests as req


class Error(BaseModel):
    code: int
    reason: str


# Setup API Framework
app = FastAPI()


# Get Request root
@app.get("/")
async def root():
    return "Redirt to /docs to use API"


# Get Request to get Live Traffic Camera Locations
@app.get("/getLocations",
         tags=["Get Live Traffic Cameras Locations"],
         summary="List of Live Traffic Cameras Locations",

         )
async def getLocations():
    '''
    Returns a List of all Traffic Cameras Locations
    '''
    # Get
    cameras = getTrafficCameraResponse()

    # Keep only the Location String
    cameras_list = list(cameras.keys())

    # Sort for Display
    cameras_list.sort()

    return cameras_list


# Post Request with Local Image to Detect Objects
@app.post("/detectLocalImage",
          tags=["Detect Vehicles"],
          summary="Detect Vehicles from Local Image (Image must be in folder local_images)",
          description="Example: testim1.jpg"
          )
async def localImage(img_name='testimg1.jpg'):
    '''
    Input: Full Name of image under 'local_images/'
    Example: testim1.jpg

    Return an image with detected objects as response
    and saves it to server
    '''

    # Load Image from Folder 'local_images/'
    img = cv2.imread('local_images/'+img_name)

    # Detect Objects
    detected_img = detectObjects(img)

    # Save to Server the Detected Image
    cv2.imwrite("detected_img.jpg", detected_img)

    return FileResponse("detected_img.jpg")


# Post Request with Live Image to Detect Objects
@app.post("/detectLiveImage",
          tags=["Detect Vehicles"],
          summary="Detect Vehicles from Live Image",
          description="Get the Locations First and the choose. Example: 5 Ways (Miranda)"
          )
async def liveImage(img_name='5 Ways (Miranda)'):
    '''
    Input: Full Name of Location
    Example: 5 Ways (Miranda)

    Return an image with detected objects as response
    and saves it to server
    '''

    # Get Live
    cameras = getTrafficCameraResponse()
    img_url = cameras[img_name]

    # Download Image
    this_image = req.get(img_url, stream=True)

    # Save to Server Original Image
    with open('camera_image.jpg', 'wb') as out_file:
        out_file.write(this_image.content)

    # Load Image
    img = cv2.imread('camera_image.jpg')

    # Detect Objects
    detected_img = detectObjects(img)

    # Save to Server Detected Image
    cv2.imwrite("detected_img.jpg", detected_img)

    return FileResponse("detected_img.jpg")


# ---------
# Functions
# ---------

def detectObjects(img):
    '''
    Return an image with boxes on detected objects.
    '''
    # Load Network
    net = cv2.dnn.readNet("dnn_model/yolov4.weights", "dnn_model/yolov4.cfg")
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(832, 832), scale=1 / 255)

    # Detect selected classes
    # Available objects for detection
    classes_dict = {
        "0": "person",
        "1": "bicycle",
        "2": "car",
        "3": "motorbike",
        "5": "bus",
        "6": "train",
        "7": "truck",
    }
    classes_allowed = [0, 1, 2, 3, 5, 6, 7]

    # Detect Objects
    object_boxes = []
    object_names = []
    class_ids, scores, boxes = model.detect(img, nmsThreshold=0.4)

    for class_id, score, box in zip(class_ids, scores, boxes):

        if score < 0.5:
            # Skip detection with low confidence
            continue

        if class_id in classes_allowed:
            object_boxes.append(box)
            object_names.append(class_id)

    object_count = len(object_boxes)

    temp_counter = 0

    for box in object_boxes:

        # Get Box Coordinates
        x, y, w, h = box

        # Draw Box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 1)

        # Get Object Name
        id_index = str(object_names[temp_counter])

        # Draw Name
        cv2.putText(img, classes_dict.get(id_index),
                    (x, y-5), 0, 1, (25, 0, 180), 2)

        temp_counter += 1

    # Draw Sum of Objects
    cv2.putText(img, "Objects: " + str(object_count),
                (15, 30), 0, 1, (100, 200, 0), 3)

    return img

# ------
# ------
# ------


def getTrafficCameraResponse():
    '''
    Connects to Live Traffic Cameras API and
    returns a dictionary with location and url of Live Image
    '''

    # Authorize Get Request
    headers = {
        'Accept': 'application/json',
        'Authorization': 'apikey VvTgKZbBguXDd9kjr8lrdUxeEyuz24bIO41A',
    }

    # Make Get Request
    response = req.get(
        'https://api.transport.nsw.gov.au/v1/live/cameras', headers=headers)

    # Save Response
    data = response.json()

    # Get Location and Camera Links from Response
    data_list = data['features']
    cameras = {}
    for element in data_list:

        location = element['properties']['title']
        href = element['properties']['href']

        # Add to dicitonary
        cameras[location] = href

    return cameras
