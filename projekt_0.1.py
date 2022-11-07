import random

# kaardipakk
def kaardipakk():
    mastid = ('poti', 'risti', 'ärtu', 'ruutu')
    väärtus = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
    kaardipakk = []
    for i in väärtus:
        for j in mastid:
            kaardipakk.append((j, i))
    random.shuffle(kaardipakk)
    return kaardipakk

# n arvule mängijatele käte genereerimine, formaadis ([käsi1], [käsi2], ...), välja jagatud kaardid eemaldatakse kaardipakist
def käed(mängijad, kaardipakk):
    for i in range(mängijad):
        käed = []
        for j in range(mängijad):
            x = random.sample(kaardipakk, 2)
            kaardipakk = eemalda(kaardipakk, x)
            käed.append(x)
        print('Mängija', i + 1, 'käsi on:', käed[i])
    print('\n')
    return käed, kaardipakk

# Võetud kaartide eemaldamine kaardipakist
def eemalda(kaardipakk, kaardid):
    for i in kaardid:
        kaardipakk.remove(i)
    return kaardipakk

# Kontrolli, kas sisestati normaalne arv mängijaid
def kontrolli_mängijate_arvu(mängijate_arv, max_arv):
    print('\n')
    while True:
        try:
            mängijate_arv = int(mängijate_arv)
            if 1 < mängijate_arv < (max_arv + 1):
                break
            else:
                print('Sellise arvu mängijatega pole võimalik mängida.')
                mängijate_arv = input('Sisesta mängijate arv: ')
        except:
            print('Sisestatu ei olnud täisarv.')
            mängijate_arv = input('Sisesta mängijate arv: ')

# Lisab lauale flopi, eemaldab lisatud kaardid kaardipakist
def flop(kaardipakk, laud):
    flop = random.sample(kaardipakk, 3)
    for i in flop:  
        laud.append(i)
    kaardipakk = eemalda(kaardipakk, flop)
    print('Flop oli:', flop)
    print('Laual on nüüd:', laud)
    print('\n')
    return laud, kaardipakk

# Lisab lauale turni, eemaldab lisatud kaardid kaardipakist
def turn(kaardipakk, laud):
    turn = random.sample(kaardipakk, 1)
    for i in turn:    
        laud.append(i)
    kaardipakk = eemalda(kaardipakk, turn)
    print('Turn oli:', turn)
    print('Laual on nüüd:', laud)
    print('\n')
    return laud, kaardipakk

# Lisab lauale riveri, eemaldab lisatud kaardid kaardipakist
def river(kaardipakk, laud):
    river = random.sample(kaardipakk, 1)
    for i in river:
        laud.append(i)
    kaardipakk = eemalda(kaardipakk, river)
    print('River oli:', river)
    print('Laual on nüüd:', laud)
    print('\n')
    return laud, kaardipakk

# Paneb käed ja laua kokku
def kõik_käed(käed, laud):
    kõik_käed = []
    for i in käed:
        kõik_kaardid = i
        for j in laud:
            kõik_kaardid.append(j)
        kõik_käed.append(kõik_kaardid)
    return kõik_käed

# Kontrollib Royal Flushi (lõpetamata)
def kontrolli_royal_flush(käed):
    mastid = ('poti', 'risti', 'ruutu', 'ärtu')
    väärtused = (10, 'J', 'Q', 'K', 'A')
    võimalused = []
    for mast in mastid:
        võimalus = set()
        for väärtus in väärtused:
            võimalus.add((mast, väärtus))
        võimalused.append(võimalus)
        
    for i in range(len(käed)):
        käsi = set(käed[i])
        for võimalus in võimalused:
            if võimalus <= käsi:
                käega_muutub_midagi_aga_mdea_kuidas = 1
                

# leiab võitja (lõpetamata)
def leia_võitja(käed, laud):
    x = 0

# Mitu mängijat mängib?
mängijate_arv = input('Sisesta mängijate arv: ')
mängijate_arv = int(mängijate_arv)
kontrolli_mängijate_arvu(mängijate_arv, 3)

# Segatakse kaardipakk
kaardipakk = kaardipakk()

# Jagatakse välja käed
käed, kaardipakk = käed(mängijate_arv, kaardipakk)

# Jagatakse välja laud
laud = []
laud, kaardipakk = flop(kaardipakk, laud)
laud, kaardipakk = turn(kaardipakk, laud)
laud, kaardipakk = river(kaardipakk, laud)

# Jagame kõik käed koos lauaga eraldi hulkadeks
käed = kõik_käed(käed, laud)
print(käed)






