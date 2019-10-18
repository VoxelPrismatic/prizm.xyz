from browser import document as doc, html
from md_4 import mark
content = {"DEVS ;]_devs": "PRIZ ;]#9244 - Literally does everything with the bot",
          "UPTIME_uptime": """\
Hopefully 24hrs with minor downtime. There may be moments of downtime of up to 1 second. \
This is normal because this bot is under development.
In case of longer downtimes [~ a day], that means the bot decided to kill itself \
and I am not there to turn it back on UwU""",
          "WHAT IT RUNS ON_cpu": """\
This bot runs on a laptop about 5 years old, an HP ProBook. \
I love it greatly, and it sacrificed its OS and time just to run this bot. \
It actually runs pretty well for 8GB of RAM, 2GB of SWAP [Virtual Ram], a 2.5GHz processor, and no dedicated GPU\
[it's stable at 2.9GHz which is very surprising for a 5 year old laptop in general]""",
          "ASCIIMOJI AND CUSTOM EMOJI_asciimoji": """\
I made all of these by myself, fyi 
Too find many cool faces that the bot uses, please visit this [link]<https://discord.gg/NHqbnyc> ;]
If you have Discord Nitro and want to use the sick ASCIImoji this bot comes with, please visit the \
[emoji server]<https://discord.gg/eYMyfcd> ;]""",
          "WTF IS THAT LOGO?_logo":"""\
That logo is something that I made quite a while ago, except that version was much worse. \
This is iteration 3, with shiny colors and more glow. It should be a prism of light, \
except it actually looks more like the Minecraft Prismarine shard, \
~which was definitely not what I was trying to improve in any way, shape or form~""",
          "WHO EVEN ARE YOU?_whoami":"""\
Absolutely nobody. I don't exist and I never made anything.
I'm an enthusiast, a programmer, and also non existent.
I'm confused and don't know what to do, but this seems cool, so I'll continue doing it.
Please keep in mind that I have no idea what I'm actually doing, so bugs will occur.""",
          "WHY IS THIS SITE LAGGY?_lah":"""\
Actually, it's because I don't know how to web design. I just asked for opinions, and you can always submit \
your feedback over at [this link]<https://github.com/VoxelPrismatic/prizm.xyz/issues/new> ;]""",
          "WHEN ARE YOU WORKING ON IT?_work":"""\
Alsmost always... I love working on it. Many changes and bug fixes are made every day"""}

element = doc["about"]

for key in content:
    element <= html.DIV(key.split("_")[0], Class="header", Id=key.split("_")[1])
    element <= html.DIV(mark(content[key]), Class="content consect")
