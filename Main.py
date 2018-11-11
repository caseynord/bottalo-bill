from discord.ext import commands

BOT_PREFIX = ("!", "?")

# real token
# TOKEN = "NTA5OTU4MDIzMjkzNDM1OTE1.DsVYQA.lluEGtYuhDYTTxOR8t_QN-t6nxU"

# tester token
TOKEN = "NTExMDIyOTIzNjcxMjczNDc0.Dsk4PQ.b5RCBuq1OlLYVkHnpMTNgh0dgmM"

client = commands.Bot(command_prefix=BOT_PREFIX)

# TODO: update discord pinned notification
# TODO: add link to cigarette card exploit
# TODO: legendary animals locations
# TODO: add links to mysteries


# - MENUS - ##################################################################

@client.command()
async def howdy(ctx):
    r"""Say "howdy" when a user types "!howdy" and list basic commands."""
    await ctx.send("howdy, {0}".format(ctx.author))
    await ctx.send("i've got maps and information, partner, what're ya lookin' for?")
    await ctx.send("------")
    await ctx.send("!maps")
    await ctx.send("!info")


@client.command()
async def maps(ctx):
    """List map commands."""
    await ctx.send("there's a lot to find out in the country, here's the maps i got for ya'")
    await ctx.send("------")
    await ctx.send("!hadino - New Hanover & Ambarino dino bone locations")
    await ctx.send("!wedino - West Elizabeth dino bone locations")
    await ctx.send("!nadino - New Austin dino bone locations")
    await ctx.send("!carvin - rock carving locations")
    await ctx.send("!cigcards - cigarette card locations")


@client.command(name="dino")
async def dino_maps(ctx):
    """"List dino bones map commands."""
    await ctx.send("if you're out looking for dino bones, take a look at these maps here")
    await ctx.send("------")
    await ctx.send("!hadino - New Hanover & Ambarino dino bone locations")
    await ctx.send("!wedino - West Elizabeth dino bone locations")
    await ctx.send("!nadino - New Austin dino bone locations")


@client.command(name="cigcards")
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


# - MAPS - ###################################################################

# - DINO BONES - #############################################################

@client.command(name="hadino")
async def hanover_ambarino_dino_bones(ctx):
    await ctx.send('https://assets.vg247.com/current/2018/11/red-dead-redemption-2-dinosaur-bones-1-768x501.png'.format(ctx))


@client.command(name="wedino")
async def west_elizabeth_dino_bones(ctx):
    await ctx.send('https://assets.vg247.com/current/2018/11/red-dead-redemption-2-dinosaur-bones-2-768x445.png'.format(ctx))


@client.command(name="nadino")
async def new_austin_dino_bones(ctx):
    await ctx.send('https://assets.vg247.com/current/2018/11/red-dead-redemption-2-dinosaur-bones-3-768x467.png'.format(ctx))


# - ROCK CARVINGS - ##########################################################

@client.command(name="carv")
async def rock_carvings(ctx):
    await ctx.send('http://www.powerpyx.com/wp-content/uploads/red-dead-redemption-2-rock-carvings-locations-map.jpg'.format(ctx))


# - CIGARETTE CARDS - ########################################################

@client.command(name="aicigs")
async def amazing_inventions_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/10/amazing-inventions-cigarette-cards-red-dead-redemption-2-update.jpg'.format(ctx))


@client.command(name="awpcigs")
async def artists_writers_poets_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/10/all-artists-writers-and-poets-cigarette-card-locations-map.jpg'.format(ctx))



@client.command(name="bhcigs")
async def breeds_of_horses_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/10/all-breeds-of-horses-cigarette-card-maps.jpg'.format(ctx))


@client.command(name="fgcigs")
async def famous_gunslingers_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/10/all-famous-gunslingers-cigarette-card-locations-map.jpg'.format(ctx))


@client.command(name="facigs")
async def fauna_of_north_america_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/10/all-fauna-of-north-america-cigarette-cards-location-map.jpg'.format(ctx))


@client.command(name="flacigs")
async def flora_of_north_america_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-flora-of-north-america-cigarette-cards-location-map.jpg'.format(ctx))

@client.command(name="gbcigs")
async def gems_of_beauty_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-gems-of-beauty-cigarette-card-locations-map.jpg'.format(ctx))


@client.command(name="mtcigs")
async def marvels_of_travel_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-marvels-of-travel-cigarette-card-locations-map.jpg'.format(ctx))


@client.command(name="pacigs")
async def prominent_americans_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-prominent-americans-cigarette-cards-location-map.jpg'.format(ctx))


@client.command(name="sscigs")
async def stars_of_the_stage_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-stars-of-the-stage-cigarette-card-locations-map.jpg'.format(ctx))


@client.command(name="vacigs")
async def vistas_of_america_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-vistas-of-america-cigarette-card-locations-map.jpg'.format(ctx))


@client.command(name="wccigs")
async def the_worlds_champions_cards(ctx):
    await ctx.send('https://d1lss44hh2trtw.cloudfront.net/assets/editorial/2018/11/all-worlds-champions-cigarette-card-locations-map.jpg'.format(ctx))


'''
@client.event
async def howdy(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Howdy, {0.author.mention}'.format(message)
        await message.channel.send(msg)
'''

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
