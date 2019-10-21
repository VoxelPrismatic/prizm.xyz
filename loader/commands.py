from browser import document as doc, html
from priz_md import mark
coms = {
    "command": {
        "cat": "catagory",
        "brf": "description",
        "usg": ";] stuff",
        "dsc": "Help text"
    }
}
commands = [(com, coms[com]["cat"], coms[com]["brf"], coms[com]["usg"], coms[com]["dsc"]) for com in coms]
for com, cat, brf, usg, dsc in commands:
    j
