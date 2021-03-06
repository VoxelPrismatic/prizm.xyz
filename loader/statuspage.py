from priz_md import mark
from browser import document as doc, window as win, html
import datetime as dt

online = False
when = "an unknown time"

history = {
    "12x07_2019": "Discord is experiencing issues, and the bot was manually shut down",
    "11x20_2019": "Linux power settings are not set up - Resolved issue",
    "11x06_2019": "HDD died... waiting for a good SSD price to show up - Resolved issue",
    "10x31_2019": "There is a connection issue on my end - Resolved issue",
    "10x29_2019": "RAM usage is a bit high, so slow response times or even crashes may occur - Resolved issue",
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
