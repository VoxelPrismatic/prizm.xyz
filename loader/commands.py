from browser import document as doc, html, window as win
from priz_md import mark
coms = {
    "command": {
        "cat": "catagory",
        "brf": "description",
        "usg": ";] stuff",
        "dsc": "Help text",
        "als": [""]
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
`{usg}`
Usage Notes ---
;;;
{dsc}
;;;
""")+"<br>", 
        Class = "tabby_sect", 
        Id = "commands_"+com, 
        style={"display": "none"})
win.comm()
