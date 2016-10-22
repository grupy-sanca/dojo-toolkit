import os

from .utils import mock

# workaround to tests run on travis
try:
    from pgi.repository import Notify, GdkPixbuf
except:
    Notify = mock.Mock()
    GdkPixbuf = mock.Mock()

from .settings import ASSETS_DIR


class BaseNotifier(object):
    def __init__(self):
        self.fail_img_path = os.path.join(ASSETS_DIR, 'r.jpg')
        self.success_img_path = os.path.join(ASSETS_DIR, 'g.jpg')

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
        Notify.init('not')
        return Notify.Notification.new('', '', '')

    def notify(self, message, image_path='', timeout=5 * 60 * 1000):
        self._notifier.update(message, '', image_path)
        self._notifier.set_timeout(timeout)
        self._notifier.show()

    def success(self, message):
        self.notify(message, self.success_img_path)

    def fail(self, message):
        self.notify(message, self.fail_img_path)
