import discord
import logging
import threading
import asyncore
import asyncio

import mail
import config

# Main assignments
logging.basicConfig(level=logging.INFO)
intents = discord.Intents().all()
client = discord.Client(intents=intents)
smtp_server = mail.mailServer((config.smtpip, config.smtpport), None, decode_data=True)

# Discord bot events
@client.event
async def on_ready():
    logging.info("Discord bot ready!")

@client.event
async def on_message(message):
    if(message.content == '!info'):
        # Build embed with IDs
        embed=discord.Embed(title="Information!!", color=0x98ddca)
        embed.add_field(name="UserID", value=message.author.id, inline=False)
        embed.add_field(name="ServerID", value=message.guild.id, inline=True)
        embed.add_field(name="ChannelID", value=message.channel.id, inline=True)
        await message.channel.send(embed=embed)

async def sender():
    while True:
        if len(config.emails) >= 1:
            # Get the channel ID
            config.emails[0].id[0] = config.emails[0].id[0].replace('.', '@')
            toSplit = config.emails[0].id[0].split("@")

            if(toSplit[0] == 'channel'):
                ch = client.get_channel(int(toSplit[1]))

            if(toSplit[0] == 'user'):
                ch = client.get_user(int(toSplit[1]))
        
            # Only send message if user or channel is found
            if(ch != None):
                # Builds embed & send
                embed=discord.Embed(title="Mail", color=0xffd3b4)
                embed.add_field(name="From", value=config.emails[0].client, inline=False)
                embed.add_field(name="Contents", value=config.emails[0].data, inline=False)
                await ch.send(embed=embed)
                logging.info("Message send to %s with ID %s", toSplit[0], toSplit[1])
            else:
                logging.warning("Failed to find %s with ID %s", toSplit[0], toSplit[1])

            # Remove message from sender queue
            config.emails.pop(0)

        if len(config.emails) > 10:
            logging.warning("Email list has more than ten emails (%s)", len(config.emails))

        await asyncio.sleep(1)

# Start a mail thread to recieve mail
mailThread = threading.Thread(target=asyncore.loop, daemon=True)
mailThread.start()

client.loop.create_task(sender())
client.run(config.discordAPIKey)

