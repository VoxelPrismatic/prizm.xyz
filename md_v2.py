import javascript as js
def Str(st):
    return js.string(st)
def Re(st):
    return js.RegExp(st)
def sub(re, to, st):
    st = Str(st)
    re = Re(re)
    while st.search(re) != -1:
        st = st.replace(re, to)
    return st
def mark(st):
    st = sub(r"\>\*(.*)\*\<", r"<i>\1</i>", st) #Italic
    st = sub(r"\>\#(.*)\#\<", r"<b>\1</b>", st) #Bold
    st = sub(r"\>\~(.*)\~\<", r"<s>\1</s>", st) #Strike
    st = sub(r"\>\_(.*)\_\<", r"<u>\1</u>", st) #Underline
    st = sub(r"\>\+(.*)\+\<", r"<sup>\1</sup>", st) #Superscript
    st = sub(r"\>\-(.*)\-\<", r"<sub>\1</sub>", st) #Subscript
    st = sub(r"\>\:(.*)\:\<", r"<span style='text-decoration: overline'>\1</span>", st) #Overline
