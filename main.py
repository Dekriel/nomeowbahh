from discord.ext import commands
import asyncio


bot = commands.Bot(command_prefix=".", self_bot=True)


@bot.event
async def on_ready():
    print("ready")


@bot.command()
async def start(ctx):
    if ctx.guild.id == 921916567145570384:
        while True:
            await asyncio.sleep(2)
            await ctx.send("<@749793965796098108> SCREW YOU")


bot.run("YOUR TOKEN HERE", bot=False)
