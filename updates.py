from browser import document
changes = {"09-12-2019 [BIG]":"""\
> Added a public exec command
> > Fixed a bug where newlines wouldn't actually go through
> > I heard about some issues with encoding but I can't verify that rn
> Fixed the aliases of the help command [again]
> Fixed very minor bugs with the simplify command
> Updated the graph command
> > The graph command now supports both-axis graphing [<span class="mono dark"> x^2+y^2=4 </span>]
> > It should now actually graph faster when using more equations
> > Uses a new pallette that overall looks nicer
> > Fixed a couple bugs
> > Now is higher resolution
> > Now has X and Y axes clearly marked
> > Now won't break when the vars are uppercase
> > Should actually parse faster and break less when doing so
> > Shouldn't break with <span class="mono dark"> x=... </span> or <span class="mono dark"> y=... </span>""",
           
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
> > [<span class="mono">x=y^2</span> and <span class="mono dark"> y=x^2 </span> are supported]
> > Support for xy functions [<span class="mono"> x^2+y^2=4 </span>] has not been added yet, I'm working on it tho""",
           
           "08-22-2019 [MASSIVE]":"""\
> Added an actually decent AI [<span class="mono dark">;]text hello</span>]
> Fixed a bug where "no" would register as a bool and break it 
> Fixed a bug where smart quotes [<span class="mono dark"> ‘’“” </span>] would register as a bool break it
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
> Updated the <span class="mono dark"> ;]inv </span> command to comply with new permission requirements
> Added this site link to the inv command""",
           
           "08-13-2019":"""\
> Updated the help command to be automatic documentation
> Updated the help command so you can now do <span class="mono dark"> ;]help {command name} </span>
> Added new interactive commands [cuddle, kiss, throw]
> Added music capabilities"""}

changelog = document.getElementById("changes")
for key in changes:
    date = document.createElement("DIV")
    text = document.createTextNode(key)
    date.class_name = "header"
    date.append(text)
    changelog.appendChild(date)
    
    changed = document.createElement("DIV")
    text = document.createTextNode("")
    changed.class_name = "content consect"
    changed.appendChild(text)
    changed.innerHTML = changes[key].replace('\n','<br>')
    changelog.appendChild(changed)
    
    
