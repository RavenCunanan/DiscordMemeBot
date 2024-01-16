import discord
import requests
import json
import datetime

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']


class MyClient(discord.Client):
  
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_time = datetime.datetime.now()

  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

    channel = self.get_channel() #enter discord channel ID
        
    if channel:
        await channel.send("Hello, I'm online! Type $help for commands.")
    else:
        print("Channel not found. Make sure to replace CHANNEL_ID with the correct channel ID.")
  
  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello World!')

    elif message.content.startswith('$help'):
      await message.channel.send("Commands are : $hello, $help, $meme, $status")

    elif message.content.startswith('$meme'):
      await message.channel.send(get_meme())

    elif message.content.startswith('$status'):
            uptime = datetime.datetime.now() - self.start_time
            await message.channel.send(f"I am online and my uptime is {uptime}")



intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Enter Token Here') # Replace with your own token.

