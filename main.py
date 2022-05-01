import ffmpeg
import nextcord as discord
from nextcord.ext import commands
from tint import img_tint_main
from help_func import help_func
from echo import echo
from voice import say
from scramble import scramble
from io import BytesIO
bot = commands.Bot(command_prefix="\\")
version = "v0.3.2"

async def returnError(ctx, e):
    #e = e.args
    errType = type(e).__name__
    errReason = str(e)
    errEmbed = discord.Embed(
            title=f"HTHS Class of 2025 Discord Bot {version}",
            description=f"""An error occured when running the command.
Error Type: `{errType}`
Error Details: `{errReason}`""",
            color=0xAA0000)
    await ctx.send(embed=errEmbed)

async def returnWait(ctx, e):
    #e = e.args
    #errType = type(e).__name__
    errReason = str(e)
    errEmbed = discord.Embed(
            title=f"HTHS Class of 2025 Discord Bot {version}",
            description=errReason+".",
            color=0xAA0000)
    await ctx.send(embed=errEmbed)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

bot.remove_command('help') # Removed default help command.

@bot.command(name="help")
async def help_command(ctx):
    try:
        await help_func(ctx)
    except Exception as e:
        await returnError(ctx, e)

@bot.command(name="echo")
@commands.cooldown(5, 60, commands.BucketType.channel)
async def echo_command(ctx, *, arg="There's nothing to echo!"):
    try:
        await echo(ctx, arg)
    except Exception as e:
        await returnError(ctx, e)
 
@bot.command(name="say")
@commands.cooldown(5, 60, commands.BucketType.user)
async def say_command(ctx, *, arg=" "):
    try:
        await ctx.voice_client.disconnect()
    except:
        pass # There is an error when we're already disconnected, but it doesn't matter.
    global bot
    try:
        result = await say(bot, ctx, arg)
        if result == "Too overloaded - try again later":
            await returnWait(ctx, "Guys why are you spamming me? I can't handle it :(")
    except Exception as e:
        await returnError(ctx, e)
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(
            title=f"HTHS Class of 2025 Discord Bot {version}",
            description="""Unknown command. Type \\help for a list of commands.""",
            color=0xAA0000)
        await ctx.send(embed=embed)
    elif isinstance(error, discord.ext.commands.CommandOnCooldown):
        await returnWait(ctx, error)
    else:
        embed = discord.Embed(
            title=f"HTHS Class of 2025 Discord Bot {version}",
            description=f"An error occured: `{str(error)}`",
            color=0xAA0000)
        await ctx.send(embed=embed)

@bot.command(name="tint", pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def tint(ctx, color: str, url: str):
    try:
        imag1 = await img_tint_main(ctx, color, url)
        if imag1 != "error":
            with BytesIO() as image_binary:
                            imag1.save(image_binary, 'PNG')
                            image_binary.seek(0)
                            await ctx.send(file=discord.File(fp=image_binary, filename='tinted_image.png'))   
    except Exception as e:
        await returnError(ctx, e)   

        
@bot.command(name="scramble")
@commands.cooldown(5, 60, commands.BucketType.channel)
async def scramble_main(ctx, *, arg=""):
    try:
      await scramble(ctx, arg)
    except Exception as e:
      await returnError(ctx, e)

@bot.command(name="leave") # this is to force quit in case of a bug
async def leave(ctx):
    try:
        await ctx.voice_client.disconnect()
    except Exception as e:
        await returnError(ctx, e)

bot.run('ODg3MDQzNzI2MTY0MjU4ODk2.YT-Z2A.vdvU_NLgDlVVyz7rBDhRcuA4Ep8') # This is the token for the TESTING version of this bot.
