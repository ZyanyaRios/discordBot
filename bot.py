from discord.ext import commands
import discord
from dataclasses import dataclass

 # with instruction from https://www.youtube.com/watch?v=2k9x0s3awss&t=1085s
 # bot includes commands to start, add, and say hello when promted with !(insert)
 

BOT_TOKEN = "###" #redacted information
CHANNEL_ID = 0

@dataclass
class Session: #created a session class 
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix="!", intents= discord.Intents.all())
session = Session()

@bot.command()
async def start(ctx):
    if session.is_active: #checking if the session is already active 
        channel = bot.get_channel(CHANNEL_ID) #grabbing channel id 
        await channel.send("Session active already")
        return
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    await ctx.send(f"Study session started started at {readable_time}")



@bot.event
async def on_ready():
    print("Hellllooooo! Ready :)")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hellllooooo! Ready :)")


@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)
    await ctx.send(f"Result: {result}")


bot.run(BOT_TOKEN)