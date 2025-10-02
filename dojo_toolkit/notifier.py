import asyncio
import os
from pathlib import Path

import desktop_notifier

from dojo_toolkit.settings import ASSETS_DIR


class NotifierClient:
    def __init__(self):
        self.notifier = desktop_notifier.DesktopNotifier(app_name="dojo toolkit")
        self.fail_img_path = os.path.join(ASSETS_DIR, "./assets/failure_notification_image.jpg")
        self.success_img_path = os.path.join(ASSETS_DIR, "./assets/success_notification_image.jpg")

    def notify(self, message, title="", image_path="", timeout=5 * 60 * 1000):
        icon_path = Path(image_path).resolve()
        icon = desktop_notifier.Icon(path=icon_path)

        asyncio.create_task(self.notifier.send(
            icon=icon,
            title=title,
            message=message,
            urgency=desktop_notifier.Urgency.Low,
            sound=desktop_notifier.DEFAULT_SOUND,
            timeout=timeout
        ))

    def success(self, message):
        self.notify(message=message, image_path=self.success_img_path)

    def failure(self, message):
        self.notify(message=message, image_path=self.fail_img_path)

notifier = NotifierClient()
