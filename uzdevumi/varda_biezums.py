import re
from collections import Counter

def analizet(teksts):
    teksts = teksts.lower()
    
    vardi = re.findall(r'\b\w+\b', teksts)
    
    biezums = Counter(vardi)
    
    print("Vārdu biežuma analīze:")
    for vards, skaits in biezums.items():
        print(f"{vards}: {skaits}")
    
    return dict(biezums)