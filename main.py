import keep_alive
import discord
from discord.ext import commands #import discord neccessaries
from discord import option

from ext import auth, names, fetch_model #import some data and functions

from rudalle import async_generate # import Kandinsky 2.1 asynchronous generation function, its needed because not asynchronous functions freezes bot until generation will be completed

import random #other neccessaries 
import requests
import base64
from io import BytesIO


intents = discord.Intents.all() 
bot = commands.Bot(command_prefix="xr7.", intents=intents) #creating bot, make sure that you enabled all intents on bot page :)

@bot.event
async def on_ready():                   # event that will let you know when bot will be ready to use
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Your Commands!!!"))

# Kandinsky Command!
@bot.slash_command(name='kandinsky', description="Generates Images by Kandinsky 2.2 (Best)")
@option("prompt", description="Enter prompt(describe image)")
@option("style", description="Choose style", choices=names.stylelist, default="none")
@option('ratio', description="Choose aspect ratio", choices=['1:1', '16:9', '9:16', '3:2', '2:3'], default='1:1')
async def kand(ctx, prompt: str, style: str, ratio: str):
    embed = discord.Embed()
    embed.title = f"Settings"
    embed.description = f'Prompt: `{prompt}`\nStyle: `{style}`\nRatio: `{ratio}`'  # create embed and send message
    embed.color = 0x751735
    embed.set_author(name="Kandinsky 2.2 text2image")
    msg = await ctx.respond(f"Generating image for {ctx.user.mention} 🖌️")
    try:
        rand_name = random.randint(0, 10000000000000000)
        await async_generate(prompt=prompt, path=f"./{ctx.user.id}_{rand_name}.png", style=style, ratio=ratio)
        # generate and save image
        file = discord.File(f"./{ctx.user.id}_{rand_name}.png", filename=f"{rand_name}.png")
        await msg.edit_original_response(content=f"{ctx.user.mention}'s image", embed=embed, file=file)  # edit message
    except Exception as e:  # catch error
        print(e)
        embed = discord.Embed(title="⚠️ Unknown error occured!",
                              description="May be you found a bug,try again!",
                              color=discord.Color.green())
        await msg.edit_original_response(embed=embed)

###
keep_alive.keep_alive()
bot.run(auth.DISCORD)
