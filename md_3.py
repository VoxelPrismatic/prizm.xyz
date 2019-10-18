from re import sub

rep = {
    " ": ["§ ", " "], #Infinite Spaces
    "§": ["\u200b", "§"],  #Short NBSP char
   
    r"(.+?)\n(=+?)": [r"<span class='head1'>\1</span>", "="],#Header 1
    r"(.+?)\n(-+?)": [r"<span class='head2'>\1</span>", "-"] #Header 2
    r"\&(.+)": [r"<span class='head1'>\1</span>", "&"], #Header 1
    r"\&\&(.+)": [r"<span class='head2'>\1</span>", "&"], #Header 2
    r"\&\&\&(.+)": [r"<span class='head3'>\1</span>", "&"], #Header 3
    r"\&\&\&\&(.+)": [r"<span class='head4'>\1</span>", "&"], #Header 4
    r"\&\&\&\&\&(.+)": [r"<span class='head5'>\1</span>", "&"], #Header 5
    r"\&\&\&\&\&\&(.+)": [r"<span class='head6'>\1</span>", "&"], #Header 6
    
    r"[^\\]\#(.*?)\#": [r"<b>\1</b>", "#"], #Bold
    r"[^\\]\*(.*?)\*": [r"<i>\1</i>", "*"], #Ital
    r"[^\\]\~(.*?)\~": [r"<s>\1</s>", "~"], #Strike
    r"[^\\]\_(.*?)\_": [r"<u>\1</u>", "_"], #Under
    
    r"[^\\]\+\+(.*?)\+\+": [r"<sup>\1</sup>", "++"], #Super
    r"[^\\]\-\-(.*?)\-\-": [r"<sub>\1</sub>", "--"], #Sub
    r"[^\\]\:\:(.*?)\:\:": [r"<span class='oL'>\1</sub>", "::"], #Overline
    r"[^\\]\|(.*)\|": [r"<span class='spoil'>\1</span>", "|"], #Spoiler
    
    r'[^\\]\"\"\"((.*|\n)?)\"\"\"': [r"<span class='quoted'>\1</span>", '"""'], #Quoted
    r"[^\\]\:\:\:[(\w+)]((.|\n)*?)\:\:\:": [r"<span class='note_\1'>\2</span>", ":::"], #Highlight
    
    r"[^\\]\;\;\;((.|\n)*)\;\;\;": [r"<div class='mono dark' style='width: 90%;'>\1</div>", ";;;"], #Code block
    r"[^\\]\`(.*)\`": [r"<span class='mono dark'>\1</span>", "`"], #Inline code block
    
    r"[^\\]( *)(\d+)([.\)\]\}\-:;]) (.*)": [r"\1\2] \3", "1"], #Ordered List
    r"[^\\]( *)([-\]>}.~+=]) (.*)": [r"\1> \2", " "], #Unordered list
    r"[^\\]\[(.*)]\<(.*)\>": [r"<a href='\2'>\1</a>", "["], #Link
    r"[^\\]\<\<(.*)\>\>": [r"<a href='\1'>\1</a>", "<<"], #Link
    r"[^\\]\[\#\[(.*)]\<(.*)\>": [r"<embed href='\2' alt='\1'>", "[#["], #Embed
    
    "\n---\n": ["<div class='mdline'>---</div>", "\n---\n"], #Seperator
    "\n": ["<br>", "\n"], #New Line
    "\u200b": ["&nbsp;", "\u200b"], #Catch for NBSP in string
    
    #[^\\] - Ignore backslashes
    #(.*) -- Actual content
}

reg = tuple([(k, rep[k][0], rep[k][1]) for k in list(rep)])
def mark(st):
    for key, val, ch in reg:
        if ch in st: #Faster loading
            st = sub(key, val, " "+st)[1:]
        #The space is needed because of the backslash escape method in the RegEx
    return st
