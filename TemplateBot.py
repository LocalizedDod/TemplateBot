# Imports

from discord.ext import commands
import discord
import ctypes # Use this if your using python on windows , If on a web delete it. Or just disable it by adding a # next to it

# Normal

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all()) # This is the prefix of the bot, Change to the prefix you want!

@bot.event
async def on_ready(): # When the bot is ready, And running. It will put the status and the console title!
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('TemplateBot')) # This is the status of the bot, Change it to something you want!
    ctypes.windll.kernel32.SetConsoleTitleW("Template Bot || 0V4Team") # Use this if your using python on windows (Console), If on a web delete it. Or just disable it by adding a # next to it 
# Up there, You can see "Status.idle". You could always change it into online or do not disturb! 


bot.remove_command('help') # This disables the normal help command, So the embed help command works! If your gonna make another bot, make sure to always put the remove command('help') above the help embed command (custom)

# Commands 

# HelpCommand, So people know all of the commands!
@bot.command()
async def help(ctx):
    plan = discord.Embed(title="Help || Prefix : .",
        color=0x0000FF) 
    plan.add_field(name="Commands:", value="< YOUR COMMANDS > | v?example | v?credits", inline=False)
    await ctx.send(embed=plan)


#ExampleCommand
@bot.command()
async def example(ctx):
    plan = discord.Embed(title="Example",
        color=0x0000FF) 
    plan.add_field(name="Example", value="Hey! This is an example.", inline=False) 
    await ctx.send(embed=plan)


@bot.command()
async def credits(ctx):
    plan = discord.Embed(title="Credits",
        color=0x0000FF)
    plan.add_field(name="Credits:", value="D0V4 | https://discord.gg/G9cEmhtepc", inline=False) # You can remove the credits, Or keep it. Thanks :))
    await ctx.send(embed=plan)

token   = 'ENTER_YOUR_TOKEN_HERE' # Get your bots token from: https://discord.com/developers! Make sure to enable all intents, Also. Whenever you enable them and save, The bot will need a new token. so reset it!
# Intents that should be enabled: PRESENCE INTENT | SERVER MEMBERS INTENT | MESSAGE CONTENT INTENT
bot.run(token) # Runs the token above!

# This is a template for bot developing beginners, Coded by D0V4 (0V4Team) https://discord.gg/G9cEmhtepc
# You can either just remove the credits command, Replace me with yourself or keep it and add yourself! I would be very thankful.
# If your using desktop / visual studio code to code this or any other application, Open command prompt and do these commands so it works when you run it:
# pip install ctypes
# pip install discord
# pip install discord.ext


# Alot of people / my friends are struggling to make a bot, So heres a template! 
# Have fun!

# D0V4 | 0V4 Team | https://discord.gg/G9cEmhtepc
# Fully Coded By D0V4. 
# DM me or any of the other devs if you have an error. 















































