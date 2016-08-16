import os

from pgi.repository import Notify, GdkPixbuf

from .settings import ASSETS_DIR


class BaseNotifier(object):
    def __init__(self):
        self.fail_img_path = os.path.join(ASSETS_DIR, 'r.jpg')
        self.success_img_path = os.path.join(ASSETS_DIR, 'g.jpg')

    def notify(self, message, image=None):
        raise NotImplemented()


class GnomeNotifier(BaseNotifier):
    def __init__(self):
        super(GnomeNotifier, self).__init__()

        Notify.init('not')
        self._notifier = Notify.Notification.new('', '', '')

        self.fail_img = GdkPixbuf.Pixbuf.new_from_file(self.fail_img_path)
        self.success_img = GdkPixbuf.Pixbuf.new_from_file(self.success_img_path)

    def notify(self, message, image_path='', timeout=5 * 60 * 1000):
        self._notifier.update(message, '', image_path)
        self._notifier.set_timeout(timeout)
        self._notifier.show()

    def success(self, message):
        self.notify(message, self.success_img_path)

    def fail(self, message):
        self.notify(message, self.fail_img_path)
