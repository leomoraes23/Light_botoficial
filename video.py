import discord
import os
import asyncio

client = discord.Client()
imagem = 'livre'

@client.event
async def on_ready():
    Nome_do_client = client.user.name
    ID_do_client = client.user.id
    print("Olá, eu sou um client e este é meu nome: %s, aqui vai meu ID: %s. " % (Nome_do_client, ID_do_client))
    print("Iniciando client.")
    print("Iniciando client...")
    print("Iniciando client.....")
    print("Iniciando client.......")
    print("Iniciando client.........")
    print("BOT iniciado com sucesso!")
    await client.change_presence(game=discord.Game(name="Não, comprando aparatos sexuais", type=4))


@client.event
async def on_member_join(member):
    chat_bem_vindo = discord.utils.get(member.server.channels, name='bate-papo', type=discord.ChannelType.text)
    await client.send_message(chat_bem_vindo, "**{} BEM VINDO AO SERVIDOR THE LIGHT, DIVIRTA-SE!.**".format(member.mention))
    

@client.event
async def on_message(message):
    if message.content.startswith('Deo'):
        await client.send_message(message.channel, "<@260157385870540803> é meu papai. ̶ ̶M̶a̶s̶ ̶e̶l̶e̶ ̶m̶e̶ ̶a̶b̶u̶s̶a̶ ̶a̶ ̶n̶o̶i̶t̶e̶ ̶;̶-̶;̶  TE AMO PAI <3")
        return
        
    if message.content.startswith('Luiz'):
        await client.send_message(message.channel, "<@417808137249095680> da o cú na botinha ksksksksksksks")
        return
    
    if message.content.lower().startswith('!msg'):
        await asyncio.sleep(0.5)
        await client.delete_message(message)
        args = message.content.split(" ")
        if not message.author.server_permissions.administrator:
            await client.send_message(message.channel, "**Desculpe, você não tem permissão para este comando.**")
            return
        try:
            args[1] == True
        except IndexError:
            await client.send_message(message.channel, '**Por favor, insira a mensagem.**')
            return
        
        ver_chat_musica = discord.utils.get(message.server.channels, name='✉chat-livre', type=discord.ChannelType.text)
        await client.send_message(ver_chat_musica, ' '.join(args[1:]))
    
    
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
