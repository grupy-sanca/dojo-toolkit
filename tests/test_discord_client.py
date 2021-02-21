from dojo_toolkit.discord_client import DiscordClient


def test_send_message():
    client = DiscordClient('token')

    response = client.send_message("Olá mundo")

    assert response.status_code == 200
