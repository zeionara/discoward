from requests import get


class DiscordClient:
    def __init__(self, guild_id: int, channel_id: int):
        self.guild_id = guild_id
        self.channel_id = channel_id

    # def _post(self):

    # def describe(self):
    #     self._post(
    #         {
    #             "op": 4,
    #             "d": {
    #                 "guild_id": "41771983423143937",
    #                 "channel_id": "127121515262115840",
    #                 "self_mute": False,
    #                 "self_deaf": False
    #             }
    #         }
    #     )

    def connect(self):
        get(
            ':

