
def fix_spaces(text):
    return re.sub(r' +', lambda m: '-' if len(m.group()) > 2 else '_', text)
