from discord.ext import commands
import discord
import os
TOKEN = os.environ['DISCORD_TOKEN']
bot = commands.Bot(command_prefix='$')

@bot.command()
async def testing(ctx, input: str, seed: int):
    # Insert Ruby Script using "input" and "seed" for their respective purposes
    output = input
    output = "boopy beepy"
    await ctx.send('`' + output + '`')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

bot.run(TOKEN)


# Now you can use $rubyscript [input] [output]