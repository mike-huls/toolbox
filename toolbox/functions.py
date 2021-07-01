from datetime import datetime

def listChunker(lst, csize:int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), csize):
        yield lst[i:i + csize]

def report(msg:str):
    _time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"{_time}: {msg}")

def weirdCase(targetString:str):
    returnWord:str = ""
    for i,letter in enumerate(targetString):
        i += 1
        if (i % 2 == 0):
            returnWord += letter.lower()
        else:
            returnWord += letter.upper()
    return returnWord