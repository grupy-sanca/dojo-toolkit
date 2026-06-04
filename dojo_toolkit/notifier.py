import os
import pathlib

from desktop_notifier import DesktopNotifierSync, Icon

from dojo_toolkit.settings import ASSETS_DIR


class Notifier(DesktopNotifierSync):
    SUCCESS_ICON: Icon
    FAIL_ICON: Icon

    def __init__(self):
        self.SUCCESS_ICON = Icon(pathlib.Path(os.path.join(ASSETS_DIR, "s.jpg")))
        self.FAIL_ICON = Icon(pathlib.Path(os.path.join(ASSETS_DIR, "r.jpg")))
        super().__init__()

    def notify(self, message, image_path="", timeout=5 * 60 * 1000):
        self.send(title="dojo toolkit", message=message)

    def success(self, message):
        self.send(title="dojo success", message=message, icon=self.SUCCESS_ICON)

    def fail(self, message):
        self.send(title="dojo fail", message=message, icon=self.FAIL_ICON)


notifier = Notifier()
