import discord
import os
import asyncio

client = discord.Client()
imagem = 'livre'

@client.event
async def on_message(message):
    if message.content.lower().startswith('!msg'):
        args = message.content.split(" ")
        if not message.author.server_permissions.administrator:
            await client.send_message(message.channel, "**Desculpe, você não tem permissão para este comando.**")
            return
        try:
            args[1] == True
        except IndexError:
            await client.send_message(message.channel, '**Por favor, insira a mensagem.**')
            return
        await client.delete_message(message)
        await client.send_message(message.channel, ' '.join(args[1:]))
    
    
    if message.content.lower().startswith('!setar'):
        await client.delete_message(message)
        args = message.content.split(" ")
        if not message.author.server_permissions.administrator:
            await client.send_message(message.channel, "**Desculpe, você não tem permissão para este comando.**")
            return

        try:
            args[1] == True
        except IndexError:
            await client.send_message(message.channel, '**Por favor, insira o LINK DA IMAGEM.**')
            return
        global imagem
        imagem = ''.join(args[1])
        await client.send_message(message.channel, '**Imagem setada com sucesso.**')

    if message.content.lower().startswith('!tl'):
        await client.delete_message(message)
        args = message.content.split(" ")
        if not message.author.server_permissions.administrator:
            await client.send_message(message.channel, "**Desculpe, você não tem permissão para este comando.**")
            return
        if imagem == 'livre':
            await client.send_message(message.channel, "**Você deve setar a imagem do aviso antes de enviar.**")
            return

        try:
            args[1] == True
        except IndexError:
            await client.send_message(message.channel, '**Por favor, insira a mensagem antes de enviar.**')
            return
        for server_member in message.server.members:
            try:
                embed = discord.Embed(description="**{}\n\n:tickets: CONVITE**\nhttps://discord.gg/2JbNFfk".format(" ".join(args[1:])),color=0x000000)
                embed.set_footer(icon_url=client.user.avatar_url, text="The Light")
                embed.set_image(url=imagem)
                await client.send_message(server_member, embed=embed)
            except:
                pass
        imagem = 'livre'


client.run(os.getenv("TOKEN"))
