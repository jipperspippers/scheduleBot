import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/')
client = discord.Client()
user = discord.User()

guild = client.get_guild()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# create event then create a role
# delete event then delete a role

## GETTING EVENTS

# remove roles or add roles
@user.event
async def on_scheduled_event_user_add(event, user):
    return

@user.event
async def on_scheduled_event_user_remove(event, user):
    return


##
#create a guild for user



bot.run(TOKEN)
