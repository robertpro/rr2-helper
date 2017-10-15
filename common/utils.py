import os
from com.dtmilano.android.viewclient import ViewClient
import autopy

THIS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = THIS_DIR + "/images/"


def take_device_screenshot(image="screen", serialno=None):
    if not image.endswith(".png"):
        image += ".png"
    device, serialno = ViewClient.connectToDeviceOrExit(verbose=False, serialno=serialno)
    device.takeSnapshot().save(IMAGES_DIR + image, 'PNG')


def find_image_in_another_image(image, in_this_image):
    if not image.endswith(".png"):
        image += ".png"
    if not in_this_image.endswith(".png"):
        in_this_image += ".png"

    _image = autopy.bitmap.Bitmap.open(IMAGES_DIR + image)
    _in_this_image = autopy.bitmap.Bitmap.open(IMAGES_DIR + in_this_image)

    return _in_this_image.find_bitmap(_image)


def click_device_image(x, y, serialno=None):
    device, serialno = ViewClient.connectToDeviceOrExit(verbose=False, serialno=serialno)
    device.touch(x, y)


def find_image_in_screen(image, serialno=None):
    if not image.endswith(".png"):
        image += ".png"
    take_device_screenshot(serialno=serialno)
    return find_image_in_another_image(image, "screen")
