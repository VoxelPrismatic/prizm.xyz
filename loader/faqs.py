from browser import document as doc, html
from priz_md import mark
content = {"OwO WHAT IS THIS?": "This is an empty FAQ because nobody asked any questions yet UwU"}

element = doc["faq"]
for key in content:
    element <= html.DIV(key, Class="header", Id="faq_"+key.lower().replace(" ", "_")+"FAQ")
    element <= html.DIV(mark(content[key]), Class="content consect")
