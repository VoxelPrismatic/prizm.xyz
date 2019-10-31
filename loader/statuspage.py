from priz_md import mark
from browser import document as doc, window as win, html
online = True
when = "7PM CST"
history = {
    "10x29_2019": "RAM usage is a bit high, so slow response times or even crashes may occur - resolved",
    "10x22_2019": "The `embedify` module has a `SyntaxError` - Resolved issue",
    "10x21_2019": "There was a `NameError` issue in the main file - Resolved Issue",
    "10x17_2019": "PC was off [how?] - Resolved issue",
    "00x00_0000": "Thats the beginning of the history"
}
for key in history:
    history[key] = mark(history[key])
    doc["status"] <= html.DIV(key+" - "+history[key], Id="status_"+key, Class="content consect")

doc["current_status"].innerHTML = "PRIZM IS " + ("ONLINE ;]" if online in [True, None] else "OFFLINE ;[")
doc["issue"].innerHTML = "No issues here" if online else mark(history[list(history)[0]]) + "<br>Will be fixed at " + when
