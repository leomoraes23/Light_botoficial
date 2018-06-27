import discord
import os
import asyncio
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.lower().startswith('!tl'):
        if not message.author.server_permissions.administrator:
            await client.send_message(message.channel, "**Desculpe, você não tem permissão para este comando.**")
            return
        args = message.content.split(" ")
        for server_member in message.server.members:
            try:
                embed = discord.Embed(description="{}".join(args[1:]), color=0x000000)
                embed.set_author(name="Aviso:", icon_url='https://i.imgur.com/ZZG7158.png')
                embed.set_thumbnail(url=server_member.avatar_url)
                embed.set_footer(text = "The Light", icon_url = server_member.avatar_url)
                await client.send_message(server_member, embed=embed)
            except:
                pass

client.run(os.getenv("TOKEN"))
