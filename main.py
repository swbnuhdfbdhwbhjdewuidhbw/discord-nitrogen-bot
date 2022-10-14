# kunai
# swev#9999/psn#0001 and over#0002

import discord
import random
import string
import os
from discord.ext import commands

client = commands.Bot(
  command_prefix=".",
  auto_reconnect=True
)

@client.event
async def on_ready():
  print("run ma 1s skiddo")

@client.command()
async def nitro(ctx, amount: int=1):
  if amount > 30:
    embed=discord.Embed(title="roses", description="max amount is 30", color=0xe30d0d)
    embed.set_author(name="roses", url="https://discord.gg/43vntTb2tj", icon_url="https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/988f7d447e36ddd6c289801d2387e740~c5_100x100.jpeg?x-expires=1655956800&x-signature=%2FWHW%2F29a3ViX15jhanzAdH7OMqE%3D")
    embed.set_footer(text="classic nitro")
    await ctx.reply(embed=embed)
    return
  if amount == 0:
    embed=discord.Embed(title="roses", description="0 is an invalid amount", color=0xe30d0d)
    embed.set_author(name="roses", url="https://discord.gg/43vntTb2tj", icon_url="https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/988f7d447e36ddd6c289801d2387e740~c5_100x100.jpeg?x-expires=1655956800&x-signature=%2FWHW%2F29a3ViX15jhanzAdH7OMqE%3D")
    embed.set_footer(text="classic nitro")
    await ctx.reply(embed=embed)
    return
  codes = []
  for code in range(amount):
    codes.append("https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16)))
  embed=discord.Embed(title="classic nitro", description="sending codes to your dms...", color=0xe30d0d)
  embed.set_author(name="roses", url="https://discord.gg/43vntTb2tj", icon_url="https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/988f7d447e36ddd6c289801d2387e740~c5_100x100.jpeg?x-expires=1655956800&x-signature=%2FWHW%2F29a3ViX15jhanzAdH7OMqE%3D")
  c = await ctx.reply(embed=embed)
  text = "```\n"
  for code in codes:
    text += code + "\n"
  text += "```"
  embed=discord.Embed(title="classic nitro", description=text, color=0xe30d0d)
  embed.set_author(name="roses", url="https://discord.gg/43vntTb2tj", icon_url="https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/988f7d447e36ddd6c289801d2387e740~c5_100x100.jpeg?x-expires=1655956800&x-signature=%2FWHW%2F29a3ViX15jhanzAdH7OMqE%3D")
  await ctx.author.send(embed=embed)
  embed=discord.Embed(title="classic nitro", description="sent codes to your dms", color=0xe30d0d)
  embed.set_author(name="roses", url="https://discord.gg/43vntTb2tj", icon_url="https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/988f7d447e36ddd6c289801d2387e740~c5_100x100.jpeg?x-expires=1655956800&x-signature=%2FWHW%2F29a3ViX15jhanzAdH7OMqE%3D")
  await c.edit(embed=embed)

  
client.run(os.environ['token'])
