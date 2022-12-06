import random
import itertools

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
def käed(mängijad, kaardipakk, nimed):
    käed = []
    for i in range(mängijad):
        x = random.sample(kaardipakk, 2)
        kaardipakk = eemalda(kaardipakk, x)
        käed.append(x)
        print(nimed[i], 'sai kätte:', käed[i])
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
    return mängijate_arv

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

# Kontrollib Royal Flushi
def kontrolli_royal_flush(käsi):
    mastid = ('poti', 'risti', 'ruutu', 'ärtu')
    väärtused = (10, 'J', 'Q', 'K', 'A')
    võimalused = []
    for mast in mastid:
        võimalus = set()
        for väärtus in väärtused:
            võimalus.add((mast, väärtus))
        võimalused.append(võimalus)
    for i in range(len(käsi)):
        käsi = set(käsi)
        for võimalus in võimalused:
            if võimalus.issubset(käsi):
                return True
    return (False, '')

def kontrolli_straight_flush(käsi):
    if kontrolli_straight(käsi)[0] == True and kontrolli_flush(käsi)[0] == True:
        if set(kontrolli_straight(käsi)[1]) != set(kontrolli_flush(käsi)[1]):
            return (True, kontrolli_three_of_a_kind(käsi)[1])
    return (False, '')

def kontrolli_four_of_a_kind(käsi):
    mastid = ('poti', 'risti', 'ruutu', 'ärtu')
    väärtused = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
    võimalused = []
    for väärtus in väärtused:
        võimalus = set()
        for mast in mastid:
            võimalus.add((mast, väärtus))
        võimalused.append(võimalus)
    võimalused.reverse()
    for i in võimalused:
        if i.issubset(set(käsi)):
            return (True, list(i)[0][1])
    return (False, '')

def kontrolli_full_house(käsi):
    if kontrolli_three_of_a_kind(käsi)[0] == True and kontrolli_pair(käsi)[0] == True:
        if kontrolli_three_of_a_kind(käsi)[1] != kontrolli_pair(käsi)[1]:
            return (True, kontrolli_three_of_a_kind(käsi)[1], kontrolli_pair(käsi)[1])
    return (False, '')

def kontrolli_flush(käed):
    mastid = ('poti', 'risti', 'ruutu', 'ärtu')
    masti_jär = []
    väärtus_jär = []
    flush = []
    for k in käed:
        masti_jär.append(k[0])
        väärtus_jär.append(k[1])
    for mast in mastid: 
        if masti_jär.count(mast) >= 5:
            for kaart in range(len(masti_jär)):
                if masti_jär[kaart] == mast:
                    flush.append(väärtus_jär[kaart])
            return (True, flush)
    return (False, "")

def kontrolli_straight(käsi):
    võimalused = []
    väärtused = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    väärtused.reverse()
    for indeks in range(0, 9):
        võimalused.append(väärtused[indeks:indeks+5])
    nr = []
    for n in käsi:
        nr.append(n[1])
    for i in range(len(võimalused)):
        if set((võimalused[i])).issubset(set(nr)):
            return (True, võimalused[i])
    return (False, '')

def kontrolli_three_of_a_kind(käsi):
    mastid = ('poti', 'risti', 'ruutu', 'ärtu')
    väärtused = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    väärtused.reverse()
    võimalused = []
    masti_võimalused = list(itertools.combinations(mastid, 3))
    for väärtus in väärtused:    
        for masti_võimalus in masti_võimalused:
            võimalus = set()
            for mast in masti_võimalus:
                võimalus.add((mast, väärtus))
            võimalused.append(võimalus)
    for i in võimalused:
        if i.issubset(set(käsi)):
            return (True, list(i)[0][1])
    return (False, '')

def kontrolli_pair(käsi):
    mastid = ('poti', 'risti', 'ruutu', 'ärtu')
    väärtused = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    väärtused.reverse()
    võimalused = []
    masti_võimalused = list(itertools.combinations(mastid, 2))
    for väärtus in väärtused:    
        for masti_võimalus in masti_võimalused:
            võimalus = set()
            for mast in masti_võimalus:
                võimalus.add((mast, väärtus))
            võimalused.append(võimalus)
    for i in võimalused:
        if i.issubset(set(käsi)):
            return (True, list(i)[0][1])
    return (False, '')

def kontrolli_two_pairs(käsi):
    mastid = ('poti', 'risti', 'ruutu', 'ärtu')
    väärtused = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    väärtused.reverse()
    võimalused = []
    masti_võimalused = list(itertools.combinations(mastid, 2))
    for väärtus in väärtused:    
        for masti_võimalus in masti_võimalused:
            võimalus = set()
            for mast in masti_võimalus:
                võimalus.add((mast, väärtus))
            võimalused.append(võimalus)
    for i in võimalused:
        for j in võimalused:
            if list(i)[0][1] != list(j)[0][1] and i.issubset(set(käsi)) and j.issubset(set(käsi)):
                return (True, list(i)[0][1], list(j)[0][1])
    return (False, '')

def kontrolli_high_card(käsi):
    mastid = ('poti', 'risti', 'ruutu', 'ärtu')
    väärtused = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    väärtused.reverse()
    võimalused = []
    for väärtus in väärtused:
        for mast in mastid:
            võimalus = set()
            võimalus.add((mast, väärtus))
            võimalused.append(võimalus)
    for i in võimalused:
        if i.issubset(set(käsi)):
            return (True, list(i)[0][1])
    return (False, '')

# leiab võitja (lõpetamata)
def leia_võitja(käed):
    suurus = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    võitjad = []
    suurim = 0
    for i in käed:
        if i[0] > suurim:
            suurim = i[0]
    for i in käed:
        if i[0] == suurim:
            võitjad.append(i)

    if len(võitjad) == 1:
        print('Mängu võitis: mängija', str(käed.index(võitjad[0]) + 1))
    elif len(võitjad) == 2:
        if võitjad[0][1] == võitjad[1][1]:
            print()

def mängijate_nimed(mängijate_arv):
    jär = []
    for i in range(mängijate_arv):
        tekst = 'Sisesta' + str(i+1) + '. mängija nimi: '
        nimi = input(tekst)
        jär.append(nimi)
    return jär
        

            
        
        

# Mitu mängijat mängib?
mängijate_arv = input('Sisesta mängijate arv: ')
mängijate_arv = int(mängijate_arv)
mängijate_arv = kontrolli_mängijate_arvu(mängijate_arv, 5)

nimed = mängijate_nimed(mängijate_arv)
#nimed = [1, 2, 3, 4, 5]

# Segatakse kaardipakk
kaardipakk = kaardipakk()
# Jagatakse välja käed
käed, kaardipakk = käed(mängijate_arv, kaardipakk, nimed)

# Jagatakse välja laud
laud = []
laud, kaardipakk = flop(kaardipakk, laud)
laud, kaardipakk = turn(kaardipakk, laud)
laud, kaardipakk = river(kaardipakk, laud)

# Jagame kõik käed koos lauaga eraldi hulkadeks
käed = kõik_käed(käed, laud)

j = -1
for i in käed:
    j += 1
    if kontrolli_royal_flush(i) == True:
        print('Mängijal', nimed[j], 'on Royal FLush')
        käed[j] = (10, 'A')
    
    elif kontrolli_straight_flush(i) == True:
        print('Mängijal', nimed[j], 'on Straight Flush')
        käed[j] = (9, kontrolli_straight_flush(i)[1])
    
    elif kontrolli_four_of_a_kind(i)[0] == True:
        print('Mängijal', nimed[j], 'on Four of a Kind')
        käed[j] = (8, kontrolli_four_of_a_kind(i)[1])
        
    elif kontrolli_straight(i)[0] == True:
        print('Mängijal', nimed[j], 'on Straight')
        käed[j] = (7, kontrolli_straight(i)[1])
    
    elif kontrolli_full_house(i)[0] == True:
        print('Mängijal', nimed[j], 'on Full House')
        käed[j] = (6, kontrolli_full_house(i)[1], kontrolli_full_house(i)[2])
    
    elif kontrolli_flush(i)[0] == True:
        print('Mängijal', nimed[j], 'on Flush')
        käed[j] = (5, kontrolli_flush(i)[1])
    
    elif kontrolli_three_of_a_kind(i)[0] == True:
        print('Mängijal', nimed[j], 'on Three of a Kind')
        käed[j] = (4, kontrolli_three_of_a_kind(i)[1])
    
    elif kontrolli_two_pairs(i)[0] == True:
        print('Mängijal', nimed[j], 'on Kaks Paari')
        käed[j] = (3, kontrolli_two_pairs(i)[1], kontrolli_two_pairs(i)[2])
    
    elif kontrolli_pair(i)[0] == True:
        print('Mängijal', nimed[j], 'on Paar')
        käed[j] = (2, kontrolli_pair(i)[1])
    
    elif kontrolli_high_card(i)[0] == True:
        print('Mängijal', nimed[j], 'on High Card')
        käed[j] = (1, kontrolli_high_card(i)[1])
print(käed)

leia_võitja(käed)





