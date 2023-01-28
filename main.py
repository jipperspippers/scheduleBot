import discord
import os
from dotenv import load_dotenv
from discord.ext import commands



intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/', intents = intents)

member = discord.Member

load_dotenv()
tk = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# create event then create a role
# delete event then delete a role
@bot.event
async def on_scheduled_event_create(Event):
    #name of role should be (trainer is the creator) Trainer - Date
    time = Event.start_time.isoformat(timespec="hours")
    eventName = Event.name
    await Event.guild.create_role(name = eventName + " at " + time)
    return


@bot.event
async def on_scheduled_event_delete(Event):
    
    #remove the roles of the users automatically

    time = Event.start_time.isoformat(timespec="hours")
    eventName = Event.name
    role = discord.utils.get(Event.guild.roles, name=eventName + " at " + time)
    await role.delete() 
    
    return

# remove roles or add roles
@bot.event
async def on_scheduled_event_user_add(Event, user):
    #add new role
    time = Event.start_time.isoformat(timespec="hours")
    eventName = Event.name
    member = Event.guild.get_member(user.id)
    role = discord.utils.get(Event.guild.roles, name=eventName+ " at " + time) 
    await member.add_roles(role)
    return

@bot.event
async def on_scheduled_event_user_remove(Event, user):
    time = Event.start_time.isoformat(timespec="hours")
    eventName = Event.name
    member = Event.guild.get_member(user.id)

    role = discord.utils.get(Event.guild.roles, name=eventName+ " at " + time) 

    await member.remove_roles(role)
    return


##
#create a guild for user



bot.run(token=tk)
