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
discordkey =
dk = open("discordkey.txt","r")
dk.read(discordkey)
dk.close()

client.run(discordkey)







"""
Help on package discord:

NAME
    discord

DESCRIPTION
    Discord API Wrapper
    ~~~~~~~~~~~~~~~~~~~
    
    A basic wrapper for the Discord API.
    
    :copyright: (c) 2015-present Rapptz
    :license: MIT, see LICENSE for more details.

PACKAGE CONTENTS
    __main__
    abc
    activity
    appinfo
    asset
    audit_logs
    backoff
    calls
    channel
    client
    colour
    context_managers
    embeds
    emoji
    enums
    errors
    file
    flags
    gateway
    guild
    http
    integrations
    invite
    iterators
    member
    mentions
    message
    mixins
    object
    oggparse
    opus
    partial_emoji
    permissions
    player
    raw_models
    reaction
    relationship
    role
    shard
    state
    sticker
    team
    template
    user
    utils
    voice_client
    webhook
    widget

CLASSES
    builtins.tuple(builtins.object)
        VersionInfo
    
    class VersionInfo(builtins.tuple)
     |  VersionInfo(major, minor, micro, releaselevel, serial)
     |  
     |  VersionInfo(major, minor, micro, releaselevel, serial)
     |  
     |  Method resolution order:
     |      VersionInfo
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getnewargs__(self)
     |      Return self as a plain tuple.  Used by copy and pickle.
     |  
     |  __repr__(self)
     |      Return a nicely formatted representation string
     |  
     |  _asdict(self)
     |      Return a new dict which maps field names to their values.
     |  
     |  _replace(self, /, **kwds)
     |      Return a new VersionInfo object replacing specified fields with new values
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  _make(iterable) from builtins.type
     |      Make a new VersionInfo object from a sequence or iterable
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(_cls, major, minor, micro, releaselevel, serial)
     |      Create new instance of VersionInfo(major, minor, micro, releaselevel, serial)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  major
     |      Alias for field number 0
     |  
     |  minor
     |      Alias for field number 1
     |  
     |  micro
     |      Alias for field number 2
     |  
     |  releaselevel
     |      Alias for field number 3
     |  
     |  serial
     |      Alias for field number 4
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  _field_defaults = {}
     |  
     |  _fields = ('major', 'minor', 'micro', 'releaselevel', 'serial')
     |  
     |  _fields_defaults = {}
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.

DATA
    __copyright__ = 'Copyright 2015-present Rapptz'
    __license__ = 'MIT'
    __title__ = 'discord'
    version_info = VersionInfo(major=1, minor=7, micro=2, releaselevel='fi...

VERSION
    1.7.2

AUTHOR
    Rapptz

FILE
    /opt/virtualenvs/python3/lib/python3.8/site-packages/discord/__init__.py"""