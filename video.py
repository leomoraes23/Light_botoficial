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
    await client.change_presence(
        game=discord.Game(name="minhas experiências na cama.", url='https://twitch.tv/The_Light', type=1))


@client.event
async def on_member_join(member):
    chat_bem_vindo = discord.utils.get(member.server.channels, name='✉chat-livre', type=discord.ChannelType.text)
    mencao_regras = discord.utils.get(member.server.channels, name='📵regras', type=discord.ChannelType.text)
    mencao_registro = discord.utils.get(member.server.channels, name='registre-se📕', type=discord.ChannelType.text)
    await client.send_message(chat_bem_vindo,"{} *Bem vindo(a) ao servidor* __**The Light**__. *Leia as {} e registre-se no canal: {} :tada::hugging:*".format(member.mention, mencao_regras.mention, mencao_registro.mention))


@client.event
async def on_message(message):
    if message.content.startswith('Deo'):
        await client.send_message(message.channel,"<@260157385870540803> é meu papai. ̶ ̶M̶a̶s̶ ̶e̶l̶e̶ ̶m̶e̶ ̶a̶b̶u̶s̶a̶ ̶a̶ ̶n̶o̶i̶t̶e̶ ̶;̶-̶;̶  TE AMO PAI <3")
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
        for server_member in list(message.server.members):
            try:
                embed = discord.Embed(description="**{}**\n".format(" ".join(args[1:])),color=0x000000)
                embed.set_footer(icon_url=client.user.avatar_url, text="The Light")
                embed.set_image(url=imagem)
                await client.send_message(server_member, embed=embed)
            except:
                pass
        imagem = 'livre'

    if message.content.lower().startswith('!staff'):
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
            await client.send_message(message.channel, '**Por favor, insira o cargo antes de enviar.**')
            return
        try:
            args[2] == True
        except IndexError:
            await client.send_message(message.channel, '**Por favor, insira a mensagem antes de enviar.**')
            return

        role = discord.utils.get(message.server.roles, name=args[1])
        for server_member in list(message.server.members):
            if role in server_member.roles:
                try:
                    embed = discord.Embed(description="**{}**\n".format(" ".join(args[2:])), color=0x000000)
                    embed.set_footer(icon_url=client.user.avatar_url, text="The Light")
                    embed.set_image(url=imagem)
                    await client.send_message(server_member, embed=embed)
                except:
                    pass
            imagem = 'livre'

    if message.content.lower().startswith('!aviso'):
        await client.delete_message(
            message)  # Comando que deleta a mensagem original do usuário (sómente a mensagem contendo o comando)

        if not message.author.server_permissions.administrator:
            await client.send_message(message.channel, '**Desculpe, você não possui acesso a este comando.**')
            return

        args = message.content.split(" ")
        try:
            args[1] == True
        except IndexError:
            await client.send_message(message.channel, '**Por favor, insira a cor do aviso.**')
            return
        color = None
        if (args[1].lower() == 'vermelho'):
            color = discord.Colour(0xFF0000)

        elif (args[1].lower() == 'verde'):
            color = discord.Colour(0x00FF00)

        elif (args[1].lower() == 'amarelo'):
            color = discord.Colour(0xFFFF00)

        elif (args[1].lower() == 'azul'):
            color = discord.Colour(0x0000FF)

        elif (args[1].lower() == 'preto'):
            color = discord.Colour(0x000000)

        elif (args[1].lower() == 'branco'):
            color = discord.Colour(0xFFFFFF)

        elif (args[1].lower() == 'rosa'):
            color = discord.Colour(0xFF1493)

        if color is None:
            await client.send_message(message.channel,'**Cor invalida. Disponíveis: vermelho, verde, amarelo, azul, preto, branco e rosa.**')
            return

        await client.send_message(message.channel, "**Digite o aviso a seguir (sem o comando).**")

        def check(msg):
            return msg.content

        message = await client.wait_for_message(author=message.author, check=check)
        await client.delete_message(message)
        aviso = message.content.strip()
        embed = discord.Embed(title='📌 __Aviso da STAFF__', description='```diff\n- {}\n```'.format(aviso, aviso),color=(color))
        embed.set_footer(text='Enviado por: {} {}'.format(message.author.name, '|' * 155))
        await client.send_message(message.channel, "@everyone")
        await client.send_message(message.channel, embed=embed)

client.run(str(os.environ.get('TOKEN')))
