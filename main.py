import discord 
import os

client = discord.Client()

@client.event
async def on_ready():
  print ('Loged in as {0.user}' .format (client))

@client.event 
async def on_message(Message):
  if Message.author == client.user:
    return

  if Message.content.startswith('.ping'):
    await Message.channel.send('pong')
   
  if Message:
    x = str(Message.author)
    y = str(Message.author.nick)
    z = str(Message.content)
    u = str(Message.channel)
    
    a = str('''
Discord ID:'''+x+''' 
Nick/Realname: '''+y+'''
Channel: '''+u+'''
Message: ''' +z+"""
""")
    
    
    print(a)
    text_file = open("sendme.txt","a")
    text_file.write(a)
    text_file.close()

#x = input('i am a banana'):
#dk = open("discordkey.txt","r")
#key = dk.read()
#dk.close()

key = str(input('Key -- '))

client.run(key)
