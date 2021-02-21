import os
from dataclasses import dataclass

import requests

DISCORD_TOKEN = os.getenv('TOKEN')


@dataclass
class Response:
    status_code: int


class DiscordClient:
    def __init__(self, token):
        self.token = token

    def send_message(self, message):
        response = requests.post(
            'https://discord.com/api/channels/812655658499440690/messages',
            json={
                "content": "Hello, World!",
                "tts": False,
                "embed": {
                    "title": "Hello, Embed!",
                    "description": "This is an embedded message."
                }
            },
            headers={
                'Authorization': f'Bot {self.token}'
            },
        )
        return Response(status_code=response.status_code)
