import os
from unittest import mock

from dojo_toolkit.settings import ASSETS_DIR

# workaround to tests run on travis
try:
    import gi

    gi.require_version("Notify", "0.7")
    from gi.repository import GdkPixbuf, Notify
except ImportError:
    Notify = mock.Mock()
    GdkPixbuf = mock.Mock()


class BaseNotifier:
    def __init__(self):
        self.fail_img_path = os.path.join(ASSETS_DIR, "r.jpg")
        self.success_img_path = os.path.join(ASSETS_DIR, "g.jpg")

    def get_notifier(self):
        raise NotImplementedError()

    def notify(self, message, image=None):
        raise NotImplementedError()


class GnomeNotifier(BaseNotifier):
    def __init__(self):
        super(GnomeNotifier, self).__init__()

        self.fail_img = GdkPixbuf.Pixbuf.new_from_file(self.fail_img_path)
        self.success_img = GdkPixbuf.Pixbuf.new_from_file(self.success_img_path)

        self._notifier = self.get_notifier()

    def get_notifier(self):
        Notify.init("not")
        return Notify.Notification.new("", "", "")

    def notify(self, message, image_path="", timeout=5 * 60 * 1000):
        self._notifier.update(message, "", image_path)
        self._notifier.set_timeout(timeout)
        self._notifier.show()

    def success(self, message):
        self.notify(message, self.success_img_path)

    def fail(self, message):
        self.notify(message, self.fail_img_path)


notifier = GnomeNotifier()
