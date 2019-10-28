from javascript import String, RegExp
import javascript as js

def jsStr(st): return String.new(st)
def RegEx(st): return RegExp.new(st)

def pyStr(st):
    if type(st) == js.String:
        return ''.join(st[int(x)] for x in dir(st))
    return str(st)

def sub(re, to, st):
    to = jsStr(to)
    tmp = RegEx("\\\\(\\d+)")
    while String.new(to).search(tmp) != -1:
        to = String.new(to).replace(tmp, "$$$1") #Convert from PY Regex to JS Regex
    re = RegEx(re)
    while String.new(st).search(re) != -1:
        st = String.new(st).replace(re, to) #Doesn't stop until no matches are found
    return pyStr(st)

def link(st):
    st = " "+st
    ##/// LINKS
    if "<" in st:
        st = sub(r"[^\\]\[(.*)\]\<(.*)\>", r"<a href='\2'>\1</a>", st) # [name]<link>
        st = sub(r"[^\\]\<\<(.*)\>\>", r"<a href='\1'>\1</a>", st) # <<link>>
    return st[1:]

def basic(st):
    st = " "+st
    ##/// BASICS
    st = sub(r"[^\\]\#(.+?)\#", r"<b>\1</b>", st) # #bolded#
    st = sub(r"[^\\]\*(.+?)\*", r"<i>\1</i>", st) # *italics*
    st = sub(r"[^\\]\~(.+?)\~", r"<s>\1</s>", st) # ~strikethrough~
    st = sub(r"[^\\]\_(.+?)\_", r"<u>\1</u>", st) # _underline_
    st = sub(r"[^\\]\>\+{2}(.+?)\+{2}\<", r"<sup>\1</sup>", st) # >++superscript++<
    st = sub(r"[^\\]\>\-{2}(.+?)\-{2}\<", r"<sub>\1</sub>", st) # >--subscript--<
    st = sub(r"[^\\]\:{2}(.+?)\:{2}", r"<span class='oL'>\1</span>", st) # ::overline::
    st = sub(r"[^\\]\%(.+?)\%", r"<span class='spoil'>\1</span>", st) # %spoiler%
    return st[1:]

def advan(st):
    st = " "+st
    ##/// ADVANCED
    st = sub(r'[^\\]\"{3}\n?((.+|\n)?)\n?\"{3}', r"<span class='quoted'>\1</span>", st) # """↵quote block↵"""
    st = sub(r"[^\\]\!{3}\n?\[(\w+)\] *((.|\n)+?)\n?\!{3}", r"<span class='note_\1'>\2</span>", st) 
         # !!![color] notice me senpai!!!
    st = sub(r"[^\\]\;{3}\n?((.|\n)+)\n?\;{3}", r"<div class='mono dark' style='width: 90%;'>\1</div>", st)
         # ;;;code block;;;
    st = sub(r"[^\\]\`(.+?)\`", r"<span class='mono dark horz'>\1</span>", st) # `inline code`
    return st[1:]

def setup(st):
    st = " "+st
    ##/// ORGANIZE
    st = sub(r"\n[^\\]( *)(\d+)([.\)\]\}\-:;])* (.*)", r"\1\2] \3", st) # 1] Ordered list
    st = sub(r"\n[^\\]( *)([-\]>}.~+=])* (.*)", r"\1> \2", st) # > Unordered list
    st = st.replace(">-~-<", "<div class='mdsep'><div class='mdline'>---</div></div>") # >-~-< sep
    st = st.replace("<-~->", "<div class='sep'>---</div>") # <-~-> invis sep
    return st[1:]

def init(st):
    st = " "+st
    st = st.replace(" ", "\u200b \u200b")
    st = st.replace("§", "\u200b")
    st = st.replace("£", "\n")
    st = st.replace(";:", "<").replace(":;", ">")
    return st

def head(st):
    st = " "+st
    ##/// HEADERS
    if "&" in st:
        st = sub(r"\&{6}(.+)", r"<div class='head6'>#/ \1</div>", st) # &&&&&&Header 6
        st = sub(r"\&{5}(.+)", r"<div class='head5'>#// \1</div>", st) # &&&&&Header 5
        st = sub(r"\&{4}(.+)", r"<div class='head4'>#// \1</div>", st) # &&&&Header 4
        st = sub(r"\&{3}(.+)", r"<div class='head3'>##/// \1</div>", st) # &&&Header 3
        st = sub(r"\&{2}(.+)", r"<div class='head2'>##/// \1</div>", st) # &&Header 2
        st = sub(r"\&{1}(.+)", r"<div class='head1'>##//// \1</div>", st) # &Header 1
    st = sub(r"(.+?)\n={3,}", r"<div class='head1'>##//// \1</div>", st) # header1 ↵ ===
    st = sub(r"(.+?)\n-{3,}", r"<div class='head2'>##/// \1</div>", st) # header2 ↵ ---
    return st

def other(st):
    st = " "+st
    ##/// OTHER
    st = st.replace("\n", "<br>") # newline
    st.replace("  ", " ").strip('\u200b ')
    return st

def elem(st):
    st = " "+st
    st = sub(r"\@\<(.*)\>", r"<\1>", st) # @div@ --> <div>
    st = sub(r"\%C\((.*)\)S\((.*)\)\[(.*)]\%", r"<button class='linky fullW \1' style='\2'>\3</button>", st)
    st = sub(r"\%S\((.*)\)\[(.*)]\%", r"<button class='linky fullW' style='\1'>\2</button>", st)
    st = sub(r"\%C\((.*)\)\[(.*)]\%", r"<button class='linky fullW \1'>\2</button>", st)
    st = sub(r"\%[(.*)]\%", r"<button class='linky fullW'>\1</button>", st) # %[button]%
    return st[1:]

def strip(st):
    while st.startswith(' ') or st.startswith('\u200b'):
        st = st[1:]
    while st.endswith(' ') or st.endswith('\u200b'):
        st = st[:-1]
    return st
    
def mark(st):
    st = init(st)
    st = elem(st)
    st = link(st)
    st = basic(st)
    st = advan(st)
    st = setup(st)
    st = head(st)
    st = other(st)
    return st
    
    ##/// NOTES
    #[^\\] - Ignore backslashes
    #\n? --- Ignore newlines
    #\X{n} - Atleast n characters of X
    #(.+) -- Actual content
    #(.+?) - Lazy actual content
