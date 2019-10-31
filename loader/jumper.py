from browser import document ashttps://github.com/VoxelPrismatic/prizm.xyz/tree/master/loader doc
url = doc.URL
if "#" in url:
    area = url.split("#")[-1]
    if area.startswith("changes_"):
        doc["btn_change"].click()
        doc["changes"].scrollIntoView()
        elem = doc[area]
        if elem: elem.click()
    elif area.startswith("about_"):
        doc["btn_about"].click()
        doc["about"].scrollIntoView()
        elem = doc[area]
        if elem: elem.scrollIntoView()
    elif area.startswith("
        
