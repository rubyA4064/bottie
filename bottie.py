import client as client
import discord
import os
TOKEN = os.environ['DISCORD_TOKEN']
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

async def on_ready():
    print("OWO TIME")
    await client.change_presence(game=discord.Game(name=""))
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "WELOME":
        await client.send_message(message.channel, "WELOME")
@bot.command()
async def testieng(ctx, input: str, seed: int):
    import random
    print("Input a string to be encoded:")
    s = input()
    print("Input a seed (integer):")
    seed = int(input())
    if seed>100:
        seed=random.randint(0,101)
    encoded = ""
    i = 0
    j = seed
    for j in range(seed, len(s)):
        char = chr(int(str(ord(s[j]))[::-1]))
        encoded = char + encoded
    for i in range(0, seed):
        char = chr(int(str(ord(s[i]))[::-1]))
        encoded = char + encoded
    print(encoded)
@bot.command()
async def rubyscript(ctx, input: str, seed: int):
    import math
    print("What would you like to encode?")

    print("What seed(integer) do you want to use?")


    firstLength = len(input)

    def reverse_int(n):
        ans = 0
        while n > 0:
            (d, n) = (n % 10, n // 10)
            ans = 10 * ans + d
        return (ans)

    def split(word):
        return [char for char in word]

    def swapPos(list, pos1, pos2):

        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list

    chars = split(input)

    for x in range(0, seed):
        chars.append(chars[0])
        chars.remove(chars[firstLength])
    evenOdd = firstLength % 2
    a = 0
    b = firstLength - 1
    chars.reverse()
    chars1 = []
    chars2 = []
    for x in range(0, firstLength):
        chars1.append(ord(chars[x]))

    for x in range(0, firstLength):
        chars1[x] = reverse_int(chars1[x])
    for x in range(0, firstLength):
        chars1[x] = chr(chars1[x])

    output11="".join(chars1)

    output = output11
    await ctx.send('`' + output + '`')

client = discord.Client()

@bot.event
async def testing(ctx, input: str, seed: int):

    output="boooooop"
    await ctx.send('`' + output + '`')
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

bot.run(TOKEN)
# Now you can use $rubyscript [input] [output]
