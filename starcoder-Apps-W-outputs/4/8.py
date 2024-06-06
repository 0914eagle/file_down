
def language(txt):
    txt=txt.replace("_","")
    if txt.endswith('po'):
        return "FILIPINO"
    elif txt.endswith('desu') or txt.endswith('masu'):
        return "JAPANESE"
    elif txt.endswith('mnida'):
        return "KOREAN"
