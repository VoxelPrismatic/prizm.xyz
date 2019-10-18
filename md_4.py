from re import sub
def mark(st):
    st = " "+st
    st = st.replace(" ", "\u200b ")
    st = st.replace("§", "\u200b")
    if "&" in st:
        st = sub(r"\&{1}(.+)", r"<span class='head1'>\1</span>", st) # &Header 1
        st = sub(r"\&{2}(.+)", r"<span class='head2'>\1</span>", st) # &&Header 2
        st = sub(r"\&{3}(.+)", r"<span class='head3'>\1</span>", st) # &&&Header 3
        st = sub(r"\&{4}(.+)", r"<span class='head4'>\1</span>", st) # &&&&Header 4
        st = sub(r"\&{5}(.+)", r"<span class='head5'>\1</span>", st) # &&&&&Header 5
        st = sub(r"\&{6}(.+)", r"<span class='head6'>\1</span>", st) # &&&&&&Header 6
    st = sub(r"(.+?)\n={3,}", r"<span class='head1'>\1</span>", st) # header1 ↵ ===
    st = sub(r"(.+?)\n-{3,}", r"<span class='head2'>\1</span>", st) # header2 ↵ ---
    
    st = sub(r"[^\\]\#(.*?)\#", r"<b>\1</b>", st) # #bolded#
    st = sub(r"[^\\]\*(.*?)\*", r"<i>\1</i>", st) # *italics*
    st = sub(r"[^\\]\~(.*?)\~", r"<s>\1</s>", st) # ~strikethrough~
    st = sub(r"[^\\]\_(.*?)\_", r"<u>\1</u>", st) # _underline_
    st = sub(r"[^\\]\>\+{2}(.*?)\+{2}\<", r"<sup>\1</sup>", st) # >++superscript++<
    st = sub(r"[^\\]\>\-{2}(.*?)\-{2}\<", r"<sub>\1</sub>", st) # >--subscript--<
    st = sub(r"[^\\]\:{2}(.*?)\:{2}", r"<span class='oL'>\1</span>", st) # ::overline::
    st = sub(r"[^\\]\%(.*)\%", r"<span class='spoil'>\1</span>", st) # %spoiler%
    
    st = sub(r'[^\\]\"{3}((.*|\n)?)\"{3}', r"<span class='quoted'>\1</span>", st) # """↵quote block↵"""
    st = sub(r"[^\\]\!{3}\[(\w+)\] *((.|\n)*?)\!{3}", r"<span class='note_\1'>\2</span>", st) 
         # !!![color] notice me senpai!!!
    st = sub(r"[^\\]\;{3}((.|\n)*)\;{3}", r"<div class='mono dark' style='width: 90%;'>\1</div>", st)
         # ;;;code block;;;
    st = sub(r"[^\\]\`(.*)\`", r"<span class='mono dark'>\1</span>", st) # `inline code`
    
    st = sub(r"[^\\]( *)(\d+)([.\)\]\}\-:;]) (.*)", r"\1\2] \3", st) # 1] Ordered list
    st = sub(r"[^\\]( *)([-\]>}.~+=]) (.*)", r"\1> \2", st) # > Unordered list
    
    st = sub(r"[^\\]\[(.*)]\<(.*)\>", r"<a href='\2'>\1</a>", st) # [name]<link>
    st = sub(r"[^\\]\<\<(.*)\>\>", r"<a href='\1'>\1</a>", st) # <<link>>
    st = sub(r"[^\\]\#\[(.*)]\<(.*)\>", r"<embed href='\2' alt='\1'>", st) # #[alt text]<link>
    
    st = st.replace("\n---\n", "<div class='mdline'>---</div>") # ↵---↵ sep
    st = st.replace("\n", "<br>") # newline
    st = st.replace("\u200b", "&nbsp;") # Non Breaking Space
    
    #[^\\] - Ignore backslashes
    #(.*) -- Actual content
    
    return st.strip()
