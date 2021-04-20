# bot.py
import os
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name="no")
async def send_bugs_no_gif(ctx):
    bugs_gif = "https://i.pinimg.com/originals/17/a1/7a/17a17ae6b93faf667b39af6d8fe34d68.gif"
    await ctx.channel.send(bugs_gif)

@bot.command(name="our")
async def send_our_image(ctx):
    bugs_gif = "https://i.kym-cdn.com/photos/images/newsfeed/001/866/880/db1.png"
    await ctx.channel.send(bugs_gif)

@bot.command(name="yes")
async def send_yes_gif(ctx):
    bugs_gif = "https://media4.giphy.com/media/3oFzm7MaLnMdD1T6tG/giphy.gif"
    await ctx.channel.send(bugs_gif)

@bot.command(name="bball")
async def send_bball_gif(ctx):
    bugs_gif = "https://media2.giphy.com/media/20MkKssy0UONHwlnIc/giphy.gif"
    await ctx.channel.send(bugs_gif)

@bot.command(name="season")
async def send_season_gif(ctx):
    bugs_gif = "https://giphy.com/gifs/facebook-looney-tunes-bugs-bunny-YaXcVXGvBQlEI"
    await ctx.channel.send(bugs_gif)

@bot.command(name="starwar")
async def send_starwar_gif(ctx):
    bugs_gif = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4de125fd-9bea-4c3d-85a9-d435be728bba/d9nuq3o-8972eef5-025e-4587-941c-c890305af74a.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTpmaWxlLmRvd25sb2FkIl0sIm9iaiI6W1t7InBhdGgiOiIvZi80ZGUxMjVmZC05YmVhLTRjM2QtODVhOS1kNDM1YmU3MjhiYmEvZDludXEzby04OTcyZWVmNS0wMjVlLTQ1ODctOTQxYy1jODkwMzA1YWY3NGEuZ2lmIn1dXX0.8ltrfCZHnRqqrilqiE6bsJXdUY4mx6fY88Wqx-xMPgI"
    await ctx.channel.send(bugs_gif)


@bot.command(name="stonk")
async def send_stonk_gif(ctx):
    bugs_gif = "https://giphy.com/gifs/looneytunes-looney-tunes-bugs-bunny-pay-day-67ThRZlYBvibtdF9JH"
    await ctx.channel.send(bugs_gif)


def get_gifs(search_key):
    url = "https://api.tenor.com/v1/search"
    params = {
        "q": search_key,
        "limit": 1
    }
    resp = requests.get(url, params=params)

    # if resp.ok:
    results = resp.json()["results"]
    gif = results[0]["media"][0]["mediumgif"]["url"]

    return gif
    # return None

@bot.command(name="bugs")
async def handle_bugs(ctx):
    message = ctx.message.content.replace("!bugs ", "")
    gif_search = f"bugs bunny {message}"

    resp = get_gifs(gif_search)

    if resp:
        await ctx.channel.send(resp)
    else:
        await ctx.channel.send("got error from tenor gif")

bot.run(TOKEN)
