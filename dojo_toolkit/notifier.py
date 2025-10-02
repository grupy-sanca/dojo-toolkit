import asyncio
import os
from pathlib import Path
from dojo_toolkit.settings import ASSETS_DIR
from desktop_notifier import DesktopNotifier, Urgency, DEFAULT_SOUND, Icon

class NotifierClient:
    def __init__(self):
        self.notifier = DesktopNotifier(app_name="dojo toolkit")
        self.fail_img_path = os.path.join(ASSETS_DIR, "./assets/failure_notification_image.jpg")
        self.success_img_path = os.path.join(ASSETS_DIR, "./assets/success_notification_image.jpg")

    def notify(self, message, title="", image_path="", timeout=5 * 60 * 1000):
        icon_path = Path(image_path).resolve()
        icon = Icon(path=icon_path)

        asyncio.create_task(self.notifier.send(
            icon=icon,
            title=title,
            message=message,
            urgency=Urgency.Low,
            sound=DEFAULT_SOUND,
            timeout=timeout
        ))

    def success(self, message):
        self.notify(message=message, image_path=self.success_img_path)

    def failure(self, message):
        self.notify(message=message, image_path=self.fail_img_path)

notifier = NotifierClient()
