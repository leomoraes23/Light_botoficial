import discord
import os
import asyncio
from random import randint

client = discord.Client()
imagem = 'livre'
respostas_do_sabio = ['Sim', 'Não', 'Talvez', 'Nunca', 'Claro', 'Quem sabe']


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
    print("BOT iniciado com!")
    await client.change_presence(
        game=discord.Game(name="Sou o BOT oficial do TL", url='https://twitch.tv/The_Light', type=1))


@client.event
async def on_member_join(member):
    chat_bem_vindo = discord.utils.get(member.server.channels, id='459773727371034624', type=discord.ChannelType.text)
    mencao_regras = discord.utils.get(member.server.channels, id='453707909570887680', type=discord.ChannelType.text)
    mencao_registro = discord.utils.get(member.server.channels, id='453680427975311361', type=discord.ChannelType.text)
    await client.send_message(chat_bem_vindo,
                              "{} *Bem vindo(a) ao servidor* __**The Light**__. *Leia as {} e registre-se no canal: {} :tada::hugging:*".format(
                                  member.mention, mencao_regras.mention, mencao_registro.mention))


@client.event
async def on_message(message):
    if message.content.lower().startswith('tl!sabio'):
        asyncio.sleep(0.1)
        await client.delete_message(message)

        ########## Variáveis do escopo ##################
        args = message.content.split(" ")
        resposta = respostas_do_sabio[randint(0, 5)]
        try:
            args[1] == True
            pergunta = ' '.join(args[1:])
        except IndexError:
            await client.send_message(message.channel, '*`Você deve adicionar a pergunta para o sábio responder :)`*')
            return

        embed = discord.Embed(color=0x0000FF)
        embed.add_field(name="Pergunta:", value='*`{}`*'.format(pergunta), inline=False)
        embed.add_field(name="Resposta:", value='*`{}`*'.format(resposta), inline=False)
        embed.set_author(name='Sábio Cagão')
        embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/2446938191/12wbg640n01k6mottrn9_400x400.jpeg')
        embed.set_footer(text="Quer perguntar pra mim? !sabio PERGUNTA", icon_url=message.server.icon_url)
        await client.send_message(message.channel, embed=embed)
        return

        if message.content.lower().startswith('!sabio'):
            asyncio.sleep(0.1)
        await client.delete_message(message)

        ########## Variáveis do escopo ##################
        args = message.content.split(" ")
        resposta = respostas_do_sabio[randint(0, 5)]
        try:
            args[1] == True
            pergunta = ' '.join(args[1:])
        except IndexError:
            await client.send_message(message.channel, '*`Você deve adicionar a pergunta para o sábio responder :)`*')
            return

        embed = discord.Embed(color=0x0000FF)
        embed.add_field(name="Pergunta:", value='*{}*'.format(pergunta), inline=False)
        embed.add_field(name="Resposta:", value='*`{}`*'.format(resposta), inline=False)
        embed.set_author(name='Sábio Cagão')
        embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/2446938191/12wbg640n01k6mottrn9_400x400.jpeg')
        embed.set_footer(text="Quer perguntar pra mim? !sabio PERGUNTA", icon_url=message.server.icon_url)
        await client.send_message(message.channel, embed=embed)
        return

    if message.content.startswith('Deo'):
        await client.send_message(message.channel,
                                  "<@468957271716790273> é um gostoso pausudo que todo mundo ama.")
        return

    if message.content.lower().startswith('!msg'):
        await asyncio.sleep(0.1)
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
                embed = discord.Embed(description="**{}**\n".format(" ".join(args[1:])), color=0x000000)
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

        def check(arg_aviso):
            return arg_aviso.content

        await client.send_message(message.channel, '**Por favor, insira a mensagem (sem comandos)**')
        mensagem_box = await client.wait_for_message(timeout=120, author=message.author, check=check)
        mensagem = mensagem_box.content.strip(" ")
        try:
            mensagem == True
        except AttributeError:
            await client.send_message(message.channel, "Tempo de envio esgotado, refaça a operação.")
            imagem = 'livre'
            return

        role = discord.utils.get(message.server.roles, name=' '.join(args[1:]))
        await client.delete_message(mensagem_box)
        await client.send_message(message.channel, "**Mensagem enviada com sucesso!**")
        for server_member in list(message.server.members):
            if role in server_member.roles:
                try:
                    embed = discord.Embed(description='**{}**'.format(''.join(mensagem)), color=0x000000)
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
            await client.send_message(message.channel,
                                      '**Cor invalida. Disponíveis: vermelho, verde, amarelo, azul, preto, branco e rosa.**')
            return

        await client.send_message(message.channel, "**Digite o aviso a seguir (sem o comando).**")

        def check(msg):
            return msg.content

        message = await client.wait_for_message(author=message.author, check=check)
        await client.delete_message(message)
        aviso = message.content.strip()
        embed = discord.Embed(title='📌 __Aviso da STAFF__', description='```diff\n- {}\n```'.format(aviso, aviso),
                              color=(color))
        embed.set_footer(text='Enviado por: {} {}'.format(message.author.name, '|' * 155))
        await client.send_message(message.channel, "@everyone")
        await client.send_message(message.channel, embed=embed)


client.run(str(os.environ.get('TOKEN')))
