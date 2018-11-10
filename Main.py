from discord.ext import commands

BOT_PREFIX = ("!", "?")
TOKEN = "NTA5OTU4MDIzMjkzNDM1OTE1.DsVYQA.lluEGtYuhDYTTxOR8t_QN-t6nxU"

client = commands.Bot(command_prefix=BOT_PREFIX)


# - MENUS - ##################################################################

@client.command()
async def howdy(ctx):
    r"""Say "howdy" when a user types "!howdy" and list basic commands."""
    await ctx.send("howdy, {0}".format(ctx.author))
    await ctx.send("i've got maps and information, partner, what are ya lookin' for?")
    await ctx.send("------")
    await ctx.send("!maps")
    await ctx.send("!info")


@client.command()
async def maps(ctx):
    r"""List map commands."""
    await ctx.send("there's a lot to find out in the country, here's the maps i got for ya'")
    await ctx.send("------")
    await ctx.send("!hadino - New Hanover & Ambarino dino bone locations")
    await ctx.send("!wedino - West Elizabeth dino bone locations")
    await ctx.send("!nadino - New Austin dino bone locations")
    await ctx.send("!carv - rock carving locations")


@client.command(name="dino")
async def dino_maps(ctx):
    r"""List dino bones map commands."""
    await ctx.send("if you're out looking for dino bones, take a look at these maps here")
    await ctx.send("------")
    await ctx.send("!hadino - New Hanover & Ambarino dino bone locations")
    await ctx.send("!wedino - West Elizabeth dino bone locations")
    await ctx.send("!nadino - New Austin dino bone locations")


# - MAPS - ###################################################################

@client.command(name="hadino")
async def hanover_ambarino_dino_bones(ctx):
    await ctx.send('https://assets.vg247.com/current/2018/11/red-dead-redemption-2-dinosaur-bones-1-768x501.png'.format(ctx))


@client.command(name="wedino")
async def west_elizabeth_dino_bones(ctx):
    await ctx.send('https://assets.vg247.com/current/2018/11/red-dead-redemption-2-dinosaur-bones-2-768x445.png'.format(ctx))


@client.command(name="nadino")
async def new_austin_dino_bones(ctx):
    await ctx.send('https://assets.vg247.com/current/2018/11/red-dead-redemption-2-dinosaur-bones-3-768x467.png'.format(ctx))


@client.command(name="carv")
async def rock_carvings(ctx):
    await ctx.send('http://www.powerpyx.com/wp-content/uploads/red-dead-redemption-2-rock-carvings-locations-map.jpg'.format(ctx))


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
