from projectapp import app, detectObjects, cv2, getTrafficCameraResponse
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Redirt to /docs to use API"
    print("Success Test root /")

def test_read_loc():
    response = client.get("/getLocations")
    assert response.status_code == 200
    assert type(response.json()) == type([])
    print("Success Test root /getLocations")

def test_detect_objects():
   img = cv2.imread('local_images/testimg1.jpg')
   r = detectObjects(img)
   assert type(r) == type(img)
   print("Success Test on file type of detect_objects()")

def test_get_locations():
    return_dictionary = getTrafficCameraResponse()
    this_dictionary = {}
    assert type(return_dictionary) == type(this_dictionary)
    print("Success Test on file type of getTrafficCameraResponse()")

def test_post_live_image():
    response = client.post("/detectLiveImage", data = '5 Ways (Miranda)')
    assert response.status_code == 200
    assert type(response.content) == bytes
    print('Success Test on post of Live Image' )

def test_post_local_image():
    response = client.post("/detectLocalImage", data = 'testim1.jpg')
    assert response.status_code == 200
    assert type(response.content) == bytes
    print('Success Test on post of Local Image' )

# Test Gets
test_get_root()
test_read_loc()

# Test Posts
test_post_live_image()
test_post_local_image()

# Test functions
test_detect_objects()
test_get_locations()
