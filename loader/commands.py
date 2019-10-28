from browser import document as doc, html, window as win
from priz_md import mark
coms = eval(open('json/commands.json').read())
doc["labels"].innerHTML = '|'.join(list(coms))
element = doc["changes"]
lists = doc["tabby"]

commands = [(com, coms[com]["cat"], coms[com]["brf"], 
             coms[com]["usg"], coms[com]["dsc"], 
             '`;]'+'`, `;]'.join(coms[com]["als"])+'`' if coms[com]["als"] else "`[NONE]`") for com in coms]
for com, cat, brf, usg, dsc, als in commands:
    lists <= html.BUTTON(f"{cat} - ;]{com}", Class = "tabby_link textR wMIN", Id = com)
    element <= html.DIV(
        mark(f"""\
&&&THE `;]{com.strip()}` COMMAND
&&&&{brf.strip()}
&&&&CATAGORY ] {cat.strip()}
&&&&&&ALIASES ] {als}
>-~-<
`{usg.strip()}`
>-~-<
Usage Notes ---
;;;
{dsc.strip()}
;;;
""")+"<br>", 
        Class = "tabby_sect", 
        Id = "commands_"+com, 
        style={"display": "none"})
win.comm()
if doc.URL.split("#")[-1] in coms:
    page = doc.URL.split("#")[-1]
    doc["blocky"].innerHTML = doc["commands_"+page].innerHTML
    doc[page].classList += " active"
