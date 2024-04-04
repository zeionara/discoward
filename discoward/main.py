from os import environ as env

import discord as ds

intents = ds.Intents.all()
intents.message_content = True

bot = ds.Client(intents = intents)


@bot.event
async def on_ready():
    global game_creator
    game_creator = await bot.fetch_user(396820551974387733)
    print('foo')
    await game_creator.send("Hello")


bot.run(env.get('DISCOWARD_BOT_TOKEN'))
