from browser import document as doc, html, window as win
from priz_md import mark
content = {"10x17_2019":"""\
> The >!;]draw!< command is now a thing!
> > Draw whatever you want in a 128x128 grid!
> > Will be upscaled to a 1024x1024 image when sending to prevent blurriness
>`#] HELP FOR DRAW [CATAGORY: fun]
=] Have fun drawing with others!
>  USAGE - ';]draw {?color} {?x1} {?y1} {?x2} {?y2} ... {?xN} {?yN}'
>  ALIAS - "paint", "color", "canvas", "painting", "drawing", "coloring"
COLOR  [STR] - The color you want to place, MUST BE HEX
xN, yN [ANY] - The XY coordinates [MAX - 127, MIN - 0]
             - You can use ranges like 0-16
             - You can be relative like ~1
             - You can use relative ranges like ~9-26
*If no params are passed, the image is sent
*If only coordinates are passed, the color at that coordinate is sent along with the image
*ALL relative points are relative to YOUR last point`<
""",
           "10x16_2019":"""\
> Added the >!;]draw!< command
> > Still working on it, and will be greatly improved tomorrow
""",
           "10x14_2019":"""\
> The char command now gives more info
> > When requesting one character, it tells you how to write it in many languages
> > > Includes PY, JS, URI/URL, JAVA, C#, C++, C, HTML, RUBY, and SWIFT
> > > If you want other languages, please visit the >$https://discordapp.com/channels/533290351184707584/535507316775059516/\
$$#prizm_suggest$< channel
""",
           "10x13_2019":"""\
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
> > > >!§ => !< - Edited
> > > >![>§- !< - Pinned
> > > >![|§|]!< - Spoiled
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
> > Fixed >!--zero!< to actually show some zeros, except not the cor
