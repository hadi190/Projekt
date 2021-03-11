import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Finds data
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

# Starts discord client
client = commands.Bot(command_prefix=".")

# Gets the test channel TODO doesn't currently actually get the channel


@client.command(name="help_command")
async def help_command(context):
    current_channel = context.channel
    message = discord.Embed(title="Information samt kommandon för boten", description="", color=0x00ff00)
    message.add_field(name=".hjälp", value="Öppnar upp den här listan, här finner du all information du behöver!", inline=False)
    message.add_field(name=".glosor", value="Startar upp glosor programmet som hjälper dig träna på dina egna, självinlagda glosor.", inline=False)
    message.add_field(name=".avsluta", value="Stänger den aktiva glosor-träningen.", inline=False)
    message.add_field(name=".tips", value="Ger ett litet tips om du är fast på ett ord, kan användas flera gånger.", inline=False)
    message.add_field(name=".nästa", value="Skippar nuvarande ord och du tas till nästa.", inline=False)
    message.add_field(name=".växla", value="Byter till det andra språket.", inline=False)




    message.set_author(name="Skål Bot")

    await current_channel.send(embed=message)


channel = client.get_channel(819154008731811840)


@client.event
# Runs on bot startup
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    # Some test code for successfully running the bot
    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id}) \n"
        f"to the channel {channel}"
    )


# Starts everything and makes the magic happen
client.run("ODE5MTUzMzYyMzM4NTc4NDYz.YEieBA.QGAziKy4xGu1oUBD52lMWY-S5Cc")
