from unittest import mock

import pytest

from dojo_toolkit.notifier import NotifierClient
from dojo_toolkit.settings import ASSETS_DIR

pytestmark = pytest.mark.asyncio

@mock.patch("dojo_toolkit.notifier.DesktopNotifier")
def test_init(mock_desktop_notifier):
    """Test NotifierClient initialization."""
    notifier_client = NotifierClient()
    assert notifier_client.notifier == mock_desktop_notifier.return_value
    assert notifier_client.fail_img_path == f"{ASSETS_DIR}/./assets/failure_notification_image.jpg"
    assert (notifier_client.success_img_path ==
            f"{ASSETS_DIR}/./assets/success_notification_image.jpg")
    mock_desktop_notifier.assert_called_once_with(app_name="dojo toolkit")

@mock.patch("dojo_toolkit.notifier.Icon")
@mock.patch("dojo_toolkit.notifier.Path")
@mock.patch("dojo_toolkit.notifier.asyncio.create_task")
def test_notify_creates_task(mock_create_task, mock_path, mock_icon):
    mock_notifier = mock.MagicMock()
    client = NotifierClient()
    client.notifier = mock_notifier

    mock_resolved_path = mock.Mock()
    mock_path.return_value.resolve.return_value = mock_resolved_path
    mock_icon_instance = mock.Mock()
    mock_icon.return_value = mock_icon_instance

    client.notify("Hello", title="Test", image_path="some/image.png", timeout=1234)

    mock_path.assert_called_once_with("some/image.png")
    mock_icon.assert_called_once_with(path=mock_resolved_path)
    mock_notifier.send.assert_called_once_with(
        icon=mock_icon_instance,
        title="Test",
        message="Hello",
        urgency=mock.ANY,
        sound=mock.ANY,
        timeout=1234
    )
    mock_create_task.assert_called_once()

@mock.patch.object(NotifierClient, "notify")
def test_success_calls_notify_with_success_image(mock_notify):
    client = NotifierClient()
    client.success("Great!")

    mock_notify.assert_called_once_with(
        message="Great!",
        image_path=client.success_img_path
    )

@mock.patch.object(NotifierClient, "notify")
def test_failure_calls_notify_with_failure_image(mock_notify):
    client = NotifierClient()
    client.failure("Oops!")

    mock_notify.assert_called_once_with(
        message="Oops!",
        image_path=client.fail_img_path
    )
