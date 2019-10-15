import javascript as js
def jsStr(st): return js.String.new(st)
def RegEx(st): return js.RegExp.new(st)
def pyStr(st):
    if type(st) == js.JSObject:
        return ''.join(st[int(x)] for x in dir(st))
    return str(st)

def sub(re, to, st):
    to = jsStr(to)
    tmp = RegEx("\\\\(\\d+)")
    while to.search(tmp) != -1:
        to = jsStr(to.replace(tmp, "$$$1"))
    print('CONVERT')
    re = RegEx(re)
    while st.search(re) != -1:
        st = jsStr(st.replace(re, to))
    return pyStr(st)

rep = {
    " ": "\u200b ", #Infinite Spaces
    "§": "\u200b",  #Short NBSP char
    
    r"(.*)\n(=*)": r"<span class='head1'>\1</span>", #Header 1
    r"(.*)\n(-*)": r"<span class='head2'>\1</span>", #Header 2
    r"\&(.+)": r"<span class='head1'>\1</span>", #Header 1
    r"\&\&(.+)": r"<span class='head2'>\1</span>", #Header 2
    r"\&\&\&(.+)": r"<span class='head3'>\1</span>", #Header 3
    r"\&\&\&\&(.+)": r"<span class='head4'>\1</span>", #Header 4
    r"\&\&\&\&\&(.+)": r"<span class='head5'>\1</span>", #Header 5
    r"\&\&\&\&\&\&(.+)": r"<span class='head6'>\1</span>", #Header 6
    
    r"[^\\]\#(.*?)\#": r"<b>\1</b>", #Bold
    r"[^\\]\*(.*?)\*": r"<i>\1</i>", #Ital
    r"[^\\]\~(.*?)\~": r"<s>\1</s>", #Strike
    r"[^\\]\_(.*?)\_": r"<u>\1</u>", #Under
    r"[^\\]\+\+(.*?)\+\+": r"<sup>\1</sup>", #Super
    r"[^\\]\-\-(.*?)\-\-": r"<sub>\1</sub>", #Sub
    r"[^\\]\:\:(.*?)\:\:": r"<span class='oL'>\1</sub>", #Overline
    r"[^\\]\|(.*)\|": r"<span class='spoil'>\1</span>", #Spoiler
    
    r"[^\\]\"\"\"((.*|\n)?)\"\"\"": r"<span class='quoted'>\1</span>", #Quoted
    r"[^\\]\:\:\:[(\w+)\]((.|\n)*?)\:\:\:": r"<span class='note_\1'>\2</span>", #Highlight
    r"[^\\]\;\;\;((.|\n)*)\;\;\;": r"<div class='mono dark' style='width: 90%;'>\1</div>", #Code block
    r"[^\\]\`(.*)\`": r"<span class='mono dark'>\1</span>", #Inline code block
    
    r"[^\\]( *)(\d+)([.)\]}-:;]) (.*)": r"\1\2] \3", #Ordered List
    r"[^\\]( *)([-\]>}.~+=]) (.*)": r"\1> \2", #Unordered list
    
    r"[^\\]\[(.*)]\<(.*)\>": r"<a href='\2'>\1</a>", #Link
    r"[^\\]\<(.*)\>": r"<a href='\1'>\1</a>", #Link
    r"[^\\]\[\#\[(.*)]\<(.*)\>": r"<embed href='\2' alt='\1'>", #Embed
    
    "\n---\n": "<div class='mdline'>---</div>", #Seperator
    "\n": "<br>", #New Line
    
    
    #[^\\] - Ignore backslashes
    #(.*) -- Actual content
}

def mark(st):
    for key, val in [(k, rep[k]) for k in list(rep)]:
        st = sub(key, val, st)
    return st
print(mark("*hello m8*"))
