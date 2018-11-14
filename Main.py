import random

import asyncio
from discord import Game
from discord import Message
from discord import Status
from discord.ext import commands

import Bot_Commands


BOT_PREFIX = "!"

# real token/bot
BOT_NAME = "Bottalo Bill"
TOKEN = "NTA5OTU4MDIzMjkzNDM1OTE1.DsVYQA.lluEGtYuhDYTTxOR8t_QN-t6nxU"

# tester token/bot
# BOT_NAME = "TestBot"
# TOKEN = "NTExMDIyOTIzNjcxMjczNDc0.Dsk4PQ.b5RCBuq1OlLYVkHnpMTNgh0dgmM"

client = commands.Bot(command_prefix=BOT_PREFIX)


# - FETCH COMMANDS- #########################################################

def format_commands(commands_dict):
    command_string = ""
    for key, value in commands_dict.items():
        command_string += "*" + key + "* - " + value[0] + "\n"
    return command_string


def query_format_commands(commands_dict, match):
    command_string = ""
    for key, value in commands_dict.items():
        if match in key:
            command_string += "*" + key + "* - " + value[0] + "\n"
    return command_string


@client.command(name="map", aliases=["m"])
async def fetch_map(ctx, arg):
    for key, value in Bot_Commands.maps.items():
        if key == arg:
            await ctx.send(value[1])


@client.command(name="info", aliases=["i"])
async def fetch_info(ctx, arg):
    for key, value in Bot_Commands.info.items():
        if key == arg:
            await ctx.send(value[1])


# - MENUS - ##################################################################

@client.command()
async def howdy(ctx):
    """Say 'howdy' when a user types '!howdy' and list basic commands."""
    await ctx.send("howdy, {0}".format(ctx.author) + "\n"
                   "i've got maps and information, partner, what're ya lookin' for?\n"
                   "------\n"
                   "!maps\n"
                   "!links")


@client.command()
async def links(ctx):
    """List info commands."""
    info_commands = format_commands(Bot_Commands.info)
    await ctx.send("i've got plenty of information to share, whad'ya want to know?\n"
                   "------\n" +
                   info_commands)


@client.command()
async def maps(ctx):
    """List map commands."""
    map_commands = format_commands(Bot_Commands.maps)
    await ctx.send("there's a lot to find out in the country, here's the maps i got for ya'\n"
                   "------\n"
                   "--type !map *command*\n" +
                   map_commands)


@client.command(name="dino")
async def dino_maps(ctx):
    """"List dino bones map commands."""
    dino_map_commands = query_format_commands(Bot_Commands.maps, "dino")
    await ctx.send("if you're out looking for dino bones, take a look at these maps here\n"
                   "------\n"
                   "--type !map *command*\n" +
                   dino_map_commands)


@client.command(name="cigs")
async def cigarette_cards(ctx):
    """List cigarette cards map commands."""
    cigs_map_commands = query_format_commands(Bot_Commands.maps, "cigs")
    await ctx.send("there's a lotta cards out there, which ones are ya lookin' for?\n"
                   "------\n"
                   "--type !map *command*\n" +
                   cigs_map_commands)


# - BOT COMMANDS - ##################################################################

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
async def clear(ctx):
    """Clear messages from channel and re-posts/pins command list."""
    await ctx.channel.purge()
    await asyncio.sleep(3)
    info_commands = format_commands(Bot_Commands.info)
    map_commands = format_commands(Bot_Commands.maps)
    await ctx.send("__**Bottalo Bill Commands:**__\n"
                   ".\n"
                   "__Info Commands:__\n"
                   "--type !info *command*\n" +
                   info_commands +
                   ".\n"
                   "__Map Commands:__\n"
                   "--type !map *command*\n" +
                   map_commands +
                   ".\n"
                   "__General Commands:__\n"
                   "!clear - delete channel messages")
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
