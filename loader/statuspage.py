from priz_md import mark
from browser import document as doc, window as win, html

online = False
current = "There is a `NameError` in the main file"
when = "6PM CST"
history = {
    "10x21_2019": "There was a `NameError` issue in the main file",
    "10x17_2019": "PC was off [how?] - Resolved issue",
    "00x00_0000": "Thats the beginning of the history"
}
for key in history:
    history[key] = mark(history[key])
    doc["status"] <= html.DIV(key+" - "+history[key], Id="status_"+key, Class="content consect")

doc["current_status"].innerHTML = "PRIZM IS " + ("ONLINE ;]" if online else "OFFLINE ;[")
doc["issue"].innerHTML = "No issues here" if online else current+"\nWill be fixed at "+when
