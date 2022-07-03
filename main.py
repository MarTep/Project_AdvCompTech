import cv2
from object_detection import detect_objects
from load_api import download_image

def show_images(img_name):
    #img_name = "test3.png"
    img = cv2.imread(img_name)
    cv2.imshow('Cars Original', img)

    r_img = detect_objects(img)
    cv2.imshow('Cars Detected', r_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    #while True:
        #if (cv2.waitKey(0) is 'b'):
            #break

while True:

    #img_name = "camera_image.jpg"

    # Load Image
    # Ask User Input Method
    print("Load Image Local or Live (from traffic cameras)")
    method = input()
    #cv2.destroyAllWindows()
    if method == 'Local':
        img_name = input()
        show_images(img_name)
    elif method == 'Live':
        download_image()
        show_images(img_name)
        img_name = 'camera_image.jpg'
    else:
        print('Wrong Input')



