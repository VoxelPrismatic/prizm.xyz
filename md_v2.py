import javascript as js
def Str(st):
    return js.String.new(st)
def Re(st):
    return js.RegExp.new(st)
def sub(re, to, st):
    to = to.replace("\1","$1").replace("\2","$2")
    st = Str(st)
    re = Re(re)
    while st.search(re) != -1:
        st = st.replace(re, to)
    return st
def mark(st):
    ##/// INIT
    st.replace(" ", "\u200b")
    
    ##/// SINGLE PARAM
    st = sub(r"\>\*(.*)\*\<", r"<i>\1</i>", st) #Italic
    st = sub(r"\>\#(.*)\#\<", r"<b>\1</b>", st) #Bold
    st = sub(r"\>\~(.*)\~\<", r"<s>\1</s>", st) #Strike
    st = sub(r"\>\_(.*)\_\<", r"<u>\1</u>", st) #Underline
    st = sub(r"\>\+(.*)\+\<", r"<sup>\1</sup>", st) #Superscript
    st = sub(r"\>\-(.*)\-\<", r"<sub>\1</sub>", st) #Subscript
    st = sub(r"\>\:(.*)\:\<", r"<span class='oL'>\1</span>", st) #Overline
    
    ##/// DOUBLE PARAM
    st = sub(r"\>\$(.*)\$\$(.*)\$\<", r"<a href='\1'>\2</a>", st) #Link
    st = sub(r"\>\$(.*)\$\$(.*)\$\<", r"<a href='\1'>\2</a>", st) #Link
    
    ##/// MULTI PARAM
    
    
    ##/// FINISH
    st
