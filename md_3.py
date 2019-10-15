rep = {
    r"(.*)\n(=*)": r"<h1>\1</h1>", #Header 1
    r"(.*)\n(-*)": r"<h2>\1</h2>", #Header 2
    r"\&(.*)": r"<h1>\1</h1>", #Header 1
    r"\&\&(.*)": r"<h2>\1</h2>", #Header 2
    r"\&\&\&(.*)": r"<h3>\1</h3>", #Header 3
    r"\&\&\&\&(.*)": r"<h4>\1</h4>", #Header 4
    r"\&\&\&\&\&(.*)": r"<h5>\1</h5>", #Header 5
    r"\&\&\&\&\&\&(.*)": r"<h6>\1</h6>", #Header 6
    
    r"\#(.*?)\#": r"<b>\1</b>", #Bold
    r"\*(.*?)\*": r"<i>\1</i>", #Ital
    r"\~(.*?)\~": r"<s>\1</s>", #Strike
    r"\_(.*?)\_": r"<u>\1</u>", #Under
    r"\!(.*?)\!": r"<b><i>\1</i></b>", #BoldItal
    r"\^\^(.*?)\^\^": r"<sup>\1</sup>", #Super
    r"\v\^(.*?)\^\v": r"<sub>\1</sub>", #Sub
    
    r"\"\"\"\[(\w+)\](.*?)\"\"\"": r"<span class='note_\1'>\2</span>", #Highlight
    r"( *)(\d+)([.)\]}-:;]) (.*)": r"\1\2] \3", #Ordered List
    r"( *)([-\]>}.~+=]) (.*)": r"\1> \2", #Unordered list
    r"\;\;\;((.|\n)*)\;\;\;": r"<div class='mono dark' style='width: 90%;'>\1</div>" #Code block
    r"\`(.*)\`": r"<span class='mono dark'>\1</span>",
}
