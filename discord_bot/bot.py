import discord
import dotenv
import os
import requests

dotenv.load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print("{} has connected to Discord!".format(client.user), flush=True)

@client.event
async def on_message(message):
    if(message.author == client.user): # Don't respond to the bot's own messages
        return

    elif("get weather" in message.content):
        await displayWeather("localhost", message.channel) # TODO: When we have more Pi's running with their ips in a database, get ip from database
    elif("set weather" in message.content):
        await message.channel.send("I can't control the weather (yet)")

PASCALS_TO_ATM = 101325

async def displayWeather(ip, channel):
    weather = requests.get("http://{}/api/weather".format(ip)).json()
    print("Weather:", weather)

    embed = discord.Embed(title="Weather", color=0x87CEEB)
    if(weather["pressure"] is not None):
        embed.add_field(name="Pressure", value="{} atm".format(weather["pressure"]/PASCALS_TO_ATM), inline=True)
    if(weather["light"] is not None):
        embed.add_field(name="Light", value="{}Lux".format(weather["light"]), inline=True)
    if(weather["humidity"] is not None):
        embed.add_field(name="Humidity", value="{}%".format(weather["humidity"]), inline=True)
    if(weather["ir_temp"] is not None):
        embed.add_field(name="IR Temperature", value="{}°C".format(weather["ir_temp"]), inline=True)
    if(weather["bar_temp"] is not None):
        embed.add_field(name="Barometer Temperature", value="{}°C".format(weather["bar_temp"]), inline=True)

    await channel.send(embed=embed)

client.run(token)
