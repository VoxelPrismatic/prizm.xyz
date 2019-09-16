from browser import document
changes = {"09-16-2019":"""\
> Fixed the <code>;]mng</code> command
> > The logging section now actually loads
> > The moderator section now doesn't throw an error
""",
           "09-15-2019":"""\
> Switched the database from <code>JSON</code> to <code>SQLITE3</code>
> > This is a pretty big change, please submit any and all bugs via the <code>;]bug</code> command or via DMs
> The <code>;]audit</code> has been refreshed
> All commands have been updated to use the new database
> Removed the guild listener because it was useless
> Fixed several bugs
""",
           "09-12-2019 [BIG]":"""\
> Added a public exec command
> > Fixed a bug where newlines wouldn't actually go through
> > I heard about some issues with encoding but I can't verify that rn
> Fixed the aliases of the help command [again]
> Fixed very minor bugs with the simplify command
> Updated the graph command
> > The graph command now supports both-axis graphing [<code>x^2+y^2=4</code>]
> > It should now actually graph faster when using more equations
> > Uses a new pallette that overall looks nicer
> > Fixed a couple bugs
> > Now is higher resolution
> > Now has X and Y axes clearly marked
> > Now won't break when the vars are uppercase
> > Should actually parse faster and break less when doing so
> > Shouldn't break with <code>x=...</code> or <code>y=...</code>""",
           
           "09-09-2019":"""\
> Added the simplify command
> Added more features to that command
> Fixed bugs with the help command
> > All aliases after the first one would have a '.' in front
> Added the calc command
> > Added more functions
> ] Why did it take so long? I was trying to prevent injection, and I'm fairly certain I succeeded""",
           
           "08-26-2019":"""\
> Cleaned up files and code to make it more readable
> Added help text for the clrin command
> Added the clrto command, it clears all messages to a given message ID
> > Useful if you don't know the exact amount of kessages to clear
> Updated the graph command so you can now graph on the y axis too 
> > [<code>x=y^2</code> and <code>y=x^2</code> are supported]
> > Support for xy functions [<code>x^2+y^2=4</code>] has not been added yet, I'm working on it tho""",
           
           "08-22-2019 [MASSIVE]":"""\
> Added an actually decent AI [<code>;]text hello</code>]
> Fixed a bug where "no" would register as a bool and break it 
> Fixed a bug where smart quotes [<code>‘’“”</code>] would register as a bool break it
> Fixed a bug where any colons would register as a dict and break it
> Now responds before it re-analyses
> New logic will come soon, it currently only chooses the best response
> Removed old files
> Updated GitHub
> Removed old AIs because they were trash
> Updated main file to not be trash
> Cleaned up so much code it's not even funny
> Added docs to other things
> Added a learning command
> Updated more files
> Updated the inv command to be dynamic
> Working on a better audit command
> Fixed bugs and things""",
           
           "08-20-2019":"""\
> Added the reddit command
> Fixed some bugs with that
> Added the captcha command
> Added the 8ball command""",
           
           "08-19-2019":"""\
> Fixed the 2048 command
> > Now groups properly when not moving right
> > Now doesn't break when there are multiple instances
> > Doesn't edit twice
> > Now ends the game properly, whereas before it would end if it couldn't add any new tiles""",
           
           "08-18-2019":"""\
> Added 2048
> Fixed bugs with the 2048 command
> Added 2048 to the help command
> Updated the help command to change the prefix in the page
> Fixed bugs with the above
> Updated the <code>;]inv</code> command to comply with new permission requirements
> Added this site link to the inv command""",
           
           "08-13-2019":"""\
> Updated the help command to be automatic documentation
> Updated the help command so you can now do <code>;]help {command name}</code>
> Added new interactive commands [cuddle, kiss, throw]
> Added music capabilities"""}

abouts = {"DEVS ;]": "PRIZ ;]#9244 - Literally does everything with the bot",
          "UPTIME": """\
Hopefully 24hrs with minor downtime. There may be moments of downtime of up to 1 second. \
This is normal because this bot is under development.
In case of longer downtimes [~ a day], that means the bot decided to kill itself \
and I am not there to turn it back on UwU""",
          "WHAT IT RUNS ON": """
This bot runs on a laptop about 5 years old, an HP ProBook. \
I love it greatly, and it sacrificed its OS and time just to run this bot. \
It actually runs pretty well for 8GB of RAM, 2GB of SWAP [Virtual Ram], and a 2.5GHz processor \
[it's stable at 2.9GHz which is very surprising for a laptop of any sort]""",
          "ASCIIMOJI AND CUSTOM EMOJI": """
I made all of these by myself, fyi 
Too find many cool faces that the bot uses, please visit this <a href="https://discord.gg/NHqbnyc">link</a> ;]
If you have Discord Nitro and want to use the sick emoji this bot comes with, please visit the \
<a href="https://discord.gg/eYMyfcd">emoji server ;]</a>""",
          "WTF IS THAT LOGO?":"""\
That logo is something that I made quite a while ago, except that version was much worse. \
This is iteration 3, with shiny colors and more glow. It should be a prism of light, \
except it actually looks more like the Minecraft Prismarine shard, 
<s>which was definitely not what I was trying to improve in any way, shape or form</s>""",
          "WHO EVEN ARE YOU?":"""\
Absolutely nobody. I don't exist and I never made anything.
I'm an enthusiast, a programmer, and also non existent.
I'm confused and don't know what to do, but this seems cool, so I'll continue doing it.
Please keep in mind that I have no idea what I'm actually doing, so bugs will occur.""",
          "WHY IS THIS SITE LAGGY?":"""\
Actually, it's because I don't know how to web design. I just asked for opinions, and you can always submit \
your feedback over at <a href="https://github.com/VoxelPrismatic/prizm.xyz/issues/new">this link</a> ;]"""}

faq = {"OwO WHAT IS THIS?": "This is an empty FAQ because nobody asked any questions yet UwU"}

def addSect(content, element):
    for key in changes:
        title = document.createElement("DIV")
        text = document.createTextNode(key)
        title.class_name = "header"
        title.append(text)
        element.appendChild(title)
    
        stuff = document.createElement("DIV")
        text = document.createTextNode("")
        stuff.class_name = "content consect"
        stuff.appendChild(text)
        replace = {'\n':'<br>',
                   '<code>':'<span class="mono dark">',
                   '</code>':'</span>'}
        for re in replace:
            content[key] = content[key].replace(re, replace[re])
        stuff.innerHTML = changes[key]
        content.appendChild(stuff)
changelog = document.getElementById("changes")
aboutlog = document.getElementById("about")
faqs = document.getElementById("faq")
addSect(changes, changelog)
addSect(abouts, aboutlog)
addSect(faq, faqs)
