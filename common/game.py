from time import sleep

from com.dtmilano.android.viewclient import ViewClient
from common import find_image_in_screen, click_device_image


class RoyalRevolt2(object):
    def __init__(self, serialno=None):
        self.device, serialno = ViewClient.connectToDeviceOrExit(verbose=False, serialno=serialno)

    def _loaded(self):
        return True  # TODO: Check if the game is loaded

    def start(self):
        self.device.startActivity(component="com.flaregames.rrtournament/com.keenflare.rrtournament.RRActivity")
        if not self._loaded():
            sleep(25)

    def close_views(self):
        pos = find_image_in_screen("x")
        while pos:
            click_device_image(*pos)
            pos = find_image_in_screen("x")
