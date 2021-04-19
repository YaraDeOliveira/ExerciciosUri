caract1 = str(input()).lower()
caract2 = str(input()).lower()
caract3 = str(input()).lower()
if caract1 == 'vertebrado':
    if caract2 == 'ave':
        if caract3 == 'carnivoro':
            print("aguia")
        else:
            print("pomba")
    else:
        if caract3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if caract2 == 'inseto':
        if caract3 == 'hematofago':
            print("pulga")
        else:
            print("lagarta")
    else:
        if caract3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
