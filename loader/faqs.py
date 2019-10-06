from browser import document as doc, html

content = {"OwO WHAT IS THIS?": "This is an empty FAQ because nobody asked any questions yet UwU"}

element = doc["faq"]
rep = {'\n':'<br>',
       '>!':'<span class="mono dark">',
       '!<': '</span>',
       '>#': '<b>',
       '#<': '</b>',
       '>*': '<i>',
       '*<': '</i>',
       '>_': '<u>',
       '_<': '</u>',
       '>`': '<div class="mono dark horz" style="width: 95%;">',
       '`<': '</div>',
       '>$': '<a href="',
       '$$': '">',
       '$<': '</a>',
       '>~': '<s>',
       '~<': '</s>'}
for key in content:
    for re in rep:
        content[key] = content[key].replace(re,rep[re])
    element <= html.DIV(key, Class="header")
    element <= html.DIV(content[key], Class="content consect")
