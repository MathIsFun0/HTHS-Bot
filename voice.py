from pyttsx3 import init
from asyncio import sleep
from os import remove
import nextcord as discord
import ffmpeg
from random import randint



async def say(client, ctx, arg):
  val = randint(0, 2147483647)
  print(val)
  user = ctx.message.author
  voice_channel = user.voice.channel
  message = arg
  channel = None
  if voice_channel != None:
    channel = voice_channel.name
    # Say stuff
    engine = init() #Idk if engine is thread safe
    try:
      remove(f"file{val}.mp3")
    except:
      pass
    engine.save_to_file(arg, f"file{val}.mp3")
    engine.runAndWait()
    #vc = await client.join_voice_channel(voice_channel)
    try:
      vc = await voice_channel.connect()
    except:
      remove(f"file{val}.mp3")
      return "Too overloaded - try again later"
    #player = vc.create_ffmpeg_player(f"file{val}.mp3", after = lambda: ctx.send(f"said {arg}"))
    vc.play(discord.FFmpegPCMAudio(f"file{val}.mp3"), after = lambda x: None)
    #player.start()
    while vc.is_playing():
      await sleep(1)
    vc.stop()
    await vc.disconnect()
    remove(f"file{val}.mp3")
  else:
    await ctx.send("User is not in a channel")
  
