import discord
import responses
from Data import store_chat

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "MTExMTA1Njc1ODE5NTA5NzYyOA.GXMtP6.csDy7WuA29Wb41Z6zESOYRCd4AusNNBACOMyLY"

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        try:
            if message.author == client.user:
                return
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)
            # message_time = str(message.time

            chat = f"{username} said: '{user_message}' '({channel})'"
            store_chat.store(chat)

            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)
            else:
                await send_message(message, user_message, is_private=False)

        except Exception as e:
            print(e)

    client.run(TOKEN)
