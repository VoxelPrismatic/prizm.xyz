from browser import document as doc
url = doc.URL
if "#" in url:
    area = url.split("#")[-1]
    if area.startswith("changes_"):
        doc["btn_change"].click()
        doc["changes"].scrollIntoView()
        elem = doc[area.split("_")[-1]]
        if elem: elem.click()
            
    elif area.startswith("about_"):
        doc["btn_about"].click()
        doc["about"].scrollIntoView()
        elem = doc[area]
        if elem: elem.scrollIntoView()
            
    elif area.startswith("faq_"):
        doc["btn_faq"].click()
        doc["faq"].scrollIntoView()
        elem = doc[area]
        if elem: elem.scrollIntoView()
        
    elif area.startswith("status_"):
        doc["btn_status"].click()
        doc["status"].scrollIntoView()
        elem = doc[area]
        if elem: elem.scrollIntoView()
    
    elif area.startswith("commands_"):
        doc["changes"].scrollIntoView()
        elem = doc[area.split("_")[-1]]
        if elem: elem.click()
        
