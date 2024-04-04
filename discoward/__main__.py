from click import group, argument, option

from discord import VoiceChannel
from discord.ext import voice_recv


@group()
def main():
    pass


@main.command()
@option('--guild-id', type = int, default = 41771983423143937)
@option('--channel-id', type = int, default = 828018838683123712)
def run(guild_id: int, channel_id: int):
    voice_channel = VoiceChannel(guild = guild_id, data = {'id': channel_id})
    voice_client = voice_channel.connect(cls = voice_recv.VoiceRecvClient)


if __name__ == '__main__':
    main()
