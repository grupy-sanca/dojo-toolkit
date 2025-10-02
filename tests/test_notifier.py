from unittest import mock

from dojo_toolkit.notifier import NotifierClient
from dojo_toolkit.settings import ASSETS_DIR


@mock.patch("dojo_toolkit.notifier.desktop_notifier.DesktopNotifier")
def test_init(mock_desktop_notifier):
    """Test NotifierClient initialization."""
    notifier_client = NotifierClient()
    assert notifier_client.notifier == mock_desktop_notifier.return_value
    assert notifier_client.fail_img_path == f"{ASSETS_DIR}/./assets/failure_notification_image.jpg"
    assert (
        notifier_client.success_img_path == f"{ASSETS_DIR}/./assets/success_notification_image.jpg"
    )
    mock_desktop_notifier.assert_called_once_with(app_name="dojo toolkit")


@mock.patch("dojo_toolkit.notifier.asyncio.create_task")
@mock.patch("dojo_toolkit.notifier.desktop_notifier.Icon")
@mock.patch("dojo_toolkit.notifier.desktop_notifier.DesktopNotifier")
def test_notify(mock_desktop_notifier_cls, mock_icon_cls, mock_create_task):
    """Test that notify sends correct notification via DesktopNotifier."""
    mock_notifier_instance = mock_desktop_notifier_cls.return_value
    mock_icon_instance = mock_icon_cls.return_value

    client = NotifierClient()
    client.notify(
        message="Test Message",
        title="Test Title",
        image_path="/some/path/to/image.jpg",
        timeout=10000,
    )

    # Icon class should be called with correct path
    mock_icon_cls.assert_called_once()
    assert str(mock_icon_cls.call_args[1]["path"]).endswith("image.jpg")

    # DesktopNotifier.send should be wrapped in create_task
    mock_notifier_instance.send.assert_called_once_with(
        icon=mock_icon_instance,
        title="Test Title",
        message="Test Message",
        urgency=mock.ANY,
        sound=mock.ANY,
        timeout=10000,
    )

    mock_create_task.assert_called_once()


@mock.patch.object(NotifierClient, "notify")
def test_success(mock_notify):
    """Test success notification uses the correct image."""
    client = NotifierClient()
    client.success("Operation succeeded")

    mock_notify.assert_called_once_with(
        message="Operation succeeded",
        image_path=client.success_img_path,
    )


@mock.patch.object(NotifierClient, "notify")
def test_failure(mock_notify):
    """Test failure notification uses the correct image."""
    client = NotifierClient()
    client.failure("Operation failed")

    mock_notify.assert_called_once_with(
        message="Operation failed",
        image_path=client.fail_img_path,
    )
