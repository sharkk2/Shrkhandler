import discord
import os

### BOT CONFIG ###
version = '1.0.0'
prefix = 's.'
mongouri = '' # MongoDB URI
connectDB = False # Enable mongodb connection
owner_ids = [1092548532180877415, 774894992728391710]
embedcolor = discord.Color.blurple()
embederrorcolor = discord.Color.red()
name = ''
token = ''
client_id = 1328005965844316211
log_channel = 1296812933455810591

### ENV CONFIG ###
directory = os.path.join(os.path.dirname(__file__), "commands")
edirectory = os.path.join(os.path.dirname(__file__), "core/events")
tdirectory = os.path.join(os.path.dirname(__file__), "core/loops")
folder_blacklist = [
    "views",
    "functions",

]
file_blacklist = [
    'registry.py',
    '__init__.py'
]

### LOGGING ###
maintainance = False
INFO_COLOR = "blue"
ERROR_COLOR = "red"
DEBUG_COLOR = "green"
WARNING_COLOR = "peach"
FATAL_COLOR = "purple"

# EMOJIS
no = "<:no:1296811045444255755>"
error = "<:no:1296811045444255755>"
tick = "<:tick:1296811053119705118>"
yes = "<:tick:1296811053119705118>"
right = "<:right:1296811051488378930>"
left = "<:left:1296811043531784323>"
reply = "<:reply:1296811047419904091>"
replycont = "<:replycont:1296811049323860020>"
chat = "<:chat:1328091510784393356>"


# STATUS LOOPER
statuses = [
    {"text": "Youtube", "type": "idle", "activity": "watching", "url": ""},
    {"text": "Minecraft", "type": "dnd", "activity": "playing", "url": ""},
    {"text": "Orders", "type": "online", "activity": "listening", "url": ""},
]

