async def scramble(ctx, arg):
  from random import shuffle
  if arg == "":
    await ctx.send("Why are you guys all trying to find bugs? :(")
    return
  l = list(arg)
  shuffle(l)
  await ctx.send("".join(l))
