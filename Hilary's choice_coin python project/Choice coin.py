import discord 
import os
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

print('bot done training')


client = discord.Client()

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

        
    if message.content.startswith('Bot'):
        response = chatbot.request(message.content[4:])
        await message.channel.send(response)

client.run('OTI3NzkyMTYzMTU5NDIwOTQ4.YdPXyQ.Md8dv0O_k4g27L4jUmoxF6rHI3s')