import json
import os


def get_user_list(config, key):
    with open("{}/zerotwobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    LOGGER_LEVEL= 1
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 6  # integer value, dont use ""
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
    TOKEN = "5212174041:AAGbPP_gU-Ysb6zpaoQFPKJABLnGNAwIN4g"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5001573230  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "itzzz_axel"
    SUPPORT_CHAT = "Vexana_Support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001744920557
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001744920557
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://phfzgnhf:4EvWx06j7lDtf7uCEnEBfDHIaJqBct2v@batyr.db.elephantsql.com/phfzgnhf"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ALLOW_CHATS = True

    TEMP_DOWNLOAD_LOC = "./Downloads"

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
