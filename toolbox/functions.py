from datetime import datetime

def listChunker(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def report(msg:str):
    _time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(f"{_time}: {msg}")

def camelCase(targetString:str):
    outp = targetString
    outp = outp[0].lower() + outp[1:]
    if (len(outp) <= 3):
        outp = outp.lower()
    return outp
