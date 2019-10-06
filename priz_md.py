from browser import document as doc
md = {'>~': '<s>',
      '~<': '</s>',
      # ^Strike through
      
      '>#': '<b>',
      '#<': '</b>',
      # ^Bold
      
      '>*': '<i>',
      '*<': '</i>',
      # ^Italic
      
      '>_': '<u>',
      '_<': '</u>',
      # ^Underline
      
      '>+': '<sup>',
      '+<': '</sup>',
      # ^Superscript
      
      '>-': '<sub>',
      '-<': '</sub>',
      # ^Subscript
      
      '>!': '<span class="mono dark">',
      '!<': '</span>',
      # ^Code
      
      '>$': '<a href="',
      '$$': '">',
      '$<': '</a>',
      # ^Link
      
      '>@': '<span class="note_',
      '@@': '">',
      '@<': '</span>',
      # ^Highlight / Quote
      
      '>|': '<table><th>',
      '?|': '</th><th>',
      '!|': '</th><tr>',
      '||': '</tr><tr>',
      '|<': '</tr></table>',
      # ^Table
      
      '>&': '<ul><li>',
      '&&': '</li><li>',
      '&<': '</li></ul>',
      # ^Unordered list
      
      '>%': '<ol><li>',
      '%%': '</li><li>',
      '%<': '</li></ol>',
      # ^Ordered list
      
      '>`': '<div class="mono dark" style="width: 60%">',
      '`<': '</div>',
      # ^Code block
      
      '>/<': '<div class="mdline">---</div>',
      # ^Seperator line
      
      '>?': '<div class="head',
      '??': '">',
      '?<': '</div>',
      # ^Header
}

def mark(st: str):
    for key in md:
        st = st.replace(key, md[key])
    return st
