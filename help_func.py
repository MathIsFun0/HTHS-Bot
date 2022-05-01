import nextcord as discord
async def help_func(ctx):
      embed = discord.Embed(
            title="HTHS Class of 2025 Discord Bot v0.3.2",
            description="""Commands:
\\echo **message** - echoes message
\\help - displays this help message
\\leave - Leaves your voice channel
\\say **message** – Says message in your voice channel
\\scramble **message** – scrambles message
\\tint **hexcolor** **imageurl** - tints image by a color (*Must be URL!*)""",
            color=0xAA0000)
      await ctx.send(embed=embed)
