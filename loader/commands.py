from browser import document as doc, html, window as win
from priz_md import mark
coms = eval(open('json/commands.json').read())
doc["labels"].innerHTML = 'COM|'.join(list(coms))+"COM"
element = doc["changes"]
lists = doc["tabby"]

commands = [(com, coms[com]["cat"], coms[com]["brf"], 
             coms[com]["usg"], coms[com]["dsc"], 
             '`;]'+'`, `;]'.join(coms[com]["als"])+'`' if coms[com]["als"] else "`[NONE]`") for com in coms]
for com, cat, brf, usg, dsc, als in commands:
    lists <= html.BUTTON(f"{cat} - ;]{com}", Class = "tabby_link textR wMIN", Id = com+"COM")
    element <= html.DIV(
        mark(f"""\
&&&THE `;]{com.strip()}` COMMAND
&&&&{brf.strip()}
&&&&CATAGORY ] {cat.strip()}
&&&&&&ALIASES ] {als}
>-~-<
`{usg.strip()}`

Usage Notes ---
;;;
{dsc.strip()}
;;;
"""+"#NOTICE ]# The {arg} stuff is a description of what to put, not what to write")+"<br>", 
        Class = "tabby_sect", 
        Id = "commands_"+com+"COM",
        style={"display": "none"})
win.comm()
