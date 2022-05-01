async def echo(ctx, arg = ""):
    if arg.startswith("\\\\echo"):
        pass # If an achievement system is added, this could be an achievement for bypassing recursion and "breaking" the bot.
    if not arg.startswith("\\echo "):
        await ctx.send(arg)
    else:
        await ctx.send("Will not echo a recursive command")
