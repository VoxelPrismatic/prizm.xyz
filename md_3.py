from re import sub

rep = {
    " ": ["\u200b ", " "], #Infinite Spaces
    "§": ["\u200b", "§"],  #Short NBSP char
    "\u200b": ["&nbsp;", "\u200b"], #Catch for NBSP in string
    
    r"(.+?)\n(=+?)": [r"<span class='head1'>\1</span>", "="], #Header 1
    r"(.+?)\n(-+?)": [r"<span class='head2'>\1</span>", "-"], #Header 2
    r"\&{1}(.+)": [r"<span class='head1'>\1</span>", "&"], #Header 1
    r"\&{2}(.+)": [r"<span class='head2'>\1</span>", "&"], #Header 2
    r"\&{3}(.+)": [r"<span class='head3'>\1</span>", "&"], #Header 3
    r"\&{4}(.+)": [r"<span class='head4'>\1</span>", "&"], #Header 4
    r"\&{5}(.+)": [r"<span class='head5'>\1</span>", "&"], #Header 5
    r"\&{6}(.+)": [r"<span class='head6'>\1</span>", "&"], #Header 6
    
    r"[^\\]\#(.*?)\#": [r"<b>\1</b>", "#"], #Bold
    r"[^\\]\*(.*?)\*": [r"<i>\1</i>", "*"], #Ital
    r"[^\\]\~(.*?)\~": [r"<s>\1</s>", "~"], #Strike
    r"[^\\]\_(.*?)\_": [r"<u>\1</u>", "_"], #Under
    
    r"[^\\]\+{2}(.*?)\+{2}": [r"<sup>\1</sup>", "++"], #Super
    r"[^\\]\-{2}(.*?)\-{2}": [r"<sub>\1</sub>", "--"], #Sub
    r"[^\\]\:{2}(.*?)\:{2}": [r"<span class='oL'>\1</sub>", "::"], #Overline
    r"[^\\]\|(.*)\|": [r"<span class='spoil'>\1</span>", "|"], #Spoiler
    
    r'[^\\]\"{3}((.*|\n)?)\"{3}': [r"<span class='quoted'>\1</span>", '"""'], #Quoted
    r"[^\\]\:{3}[(\w+)]((.|\n)*?)\:{3}": [r"<span class='note_\1'>\2</span>", ":::"], #Highlight
    r"[^\\]\;{3}((.|\n)*)\;{3}": [r"<div class='mono dark' style='width: 90%;'>\1</div>", ";;;"], #Code block
    r"[^\\]\`(.*)\`": [r"<span class='mono dark'>\1</span>", "`"], #Inline code block
    
    r"[^\\]( *)(\d+)([.\)\]\}\-:;]) (.*)": [r"\1\2] \3", "1"], #Ordered List
    r"[^\\]( *)([-\]>}.~+=]) (.*)": [r"\1> \2", " "], #Unordered list
    
    r"[^\\]\[(.*)]\<(.*)\>": [r"<a href='\2'>\1</a>", "["], #Link
    r"[^\\]\<\<(.*)\>\>": [r"<a href='\1'>\1</a>", "<<"], #Link
    r"[^\\]\#\[(.*)]\<(.*)\>": [r"<embed href='\2' alt='\1'>", "#["], #Embed
    
    "\n---\n": ["<div class='mdline'>---</div>", "\n---\n"], #Seperator
    "\n": ["<br>", "\n"], #New Line
    
    #[^\\] - Ignore backslashes
    #(.*) -- Actual content
}

reg = tuple([(k, rep[k][0], rep[k][1]) for k in list(rep)])
def mark(st):
    for key, val, ch in reg:
        if ch in st: #Faster loading
            st = sub(key, val, " "+st)[1:]
            ps = False
            #The space is needed because of the backslash escape method in the RegEx
    return st
