from itertools import product
def generator_cuvinte(n,limbaj):
    lista_cuvinte=[]
    for index in range(0,n+1):
        lista_cuvinte+=product(limbaj,repeat=index)
    lista_cuvinte = [''.join(tuplu) for tuplu in lista_cuvinte]
    return lista_cuvinte

def functie(tabel,stare_actuala,litera_actuala):
    for posibilitate in tabel:
        if stare_actuala==posibilitate[0] and litera_actuala==posibilitate[1]:
            return posibilitate[2]

print("*NOTA: pentru valorile care nu trec cu o anumita litera prin functia de tranzitie, se lasa spatiu liber")
print("1) DFA")
print("2) NFA")
print("3) lambda-NFA")
tip_automat=input("Tipul automatului pentru care doriti sa generati toate cuvintele acceptate: ")
n=int(input("Lungime maxima cuvinte: "))

if tip_automat=="1" or tip_automat=="DFA":
    with open("input.txt","r") as f:
        stari=[str(x) for x in f.readline().strip().split()]
        alfabet = [str(x) for x in f.readline().strip().split()]
        tabel=[]
        for stare in stari:
            for litera in alfabet:
                stare_echivalenta = str(f.readline().strip("\n"))
                tabel.append((stare,litera,stare_echivalenta))
        stare_initiala = str(f.readline().strip())
        stari_finale=[str(x) for x in f.readline().strip().split()]
    if stare_initiala not in stari:
            print("Ati introdus datele gresit.")
            exit()
    for x in stari_finale:
        if x not in stari:
            print("Ati introdus datele gresit.")
            exit()
    for x in tabel:
        if x[2] not in stari and x[2]!="":
            print("Ati introdus datele gresit.")
            exit()

    lista_cuvinte=generator_cuvinte(n,alfabet)
    for cuvant in lista_cuvinte:
        stare_actuala = stare_initiala
        for index in range(len(cuvant)):
            stare_actuala = functie(tabel, stare_actuala, cuvant[index])
        if stare_actuala in stari_finale:
            print(cuvant)

if tip_automat=="2" or tip_automat=="NFA":
    with open("input.txt", "r") as f:
        stari = [str(x) for x in f.readline().strip().split()]
        alfabet = [str(x) for x in f.readline().strip().split()]
        tabel = []
        for stare in stari:
            for litera in alfabet:
                stare_echivalenta = f.readline().strip("\n").split()
                tabel.append((stare, litera, stare_echivalenta))
        stare_initiala = str(f.readline().strip())
        stari_finale = [str(x) for x in f.readline().strip().split()]
    if stare_initiala not in stari:
        print("Ati introdus datele gresit.")
        exit()
    for x in stari_finale:
        if x not in stari:
            print("Ati introdus datele gresit.")
            exit()
    for x in tabel:
        for y in x[2]:
            if y not in stari  and x[2] !=[]:
                print("Ati introdus datele gresit.")
                exit()
    lista_cuvinte = generator_cuvinte(n, alfabet)
    for cuvant in lista_cuvinte:
        stari_actuale = [stare_initiala]
        for index in range(len(cuvant)):
            temp=[]
            for stare in stari_actuale:
                temp+=functie(tabel,stare,cuvant[index])
            stari_actuale=temp
        for stare in stari_actuale:
            if stare in stari_finale:
                print(cuvant)
                break

if tip_automat=="3" or tip_automat=="lambda-NFA":
    with open("input.txt", "r") as f:
        stari = [str(x) for x in f.readline().strip().split()]
        alfabet = [str(x) for x in f.readline().strip().split()]
        alfabet.append("λ")
        tabel = []
        for stare in stari:
            for litera in alfabet:
                stare_echivalenta = f.readline().strip("\n").split()
                tabel.append((stare, litera, stare_echivalenta))
        stare_initiala = str(f.readline().strip())
        stari_finale = [str(x) for x in f.readline().strip().split()]
    if stare_initiala not in stari:
        print("Ati introdus datele gresit.")
        exit()
    for x in stari_finale:
        if x not in stari:
            print("Ati introdus datele gresit.")
            exit()
    for x in tabel:
        for y in x[2]:
            if y not in stari and x[2] != []:
                print("Ati introdus datele gresit.")
                exit()
    lambda_count=0
    for x in tabel:
        if "λ"==x[1] and len(x[2])!=0:
            lambda_count+=5
    cuvinte_acceptate=[]
    lista_cuvinte = generator_cuvinte(n+lambda_count, alfabet)
    for cuvant in lista_cuvinte:
        stari_actuale = [stare_initiala]
        for index in range(len(cuvant)):
            temp=[]
            for stare in stari_actuale:
                temp+=functie(tabel,stare,cuvant[index])
            stari_actuale=temp
        for stare in stari_actuale:
            if stare in stari_finale and cuvant.replace("λ","") not in cuvinte_acceptate and len(cuvant.replace("λ",""))<=n:
                cuvinte_acceptate.append(cuvant.replace("λ",""))
                break
    print(len(cuvinte_acceptate))
    print(*cuvinte_acceptate)



