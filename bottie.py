import discord
import os
TOKEN = os.environ['DISCORD_TOKEN']
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def rubyscript(ctx, input: str, seed: int):
    encode = input.lower()
    key = input.lower()

    alphabetBase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    overall = []

    def split(word):
        return [char for char in word]

    def createNum(inputs):
        inputs1 = []
        for x in range(0, len(inputs)):
            inputs1.append(int(ord(inputs[x])) - 97)
        return inputs1

    def convert(list):

        # Converting integer list to string list
        s = [str(i) for i in list]

        # Join list items using join()
        res = int("".join(s))

        return (res)

    for x in range(0, 25):
        overall.append(alphabetBase)

        alphabetBase = alphabetBase[1:] + alphabetBase[:1]

    encodeL = split(encode)
    keyL0 = split(key)

    for x in range(0, len(encode)):
        if ' ' in encodeL:
            encodeL.remove(' ')
    for x in range(0, len(key)):
        if ' ' in keyL0:
            keyL0.remove(' ')

    keyL = []
    eLen = len(encode)
    kLen = len(key)

    index = 0
    # copies key to be same length as plaintext
    for x in range(0, kLen):
        keyL.append(keyL0[x])

    while kLen < eLen:

        keyL.append(keyL0[index])
        kLen += 1
        index += 1
        if index >= len(key):
            index = 0

    keyL = createNum(keyL)
    encode = createNum(encode)

    output = []
    for x in range(0, eLen):
        output.append(overall[keyL[x]][encode[x]])

    print(''.join(output))

client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

bot.run(TOKEN)
# Now you can use $rubyscript [input] [output]