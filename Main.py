import random

import asyncio
from discord import Game
from discord import Message
from discord import Status
from discord.ext import commands

BOT_PREFIX = "!"

# real token/bot
BOT_NAME = "Bottalo Bill"
TOKEN = "NTA5OTU4MDIzMjkzNDM1OTE1.DsVYQA.lluEGtYuhDYTTxOR8t_QN-t6nxU"

# tester token/bot
# BOT_NAME = "TestBot"
# TOKEN = "NTExMDIyOTIzNjcxMjczNDc0.Dsk4PQ.b5RCBuq1OlLYVkHnpMTNgh0dgmM"

client = commands.Bot(command_prefix=BOT_PREFIX)


# - MENUS - ##################################################################

@client.command()
async def howdy(ctx):
    """Say 'howdy' when a user types '!howdy' and list basic commands."""
    await ctx.send("howdy, {0}".format(ctx.author))
    await ctx.send("i've got maps and information, partner, what're ya lookin' for?")
    await ctx.send("------")
    await ctx.send("!maps")
    await ctx.send("!info")


# - INFO - ###################################################################

@client.command()
async def info(ctx):
    """List info commands."""
    await ctx.send("i've got plenty of information to share, whad'ya want to know?")
    await ctx.send("!animals - legendary animal information")
    await ctx.send("!fish - legendary fish information")
    await ctx.send("!ciginfo - cigarette card information")
    await ctx.send("!mystery - mysteries information")


@client.command(name="animals")
async def animal_info(ctx):
    """List animal information."""
    await ctx.send("if you've gone hunting with Hosea you should have a map in your satchel...")
    await ctx.send("if that isn't enough you can find more information here")
    await ctx.send("https://www.eurogamer.net/articles/2018-11-09-red-dead-redemption-2-legendary-animal-locations-4975")


@client.command(name="fish")
async def fish_info(ctx):
    """List fish information."""
    await ctx.send("if you've met with Jeremy Gill you should have a map in your satchel...")
    await ctx.send("if that isn't enough you can find more information here")
    await ctx.send("https://www.eurogamer.net/articles/2018-11-09-red-dead-redemption-2-legendary-fish-locations-4975")


@client.command(name="ciginfo")
async def cig_info(ctx):
    """List cigarette card information"""
    await ctx.send("you can scour the land looking for cigarette cards, but there may be an easier way")
    await ctx.send("http://www.powerpyx.com/red-dead-redemption-2-all-cigarette-card-locations/")


@client.command(name="mystery")
async def mystery_info(ctx):
    """List mystery information."""
    await ctx.send("there are a lot of mysteries out there")
    await ctx.send("if yer not afraid of spoilin' some fun, you can find learn more here")
    await ctx.send("https://www.gamespot.com/videos/uncovering-red-dead-redemption-2s-biggest-mystery/2300-6447057/")


# - MAPS - ###################################################################

@client.command()
async def maps(ctx):
    """List map commands."""
    await ctx.send("there's a lot to find out in the country, here's the maps i got for ya'")
    await ctx.send("------")
    await ctx.send("!dream - dreamcatcher locations")
    await ctx.send("!carvin - rock carving locations")
    await ctx.send("!cigmaps - cigarette card locations")
    await ctx.send("!hadino - New Hanover & Ambarino dino bone locations")
    await ctx.send("!wedino - West Elizabeth dino bone locations")
    await ctx.send("!nadino - New Austin dino bone locations")


@client.command(name="dino")
async def dino_maps(ctx):
    """"List dino bones map commands."""
    await ctx.send("if you're out looking for dino bones, take a look at these maps here")
    await ctx.send("------")
    await ctx.send("!hadino - New Hanover & Ambarino dino bone locations")
    await ctx.send("!wedino - West Elizabeth dino bone locations")
    await ctx.send("!nadino - New Austin dino bone locations")


@client.command(name="cigmaps")
async def cigarette_cards(ctx):
    """List cigarette cards map commands."""
    await ctx.send("there's a lotta cards out there, which ones are ya lookin' for?")
    await ctx.send("------")
    await ctx.send("!aicigs - amazing inventions cigarette cards locations")
    await ctx.send("!awpcigs - artists, writers, and poets cigarette cards locations")
    await ctx.send("!bhcigs - breeds of horses cigarette cards locations")
    await ctx.send("!fgcigs - famous gunslingers cigarette cards locations")
    await ctx.send("!faacigs - fauna of north america cigarette cards locations")
    await ctx.send("!flacigs - flora of north america cigarette cards locations")
    await ctx.send("!gbcigs - gems of beauty cigarette cards locations")
    await ctx.send("!mtcigs - marvels of time cigarette cards locations")
    await ctx.send("!pacigs - prominent americans cigarette cards locations")
    await ctx.send("!sscigs - stars of the stage cigarette cards locations")
    await ctx.send("!vacigs - vistas of america cigarette cards locations")
    await ctx.send("!wccigs - the world's champions cigarette cards locations")


# - ROCK CARVINGS - ##########################################################

@client.command(name="carv")
async def rock_carvings(ctx):
    await ctx.send("http://www.powerpyx.com/wp-content/uploads/red-dead-redemption-2-rock-carvings-locations-map.jpg".format(ctx))


# - DREAMCATCHERS - ##########################################################

@client.command(name="dream")
async def rock_carvings(ctx):
    await ctx.send("https://cdn.gamerant.com/wp-content/uploads/red-dead-redemption-2-map-dreamcatchers-notes-729x410.jpg.webp".format(ctx))


# - DINO BONES - #############################################################

@client.command(name="hadino")
async def hanover_ambarino_dino_bones(ctx):
    await ctx.send("https://assets.vg247.com/current/2018/11/red-dead-redemption-2-dinosaur-bones-1-768x501.png".format(ctx))


@client.command(name="wedino")
async def west_elizabeth_dino_bones(ctx):
    await ctx.send("https://assets.vg247.com/current/2018/11/red-dead-redemption-2-dinosaur-bones-2-768x445.png".format(ctx))


@client.command(name="nadino")
async def new_austin_dino_bones(ctx):
    await ctx.send("https://assets.vg247.com/current/2018/11/red-dead-redemption-2-dinosaur-bones-3-768x467.png".format(ctx))


# - CIGARETTE CARDS - ########################################################

@client.command(name="aicigs")
async def amazing_inventions_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/10/amazing-inventions-cigarette-cards-red-dead-redemption-2-update.jpg".format(ctx))


@client.command(name="awpcigs")
async def artists_writers_poets_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/10/all-artists-writers-and-poets-cigarette-card-locations-map.jpg".format(ctx))



@client.command(name="bhcigs")
async def breeds_of_horses_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/10/all-breeds-of-horses-cigarette-card-maps.jpg".format(ctx))


@client.command(name="fgcigs")
async def famous_gunslingers_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/10/all-famous-gunslingers-cigarette-card-locations-map.jpg".format(ctx))


@client.command(name="facigs")
async def fauna_of_north_america_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/10/all-fauna-of-north-america-cigarette-cards-location-map.jpg".format(ctx))


@client.command(name="flacigs")
async def flora_of_north_america_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-flora-of-north-america-cigarette-cards-location-map.jpg".format(ctx))

@client.command(name="gbcigs")
async def gems_of_beauty_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-gems-of-beauty-cigarette-card-locations-map.jpg".format(ctx))


@client.command(name="mtcigs")
async def marvels_of_travel_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-marvels-of-travel-cigarette-card-locations-map.jpg".format(ctx))


@client.command(name="pacigs")
async def prominent_americans_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-prominent-americans-cigarette-cards-location-map.jpg".format(ctx))


@client.command(name="sscigs")
async def stars_of_the_stage_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-stars-of-the-stage-cigarette-card-locations-map.jpg".format(ctx))


@client.command(name="vacigs")
async def vistas_of_america_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-vistas-of-america-cigarette-card-locations-map.jpg".format(ctx))


@client.command(name="wccigs")
async def the_worlds_champions_cards(ctx):
    await ctx.send("https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-worlds-champions-cigarette-card-locations-map.jpg".format(ctx))


async def play_games():
    """Allow bot to 'play' game and periodically switch between them."""
    await client.wait_until_ready()
    playing_game = True
    game = [
        "Poker",
        "Blackjack",
        "Horseshoes",
        "Red Dead Revolver",
        "Red Dead Redemption",
        "Red Dead Redemption 2",
        "Sunset Riders",
        "Custer's Revenge",
        "Gun Fight",
        "Outlaw"
    ]
    while not client.is_closed():
        if playing_game:
            await client.change_presence(game=Game(name=random.choice(game)))
            await asyncio.sleep(3600)  # run every 1 hour
            playing_game = False
        elif not playing_game:
            await client.change_presence(status=Status.online)
            await asyncio.sleep(900)  # run every 15 minutes
            playing_game = True


@client.command()
async def clear(ctx, amount: int):
    """Clear messages from channel and re-posts/pins command list."""
    await ctx.channel.purge(limit=amount)
    await asyncio.sleep(3)
    await ctx.send("**__Bottalo Bill Commands:__**\n"
                   ".\n"
                   "__Info Commands:__\n"
                   "!animals - legendary animal information\n"
                   "!fish - legendary fish information\n"
                   "!ciginfo - cigarette card information\n"
                   "!mystery - mysteries information\n"
                   ".\n"
                   "__Map Commands:__\n"
                   "!dream - dreamcatcher locations\n"
                   "!carvin - rock carving locations\n"
                   "!cigmaps - cigarette card locations\n"
                   ".\n"
                   "!hadino - New Hanover & Ambarino dino bone locations\n"
                   "!wedino - West Elizabeth dino bone locations\n"
                   "!nadino - New Austin dino bone locations\n"
                   ".\n"
                   "!aicigs - amazing inventions cigarette cards locations\n"
                   "!awpcigs - artists, writers, and poets cigarette cards locations\n"
                   "!bhcigs - breeds of horses cigarette cards locations\n"
                   "!fgcigs - famous gunslingers cigarette cards locations\n"
                   "!faacigs - fauna of north america cigarette cards locations\n"
                   "!flacigs - flora of north america cigarette cards locations\n"                    "!gbcigs - gems of beauty cigarette cards locations"
                   "!mtcigs - marvels of time cigarette cards locations\n"
                   "!pacigs - prominent americans cigarette cards locations\n"
                   "!sscigs - stars of the stage cigarette cards locations\n"
                   "!vacigs - vistas of america cigarette cards locations\n"
                   "!wccigs - the world's champions cigarette cards locations\n"
                   ".\n"
                   "!clear 100 - clear last 100 messages and re-post commands")
    msg = await ctx.channel.history().get(author__name=BOT_NAME)
    await Message.pin(msg)


@client.event
async def on_ready():
    """Print logged in message to console to know bot is ready."""
    log_msg = "Logged in as: " + client.user.name
    print(log_msg)
    print("-" * len(log_msg))

client.loop.create_task(play_games())
client.run(TOKEN)
