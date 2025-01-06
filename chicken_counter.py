import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

chicken_count = 0


def chicken_count_up():
    global chicken_count
    chicken_count += 2


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$hello') or message.content.startswith(
            '$hi'):
        await message.channel.send('Hello!')

    if message.content.startswith("$count"):
        await message.channel.send(f"There are {chicken_count} chickens.")

    if message.content.startswith("$add"):
        chicken_count_up()
        await message.channel.send("The amount of chickens is now " +
                                   str(chicken_count))