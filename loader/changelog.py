from browser import document as doc, html
from priz_md import mark
content = {"10x13_2019":"""\
> The >!;]reddit!< command has been updated
> > Now properly states whether or not the post is archived
> > Now states whether or not the >![IMAGE]!< button should be pressed
""",
           "10x11_2019":"""\
> The >!;]reddit!< command has been updated
> > Now looks much cleaner
> > Attributes---
> > > >![-] !< - Archived
> > > >!O-O !< - Link submission
> > > >!TXT !< - Text submission
> > > >! => !< - Edited
> > > >![&#x3e;- !< - Pinned
> > > >![&#x7c;&#x7c;]!< - Spoiled
> > Now supports multireddits
> > Now loads so much faster
> > Direct links now work
""",
           "10x08_2019":"""\
> The >!;]graph!< command has new features
> > Adding >!--zero!< to the end of the equation now shows the true zeros
> > Adding >!--yint!< to the end will show the y-intercept
> > >!--max!<, >!--min!<, >!--zero!<, >!--yint!< will be shown next to the equation in the legend, \
and everything else should work as normal...
>#Please use the >!;]bug!< command if you experience any issues#<
""",
           "10x03_2019":"""\
> The >!;]quad!< command should work now...
> > Should load faster
> > Shouls give the >*right*< answer...

> Logging now >#should#< work
> > Logging works on my own server, so...
""",
           "10x02_2019":"""\
> Just realized, the logging features are broken again
> > All >!;]mng!< features should still be funtional though
""",
           "10x01_2019":"""\
> The >!;]graph!< command now actually works [mostly]
> > Fixed >!--max!< and >!--min!< to not show up with >![nan, nan]!<
> > Fixed >!--zero!< to actually show some zeros, except not the correct ones...
""",
           "09x29_2019":"""\
> The >!;]graph!< command now has been refreshed
> > The new syntax ] >!;]graph {?window} {eq1} | {eq2} | {eq3} | {eqX}!<
> > Adding >!--max!< to the end of the equation should give you the maximum coordinates shown
> > Adding >!--min!< to the end of the equation should give you the minimum coordinates shown
> > Adding >!--zero!< should give you the coordinates for when >!y = 0!<

> The >!;]sym!< command has been updated
> > Doing something like >!;]sym 2x^2!< shouldn't break it

> Added the >!;]sub!< command
> > Syntax ] >!;]sub {num} {eq}!<
> > Allows you to substitute {num} in for X in {eq}
> > Example ] >!;]sub 206 x^2+34!<

> The >!;]calc!< command now actually loads on startup
""",
           "09x23_2019":"""\
> The >!;]graph!< command now doesnt need xmin or xmax, but now also has options for ymin and ymax
> > >!;]graph x!< - ymin, ymax, xmin, xmax = -10, 10, -10, 10
> > >!;]graph -3 x!< - ymin, ymax, xmin, xmax = -10, 10, -3, 10
> > >!;]graph -3 3 x!< - ymin, ymax, xmin, xmax = -10, 10, -3, 3
> > >!;]graph -3 3 -5 x!< - ymin, ymax, xmin, xmax = -5, 10, -3, 3
> > >!;]graph -3 3 -5 5 x!< - ymin, ymax, xmin, xmax = -5, 5, -3, 3
""",
           "09x22_2019":"""\
> Logging now actually works

> You can now create, edit, delete, and view tags with no issues

> All >!;]mng!< features now work
""",
           "09x16_2019":"""\
> Fixed the >!;]mng!< command
> > The logging section now actually loads
> > The moderator section now doesn't throw an error
""",
           "09x15_2019":"""\
> Switched the database from >!JSON!< to >!SQLITE3!<

> > This is a pretty big change, please submit any and all bugs via the >!;]bug!< command or via DMs

> The >!;]audit!< command has been refreshed

> All commands have been updated to use the new database

> Removed the guild listener because it was useless

> Fixed several bugs
""",
           "09x12_2019":"""\
> Added a public exec command
> > Fixed a bug where newlines wouldn't actually go through
> > I heard about some issues with encoding but I can't verify that rn

> Fixed the aliases of the help command [again]

> Fixed very minor bugs with the simplify command

> Updated the graph command
> > The graph command now supports both-axis graphing [>!x^2+y^2=4!<]
> > It should now actually graph faster when using more equations
> > Uses a new pallette that overall looks nicer
> > Fixed a couple bugs
> > Now is higher resolution
> > Now has X and Y axes clearly marked
> > Now won't break when the vars are uppercase
> > Should actually parse faster and break less when doing so
> > Shouldn't break with >!x=...!< or >!y=...!<
""",
           
           "09x09_2019":"""\
> Added the simplify command

> Added more features to that command

> Fixed bugs with the help command
> > All aliases after the first one would have a >!.!< in front

> Added the calc command
> > Added more functions
> > Why did it take so long? I was trying to prevent injection, and I'm fairly certain I succeeded
""",
           
           "08x26_2019":"""\
> Cleaned up files and code to make it more readable

> Added help text for the clrin command

> Added the clrto command, it clears all messages to a given message ID
> > Useful if you don't know the exact amount of kessages to clear

> Updated the graph command so you can now graph on the y axis too 
> > [>!x=y^2!< and >!y=x^2!< are supported]
> > Support for xy functions [>!x^2+y^2=4!<] has not been added yet, I'm working on it tho
""",
           
           "08x22_2019":"""\
> Added an actually decent AI [>!;]text hello!<]

> Fixed a bug where "no" would register as a bool and break it 

> Fixed a bug where smart quotes [>!‘’“”!<] would register as a bool break it

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

> Fixed bugs and things
""",
           
           "08x20_2019":"""\
> Added the >!;]reddit!< command
> > Fixed some bugs with that

> Added the >!;]captcha!< command

> Added the >!;]8ball!< command
""",
           
           "08x19_2019":"""\
> Fixed the >!;]2048!< command
> > Now groups properly when not moving right
> > Now doesn't break when there are multiple instances
> > Doesn't edit twice
> > Now ends the game properly, whereas before it would end if it couldn't add any new tiles
""",
           
           "08x18_2019":"""\
> Added 2048
> > Fixed some bugs
> > Added to the help command

> Updated the help command to change the prefix in the page
> > Fixed bugs

> Updated the >!;]inv!< command to comply with new permission requirements
> Added this site link to the inv command
""",
           
           "08x13_2019":"""\
> Updated the help command to be automatic documentation

> Updated the help command so you can now do >!;]help {command name}!<

> Added new interactive commands [cuddle, kiss, throw]

> Added music capabilities""",
           "00x00_0000":"""\
> This bit here was lost in time...
> > Rest assured, the bot was being developed :D
""",
           "06x26_2019":"""\
> Added the >!embedify!< utility

> Moved module loading to a seperate file

> Removed some useless things
> > Like >!bot.lock = False!< which I literally never used

> Moved custom faces and texts into a different file

> Moved command re/un/loading to a different file

> Added a paginator
"""}

doc["labels"].innerHTML = '|'.join(list(content))
element = doc["changes"]
lists = doc["tabby"]

for key in content:
    lists <= html.BUTTON(key, Class = "tabby_link", Id = key)
    element <= html.DIV(mark(content[key])+"<br>", Class = "tabby_sect", Id = key+"-", style={"display": "none"})
