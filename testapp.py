from projectapp import app, detectObjects, cv2, getTrafficCameraResponse
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_root():
    '''
    Unit Test for response of root "/"
    Should be fixed string
    '''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Redirt to /docs to use API"
    print("Success Test root /")


def test_read_loc():
    '''
    Unit Test for type of response of root "/getLocations"
    Should be 'list'
    '''
    response = client.get("/getLocations")
    assert response.status_code == 200
    assert type(response.json()) == type([])
    print("Success Test root /getLocations")


def test_detect_objects():
   '''
   Unit Test for type of return of detectObjects()
   Should be 'numpy array'
   '''
   img = cv2.imread('local_images/testimg1.jpg')
   r = detectObjects(img)
   assert type(r) == type(img)
   print("Success Test on file type of detect_objects()")

def test_get_locations():
    '''
    Unit Test for type of return of getTrafficCameraResponse()
    Should be 'dictionary'
    '''
    return_dictionary = getTrafficCameraResponse()
    this_dictionary = {}
    assert type(return_dictionary) == type(this_dictionary)
    print("Success Test on file type of getTrafficCameraResponse()")

def test_post_live_image():
    '''
    Unit Test for type of response of root "/detectLiveImage"
    Should be 'bytes' (which means image)
    '''
    response = client.post("/detectLiveImage", data = '5 Ways (Miranda)')
    assert response.status_code == 200
    assert type(response.content) == bytes
    print('Success Test on post of Live Image' )

def test_post_local_image():
    '''
    Unit Test for type of response of root "/detectLocalImage"
    Should be 'bytes' (which means image)
    '''
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
