from priz_md import mark
from browser import document as doc, window as win, html
history = {
    "00x00_0000": "Thats the beginning of the history"
}
for key in history:
    history[key] = mark(history[key])
    doc["status"] <= html.DIV(key+" - "+history[key], Class="status_"+key)
