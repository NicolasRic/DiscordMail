# DiscordMail
DiscordMail is a discord bot that acts as an SMTP server and relays the messages to discord users or channels.

## Quick Installation Guide
You will need the following to setup DiscordMail
- Python
- Pip

Once installed you can install DiscordMail's dependancies.
```
git clone https://github.com/NicolasRic/DiscordMail.git
cd DiscordMail
pip install discord.py
```

Next you will need to make your own configuration file. The easiest way to do this is just copy the example config.
```
cp example.config.py config.py
```
Open the config.py file and change smtpip to your ip, and discordAPIKey to the discord bot's API key. 

## Setup servers
To get emails forward to discord, you are going to need to change your SMTP server. You should change SMTP server IP and Port to your discord bots port.
The email you pick for sender doesnt matter. It will show up in the discord message but WONT change the destination.

### Direct message
If you want the bot to send you a direct message, your recipient email should be as fllows: user@userID.discord, where userID is your userID.
To find your user ID you can follow this https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-

### Message channel
If you want the bot to send a message to a channel, first you must invite the discord bot into your server, then you can use the !info command to find the channel ID. Once done you need to change your recipient email to channel@channelID.discord, where channelID is your channel ID.
