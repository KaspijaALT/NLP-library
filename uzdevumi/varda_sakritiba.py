def analizet_sakritibas(teksts1, teksts2):

    vardi1 = set(teksts1.lower().split())
    vardi2 = set(teksts2.lower().split())
    
    sakritibas = vardi1.intersection(vardi2)
    
    sakritibas_procents = (len(sakritibas) / len(vardi1)) * 100
    
    print("Sakritību analīze:")
    print(f"Sakritīgie vārdi: {sakritibas}")
    print(f"Sakritības procents: {sakritibas_procents:.2f}%")
    
    return {
        'sakritibas_vardi': sakritibas,
        'sakritibas_procents': sakritibas_procents
    }