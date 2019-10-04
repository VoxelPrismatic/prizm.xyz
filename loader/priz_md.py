from browser import document as doc
md = {'>~': '<s>',
      '~<': '</s>',
      
      '>#': '<b>',
      '#<': '</b>',
      
      '>*': '<i>',
      '*<': '</i>',
      
      '>_': '<u>',
      '_<': '</u>',
      
      '>+': '<sup>',
      '+<': '</sup>',
      
      '>-': '<sub>',
      '-<': '</sub>',
      
      '>!': '<span class="mono dark">',
      '!<': '</span>',
      
      '>$': '<a href="',
      '$$': '">',
      '$<': '</a>',
      
      '>@': '<span class="notice_',
      '@@': '">',
      '@<': '</span>',
      
      '>t': '<div class="grid',
      '?t': '"><div>',
      '!t': '</div><div>',
      't<': '</div>',
      
      '>]': '<ul>',
      ']]': '<li>',
      '[[': '</li>',
      '[<': '</ul>',
      
      '>}': '<ol>',
      '}}': '<li>',
      '{{': '</li>',
      '{<': '</ol>',
      
      '>/<': '<div style="background-color: #11222288; color: #00000000; width: 90%; height: 2px">---</div>"
     }
