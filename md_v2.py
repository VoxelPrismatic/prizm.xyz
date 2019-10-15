from javascript import String as Str, RegExp as RegEx

others = {">|": "<table>",
          "|#": "<th><td>",
          "-|": "</td><td>",
          "#|": "</td></th>",
          "+|": "</td></tr><tr><td>",
          "|+": "</td></tr>",
          "|<": "</table>",
          # ^Table
          
          ">&": "<ul><li>",
          "&&": "</li><li>",
          "&<": "</li></ul>",
          # ^Unordered list
          
          ">^": "<ol><li>",
          "^^": "</li><li>",
          "^<": "</li></ol>",
          # ^Ordered list
         }

def replaces(st, *arg):
    for ex, to in arg:
        st = st.replace(ex, to)
    return st

def pyStr(st):
    return ''.join(st[int(x)] for x in dir(st))

def sub(re, to, st):
    to = Str(to)
    tmp = RegEx("\\(\d+)")
    while to.search(tmp) != -1:
        to = to.replace(tmp, "$$$1")
    to = pyStr(to)
    st = Str(st)
    re = RegEx(re)
    while st.search(re) != -1:
        st = st.replace(re, to)
    return pyStr(st)

def mark(st):
    ##/// INIT
    st = st.replace("\t", "    ")
    st.replace(" ", "\u200b")
    
    ##/// SINGLE PARAM
    st = sub(r"\>\*(.*)\*\<", r"<i>\1</i>", st) #Italic
    st = sub(r"\>\#(.*)\#\<", r"<b>\1</b>", st) #Bold
    st = sub(r"\>\~(.*)\~\<", r"<s>\1</s>", st) #Strike
    st = sub(r"\>\_(.*)\_\<", r"<u>\1</u>", st) #Underline
    st = sub(r"\>\+(.*)\+\<", r"<sup>\1</sup>", st) #Superscript
    st = sub(r"\>\-(.*)\-\<", r"<sub>\1</sub>", st) #Subscript
    st = sub(r"\>\:(.*)\:\<", r"<span class='oL'>\1</span>", st) #Overline
    st = sub(r"\>\=(.*)\=\<", r"<span class='spoil'>\1</span>", st) #Spoiler
    st = sub(r"\>\!(.*)\!\<", r"<span class='mono dark'>\1</span>", st) #Inline code
    st = sub(r"\>\`(.*)\`\<", r"<div class='mono dark' style='width: 90%'>\1</div>", st) #Code block
    
    ##/// DOUBLE PARAM
    st = sub(r"\>\$(.*)\$\$(.*)\$\<", r"<a href='\1'>\2</a>", st) #Link
    st = sub(r"\>\@(.*)\@\@(.*)\@\<", r"<span class='note_\1'>\2</span>", st) #Highlight
    st = sub(r"\>\?(.*)\?\?(.*)\?\<", r"<span class='head\1'>\2</span>", st) #Header
    
    ##/// MULTI PARAM
    for key in others:
        st = st.replace(key, others[key])
    
    ##/// FINISH
    st = st.replace(">/<", "<div class='mdline'>---</div>")
    st = st.replace("\n", "<br>")
    st = st.replace("\>", "&gt;")
    st = st.replace("\<", "&lt;")
    return st
