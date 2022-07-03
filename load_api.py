import requests as req
import shutil
import cv2
from object_detection import detect_objects
#response_API = req.get('https://www.askpython.com/')
# response_API.status_code

def download_image():
    # AUthorize Get Request
    headers = {
        'Accept': 'application/json',
        'Authorization': 'apikey VvTgKZbBguXDd9kjr8lrdUxeEyuz24bIO41A',
    }

    # Make Get Request
    response = req.get(
        'https://api.transport.nsw.gov.au/v1/live/cameras', headers=headers)

    # Save Response
    body = response.content
    data = response.json()

    # Get Location and Camera Links from Response
    data_list = data['features']
    cameras = {}
    for element in data_list:
        location = element['properties']['title']
        href     = element['properties']['href']
        cameras[location] = href

    # Dictionary to List
    cameras_list = [(location, href) for location, href in cameras.items()]

    # Print Locations
    counter = 1
    for this_tuple in cameras_list:
        print(str(counter)+". ", this_tuple[0])
        counter += 1

    # Get User Selected Location
    print('Enter Location Index:')
    url_index = 1
    #int(input())
    print(url_index)


    # Download Image
    img_url = cameras_list[url_index-1][1]
    this_image = req.get(img_url, stream=True)

    # Save Image Local from Location
    with open('camera_image.jpg', 'wb') as out_file:
        #shutil.copyfileobj(this_image, out_file)
        out_file.write(this_image.content)

'''
cv2.destroyAllWindows()
#img_name = "camera_image.jpg"
img_name = "test3.png"
img = cv2.imread(img_name)
cv2.imshow('Cars1', img)
r_img = detect_objects(img)

cv2.imshow('Cars2', r_img)

while 1:
    if (cv2.waitKey(0) is 'b'): break
    '''