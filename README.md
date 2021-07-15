# AntiBots
Remove botted VoIPs and deleted accounts from your channel automatically

# Installation
This telegram bot is fully async and made using Pyrogram. The installation process may vary from device to device.

**1)** Install requred libraries
```sh
pip install pyrogram tgcrypto
```
_Pyrogram is required to make the bot work, since it's the library used to communicate with telegram_

**2)** Run the script

```sh
python3 antibots.py
```
_Run the script using python3 (can be also executed with ```sh python antibots.py``` )_

# Commands

**1)** Get a list of the latest 200 members of your channel
```sh
/start <ChannelID>
```  
**ARGS** | ChannelID - The ID of your channel, can be retrieved using @usinfobot [channelusername]

**2)** Remove botted members
```sh
/remove [1 or 2]
```  
**ARGS** | 1 or 2
   
   --> By using the number 1 you'll remove only the accounts considered as VoIPs (DC1, DC3, DC5)
   
   --> By using the number 2 you'll also remove deleted accounts, users without a profile picture and suspicious accounts (DC1, DC2, DC3, DC5, Deleted Accounts, Users without a propic)


# Important Notes

**Telegram has a limit for channels which allows you to retrieve only 200 MEMBERS each time you do the start command. If your channel has more than 200 members repeat the command when a removal is complete.**
