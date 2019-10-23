from browser import document as doc, html, window as win
from priz_md import mark
coms = {
    "rick": {
        "brf": "Never gonna give you up!",
        "usg": ";]rick",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "fun"
    }, "learn": {
        "brf": "You can help me learn!",
        "usg": ";]learn {?text}",
        "dsc": "TEXT [STR] - OPTIONAL: Preset conversation, new message on new line",
        "als": [],
        "cat": "ai"
    }, "info": {
        "brf": "Shows aditional bot info",
        "usg": ";]info",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "inf"
    }, "role": {
        "brf": "Adds or removes {role} from {user} for a {reason}",
        "usg": ";]role {mbr} {add/remove} {rol} {?rsn}",
        "dsc": """\
MBR [MEMBER] - The target user, mention or name or ID
ROL [ROLE  ] - The target role, mention or name or ID
RSN [STR   ] - The reason for the action DEFAULT: \"REQUESTED BY ] <name>\"
""",
        "als": [],
        "cat": "mod"
    }, "text": {
        "brf": "You can have a conversation with me!",
        "usg": ";]text {convo}",
        "dsc": "CONVO [STR] - The conversation",
        "als": [ "ai", "chat", "" ],
        "cat": "ai"
    }, "binary": {
        "brf": "Converts binary to text, and text to binary",
        "usg": ";]binary {st}",
        "dsc": "ST [STR] - The stuff to convert to/from binary",
        "als": [],
        "cat": "fun"
    }, "slap": {
        "brf": "Slaps a {member} for a {reason}!",
        "usg": ";]slap {mbr} {?reason}",
        "dsc": """\
MBR    [INT or PING] - The member you want to slap
REASON [STR        ] - The reason for the slap
""",
        "als": [],
        "cat": "int"
    }, "slots": {
        "brf": "Virtual Slot Machine",
        "usg": ";]slots",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "fun"
    }, "_2048": {
        "brf": "2048 but in Discord",
        "usg": ";]2048 {?size}",
        "dsc": "SIZE [INT] - The size [is square] DEFAULT: 4",
        "als": [ "2048" ],
        "cat": "fun"
    }, "factor": {
        "brf": "Finds the factors and prime factors of {num}",
        "usg": ";]factor {num}",
        "dsc": "NUM [INT] - The number to find the factors of",
        "als": [ "fct" ],
        "cat": "math"
    }, "simple": {
        "brf": "Symplify complex equations",
        "usg": ";]simplify {eq}",
        "dsc": "EQ [STR] - The equation to simplify",
        "als": [ "simp", "simplify", "sym" ],
        "cat": "math"
    }, "captcha": {
        "brf": "Are you a bot?",
        "usg": ";]captcha {mbr}",
        "dsc": "MBR [MEMBER] A member, ping or name or ID",
        "als": [],
        "cat": "fun"
    }, "vox": {
        "brf": "Phoentically spells words",
        "usg": ";]vox {text}",
        "dsc": "TEXT [STR] - The text",
        "als": [],
        "cat": "fun"
    }, "coin": {
        "brf": "Flips a virtual coin {x} times!",
        "usg": ";]coin {?num}",
        "dsc": "NUM [INT] - How many times the coin should be flipped",
        "als": [],
        "cat": "fun"
    }, "rad": {
        "brf": "Radical Reducers",
        "usg": ";]rad {D} {X}",
        "dsc": """\
D [INT] - Discriminator, aka X\u221a>>D<<
X [INT] - The radical, aka \"square root\" is 2 and \"cube root\" is 3
""",
        "als": [ "reduce", "radical" ],
        "cat": "math"
    }, "react": {
        "brf": "Adds reactions quickly and easily",
        "usg": ";]react {mID} {rct1} {rct2} {...}",
        "dsc": "mID  [INT] - The message\nRCTx [ANY] - The reaction[s]",
        "als": [],
        "cat": "fun"
    }, "hug": {
        "brf": "Hugs a {member} for a {reason}!",
        "usg": ";]hug {mbr} {?reason}",
        "dsc": """\
MBR    [INT or PING] - The Member you want to hug
REASON [STR        ] - The reason for the hug
""",
        "als": [],
        "cat": "int"
    }, "rpn": {
        "brf": "Reverse Polish Notation [1 1 +]",
        "usg": ";]rpn {eq}",
        "dsc": "EQ [STR] - The RPN equation",
        "als": [],
        "cat": "math"
    }, "djq": {
        "brf": "In rememberance of DJ Quzingler [BOT]",
        "usg": ";]djq",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "fun"
    }, "factorial": {
        "brf": "Factorial!",
        "usg": ";]factorial {num}",
        "dsc": "NUM [INT] - The thing to factorialize",
        "als": [ "fact" ],
        "cat": "math"
    }, "hlep": {
        "brf": "Brings up this message",
        "usg": ";]help {?com}",
        "dsc": "COM [command] - OPTIONAL: Brings up a help message for that specific command",
        "als": [ "help" ],
        "cat": "inf"
    }, "cuddle": {
        "brf": "Cuddle with a {member} for a {reason}!",
        "usg": ";]cuddle {mbr} {?reason}",
        "dsc": """\
MBR    [INT or PING] - The member you want to cuddle
REASON [STR        ] - The reason for the cuddle
""",
        "als": [],
        "cat": "int"
    }, "char": {
        "brf": "Shows unicode info on {char}",
        "usg": ";]char {chars}",
        "dsc": "CHARS [STR] - The characters you want data on",
        "als": [],
        "cat": "oth"
    }, "asci": {
        "brf": "Just prints one of these cool ASCIImoji!",
        "usg": ";]asci",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "fun"
    }, "ball8": {
        "brf": "I definitely predict the future",
        "usg": ";]8ball {question}",
        "dsc": "QUESTION [STR] What do you want me to answer",
        "als": [ "8b", "8bl", "8ball" ],
        "cat": "fun"
    }, "data": {
        "brf": "Shows the data usage",
        "usg": ";]data",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "inf"
    }, "draw": {
        "brf": "Have fun drawing with others!",
        "usg": ";]draw {?color} {?x1} {?y1} {?x2} {?y2} ... {?xN} {?yN}",
        "dsc": """\
COLOR  [STR] - The color you want to place, MUST BE HEX
xN, yN [ANY] - The XY coordinates [MAX - 127, MIN - 0]
- - You can use ranges like 0-16
- - You can be relative like ~1
- - You can use relative ranges like ~9-26
*If no params are passed, the image is sent
*If only coordinates are passed, the color at that coordinate is sent along with the image
*ALL relative points are relative to YOUR last point
""",
        "als": [ "paint", "color", "canvas", "painting", "drawing", "coloring" ],
        "cat": "fun"
    }, "substitute": {
        "brf": "Substitutes a number in for X",
        "usg": ";]substitute {num} {eq}",
        "dsc": "NUM [FLOAT] - The thing X is equal to\nEQ  [STR  ] - The equation to solve",
        "als": [ "sub" ],
        "cat": "math"
    }, "optn": {
        "brf": "I choose something for you!",
        "usg": ";]choose {arg1} \"{multi word arg2}\" {...}",
        "dsc": "ARGx [STR] - The choice itself",
        "als": [ "choose" ],
        "cat": "fun"
    }, "throw": {
        "brf": "Throws a {member} for a {reason}!",
        "usg": ";]throw {mbr} {?reason}",
        "dsc": """\
MBR    [INT or PING] - The member you want to throw
REASON [STR        ] - The reason for the throw
""",
        "als": [],
        "cat": "int"
    }, "mng": {
        "brf": "Brings up a management interface",
        "usg": ";]mng",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [ "manage", "tor" ],
        "cat": "mod"
    }, "blkjck": {
        "brf": "Virtual Black Jack",
        "usg": ";]blkjck",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [ "blackjack", "bj" ],
        "cat": "fun"
    }, "play": {
        "brf": "Plays Music",
        "usg": ";]play {vc} {link}",
        "dsc": """
LINK [STR] - Link to some file, youtube video, or is a youtube search
- - YOUTUBE SEARCH---
- - > SYNTAX: \";]play {vc} yt-{search}\"
- - > SEARCH RESULT: append \"-i={search result number}\"
- - § to get that result playing
VC   [VC ] - The VC I should join
""",
        "als": [],
        "cat": "music"
    }, "hlepmod": {
        "brf": "Brings up the mod help message",
        "usg": ";]helpmod",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [ "helpmod", "modhelp", "modhlep" ],
        "cat": "inf"
    }, "code": {
        "brf": "A public exec command to test your code!",
        "usg": ";]code {lang} {code}",
        "dsc": """\
LANG [STR] - The language to use
- - 'js' for JavaScript
- - 'py' for Python
- - 'tr' for Boolean Logic
CODE [STR] - The code to execute
""",
        "als": [ "exec" ],
        "cat": "oth"
    }, "quad": {
        "brf": "Solves the quadratic formula",
        "usg": ";]quad {A} {B} {C}",
        "dsc": "A, B, C [FLOATS] - Corrosponds to \"Ax^2 + Bx + C\"",
        "als": [],
        "cat": "math"
    }, "kiss": {
        "brf": "Kisses a {member} for a {reason}!",
        "usg": ";]slap {mbr} {?reason}",
        "dsc": """\
MBR    [INT or PING] - The member you want to slap
REASON [STR        ] - The reason for the slap
""",
        "als": [],
        "cat": "int"
    }, "rol": {
        "brf": "Displays info about a given {role}",
        "usg": ";]rol {role}",
        "dsc": "ROLE [ROLE] - The target role, ping or name or ID",
        "als": [],
        "cat": "dis"
    }, "dnd": {
        "brf": "Rolls all the dice from DnD",
        "usg": ";]dnd",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "fun"
    }, "pin": {
        "brf": "Pins a message for you, useful on mobile",
        "usg": ";]pin {mID}",
        "dsc": "mID [INT] - The ID of the message you wish to pin",
        "als": [],
        "cat": "mod"
    }, "unpin": {
        "brf": "Unpins a message for you, useful on mobile",
        "usg": ";]unpin {mID}",
        "dsc": "mID [INT] - The ID of the message you wish to unpin",
        "als": [],
        "cat": "mod"
    }, "spam": {
        "brf": "Spams {x} chars!",
        "usg": ";]spam {?x}",
        "dsc": "X [INT] - How many chars to spam DEFAULT: 10",
        "als": [],
        "cat": "fun"
    }, "inv": {
        "brf": "Invite for me and my support server",
        "usg": ";]inv",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [ "invite" ],
        "cat": "inf"
    }, "chnl": {
        "brf": "Shows info about a given {text_channel}",
        "usg": ";]chnl {txt_chnl}",
        "dsc": "TXT CHNL [TEXT CHANNEL] - The target channel",
        "als": [],
        "cat": "dis"
    }, "hangman": {
        "brf": "DONT Hang the man",
        "usg": ";]hangman",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [ "hman", "hm" ],
        "cat": "fun"
    }, "snd": {
        "brf": "I send {text} to a given {channel}",
        "usg": ";]snd {cID} {mCTX}",
        "dsc": "cID  [INT] - The Channel ID\nmCTX [STR] - The text to send",
        "als": [ "send" ],
        "cat": "fun"
    }, "usr": {
        "brf": "Shows info for a given {user}",
        "usg": ";]usr {usr}",
        "dsc": "USR [MEMBER] - The member you want info on",
        "als": [],
        "cat": "dis"
    }, "mock": {
        "brf": "iM nOt MoCkInG yOu",
        "usg": ";]mock {msg}",
        "dsc": "MSG [INT] - The ID of the message you want me to mock",
        "als": [],
        "cat": "fun"
    }, "calc": {
        "brf": "It is a calculator",
        "usg": ";]calc {eq}",
        "dsc": "EQ [STR] - The thing to solve",
        "als": [],
        "cat": "math"
    }, "cool": {
        "brf": "Gives someone a sneaky surprise",
        "usg": ";]cool {uID}",
        "dsc": "uID [INT] - The ID of the user you are willing to surprise",
        "als": [],
        "cat": "fun"
    }, "pause": {
        "brf": "Toggles the music",
        "usg": ";]pause",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [ "resume", "continue", "stop" ],
        "cat": "music"
    }, "ban": {
        "brf": "Bans {member} for {reason} and deletes their messages from the past {x} days",
        "usg": ";]ban {mbr1} {mbr2} {...} {?num} {?rsn}",
        "dsc": """\
MBRx [INT or PING] - The target member[s],
NUM  [INT   ] - Delete messages from the past {x} days
RSN  [STR   ] - The reason for the ban
""",
        "als": [],
        "cat": "mod"
    }, "audit": {
        "brf": "Edits channels and things",
        "usg": ";]audit",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "mod"
    }, "find": {
        "brf": "Finds a meta object given an ID or name",
        "usg": ";]find {fID}",
        "dsc": "fID [STR] - The name or ID of the thing to find",
        "als": [],
        "cat": "inf"
    }, "emj": {
        "brf": "Sends info about a given {emoji}",
        "usg": ";]emj {emoji}",
        "dsc": "EMOJI [EMOJI] - The CUSTOM emoji in question",
        "als": [],
        "cat": "dis"
    }, "kick": {
        "brf": "Kicks a {member}",
        "usg": ";]kick {mbr1} {mbr2} {...}",
        "dsc": "MBRx [MEMBER] - The target member, ID or ping or name",
        "als": [],
        "cat": "mod"
    }, "emji": {
        "brf": "Steals an emoji for you",
        "usg": ";]emji {emj1} {emj2} {...}",
        "dsc": "EMJx [EMOJI] - The emoji you want to steal",
        "als": [],
        "cat": "fun"
    }, "reddit": {
        "brf": "Gives you a random post from a given {subreddit}",
        "usg": ";]reddit {?subreddit} {?search}",
        "dsc": """\
SUBREDDIT [STR] - The name of the subredditm /r/ is optional
- - /u/ is required to redditor feeds
- - also can be a link to a submission
- - /m/<multireddit>#<redditor> is needed for multireddits
- - - eg /m/CoolMultireddit#Redditor1010
SEARCH    [STR] - What to search for
""",
        "als": [ "rd", "redd", "rdt", "red" ],
        "cat": "fun"
    }, "rng": {
        "brf": "Prints rng from {x} to {y}, {z} times!",
        "usg": ";]rng {x} {y} {?z}",
        "dsc": "X [INT] - Minimum number\nY [INT] - Maximum number\nZ [INT] - OPTIONAL: Number of numbers",
        "als": [],
        "cat": "fun"
    }, "rto": {
        "brf": "Reduces the ratio between {x} and {y}",
        "usg": ";]rto {x} {y}",
        "dsc": "X [INT] - The first number\nY [INT] - The second number",
        "als": [ "frac", "ratio" ],
        "cat": "math"
    }, "bug": {
        "brf": "Creates a bug report",
        "usg": ";]bug {txt}",
        "dsc": "TXT [STR] - The bug, preferably with the error and command",
        "als": [],
        "cat": "inf"
    }, "git": {
        "brf": "Shows the git repo",
        "usg": ";]git",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "inf"
    }, "msg": {
        "brf": "Displays info on a given {message}",
        "usg": ";]msg {msg}",
        "dsc": "MSG [INT] - The ID of the target message",
        "als": [],
        "cat": "dis"
    }, "gld": {
        "brf": "Shows info about this guild",
        "usg": ";]gld",
        "dsc": "[NO ARGS FOR THS COMMAND]",
        "als": [],
        "cat": "dis"
    }, "nick": {
        "brf": "Changes the nickname of a {member} to {this}",
        "usg": ";]nick {mbr} {this}",
        "dsc": "MBR  [INT OR PING] - The target member\nTHIS [STR   ] - The nickname",
        "als": [],
        "cat": "mod"
    }, "_sysinfo": {
        "brf": "Shows what I'm running on",
        "usg": ";]os",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [ "system", "os", "sys" ],
        "cat": "inf"
    }, "rev": {
        "brf": "esreveR",
        "usg": ";]rev {phrase}",
        "dsc": "PHRASE [STR] - The stuff to reverse",
        "als": [],
        "cat": "fun"
    }, "stats": {
        "brf": "Gives statistics on inputed data",
        "usg": ";]stats {x1} {x2} {x3} {...}",
        "dsc": "X [FLOAT] - A number or a statistic",
        "als": [],
        "cat": "math"
    }, "mix": {
        "brf": "A noise generator with 2 inputs",
        "usg": ";]mix {action} {?args}",
        "dsc": """\
ACTION [STR] - [slot1, slot2, imgs, view, slots, kill]
- > slot1 - Load an attached image into the \"image\" file
- > slot2 - Load an attached image into the \"pattern\" file
- > imgs  - View currently loaded images
- > view  - View the status of the current mix
- > slots - Start the mixing
- > kill  - Kills the current process if you started it
ARGS   [STR] - [-iter=,-np]
- > -iter= - Set the number of iterations [max 120, min 5]
- >    -np - Do not ping when finished
""",
        "als": [],
        "cat": "ai"
    }, "leave": {
        "brf": "Leaves the VC",
        "usg": ";]leave",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "music"
    }, "dir": {
        "brf": "C:\\> dir",
        "usg": ";]dir {?path}",
        "dsc": "?PATH [STR] - OPTIONAL: Path",
        "als": [],
        "cat": "inf"
    }, "enbl": {
        "brf": "Enables a {command}",
        "usg": ";]enbl {com_name}",
        "dsc": "COM NAME [STR] - The name of the target command",
        "als": [ "enable" ],
        "cat": "mod"
    }, "poll": {
        "brf": "Creates a poll",
        "usg": ";]poll {txt}",
        "dsc": "TEXT [STR] - The poll content",
        "als": [],
        "cat": "fun"
    }, "dsbl": {
        "brf": "Disables a {command}",
        "usg": ";]dsbl {com_name}",
        "dsc": "COM NAME [STR] - The name of the target command",
        "als": [ "disable" ],
        "cat": "mod"
    }, "graph": {
        "brf": "Your personal graphing calculator",
        "usg": ";]graph {?window} {eq1} {?ops} | {eq2} {?ops} | {...} {?ops}",
        "dsc": """\
WINDOW [INT x 4] - Set XMIN, XMAX, YMIN, YMAX in that order
EQx    [STR    ] - The equation to graph
OPS    [STR    ] - Other arguments
- > `--max` for the maximum point shown in the graph
- > `--min` for the minimum point shown in the graph
- > `--zero` for the roots of the function
- > `--yint` for the y intercept
*Use '>=' and '<=' for 'at least' and 'at most' graphs [respectively]
""",
        "als": [],
        "cat": "math"
    }, "clr": {
        "brf": "Clears {x} messages from chat",
        "usg": ";]clr {x}",
        "dsc": "X [INT] - The number of messages to clear",
        "als": [],
        "cat": "mod"
    }, "md": {
        "brf": "Sends the escaped contents of {messageID}",
        "usg": ";]md {mID}",
        "dsc": "mID [INT] - Message ID",
        "als": [],
        "cat": "fun"
    }, "clrin": {
        "brf": "Clears messages from {int1} to {int2} in chat",
        "usg": ";]clrin {int1} {int2}",
        "dsc": "INTx [INT] - The message IDs to clear in between",
        "als": [],
        "cat": "mod"
    }, "pre": {
        "brf": "Changes the prefix to {pre}",
        "usg": ";]pre {pre}",
        "dsc": "PRE [STR] - The new prefix",
        "als": [ "prefix" ],
        "cat": "mod"
    }, "ping": {
        "brf": "Sends the ping time",
        "usg": ";]ping",
        "dsc": "[NO ARGS FOR THIS COMMAND]",
        "als": [],
        "cat": "inf"
    }, "mines": {
        "brf": "Sweep mines away",
        "usg": ";]mines {?size} {?mines}",
        "dsc": "SIZE  [INT] - X by X tiles DEFAULT: 10\nMINES [INT] - How many mines DEFAULT: 10",
        "als": [],
        "cat": "fun"
    }, "mbr": {
        "brf": "Shows info on a given {member}",
        "usg": ";]mbr {mbr}",
        "dsc": "MBR [MEMBER] - The target member, ID or ping or name",
        "als": [],
        "cat": "dis"
    }, "tag": {
        "brf": "Custom commands, kinda",
        "usg": ";]tag {action} {?name} {?data}",
        "dsc": """\
ACTION [STR] - The action you want to take
- > Use the tag name to view the tag
- > Use 'edit {name} {content}' to edit your tag
- > Use 'add {name} {content}' to create a tag
- > Use 'delete {name}' to delete your tag
NAME   [STR] - Only used when adding or editing a tag
DATA   [STR] - The content when adding or editing a tag
""",
        "als": [],
        "cat": "oth"
    }, "clrto": {
        "brf": "Clears messages from {int1} to {int2}  [non inclusive] in chat",
        "usg": ";]clrto {mID}",
        "dsc": "mID [INT] - The message ID to clear to",
        "als": [],
        "cat": "mod"
    }
}

doc["labels"].innerHTML = '|'.join(list(coms))
element = doc["changes"]
lists = doc["tabby"]

commands = [(com, coms[com]["cat"], 
             coms[com]["brf"], coms[com]["usg"], 
             coms[com]["dsc"], '", "'.join(coms[com]["als"])) for com in coms]
for com, cat, brf, usg, dsc, als in commands:
    lists <= html.BUTTON(com, Class = "tabby_link", Id = com)
    element <= html.DIV(
        mark(f"""\
&&&THE {com} COMMAND
&&&&{brf}
&&&&&CATAGORY ] {cat}
>++ALIASES ] "{als}"++<
-~-
`{usg}`
-~-
Usage Notes ---
;;;
{dsc}
;;;
""")+"<br>", 
        Class = "tabby_sect", 
        Id = "commands_"+com, 
        style={"display": "none"})
win.comm()
