import random
import itertools

import pygame
from pygame.locals import *
from sys import exit


def kaardipakk():
    mastid = ('poti', 'risti', 'ärtu', 'ruutu')
    väärtus = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
    kaardipakk = []
    for i in väärtus:
        for j in mastid:
            kaardipakk.append((j, i))
    random.shuffle(kaardipakk)
    return kaardipakk

sõnastik = {}
# n arvule mängijatele käte genereerimine, formaadis ([käsi1], [käsi2], ...), välja jagatud kaardid eemaldatakse kaardipakist
def käed(mängijad, kaardipakk, nimed):
    käed = []
    for i in range(mängijad):
        x = random.sample(kaardipakk, 2)
        kaardipakk = eemalda(kaardipakk, x)
        käed.append(x)
        sõnastik[nimed[i]] = käed[i]
        print(nimed[i], 'sai kätte:', käed[i])
    print()
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

laual = []
# Lisab lauale riveri, eemaldab lisatud kaardid kaardipakist
def river(kaardipakk, laud):
    river = random.sample(kaardipakk, 1)
    for i in river:
        laud.append(i)
    kaardipakk = eemalda(kaardipakk, river)
    print('River oli:', river)
    print('Laual on nüüd:', laud)
    laual.append(laud)
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
    mitmes = 0
    for i in range(len(käed)):
        käed[i] = list(käed[i])
        käed[i].append(mitmes)       
        mitmes += 1
    for i in käed:
        if i[0] > suurim:
            suurim = i[0]
    for i in käed:
        if i[0] == suurim:
            võitjad.append(i)

    if len(võitjad) == 1:
        print('Mängu võitis:', nimed[käed.index(võitjad[0])])
        return(nimed[käed.index(võitjad[0])])
    #2 sama kätt
    elif len(võitjad) == 2:
        suurus = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        if type(võitjad[0][1]) == list:
            if võitjad[0][1] == võitjad[1][1]:
                print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], 'ja', nimed[võitjad[1][2]])
                return(nimed[võitjad[0][2]], nimed[võitjad[1][2]])
            else:
                suurim = -1
                w = []
                for i in võitjad[0][1]:
                    if suurim < suurus.index(i):
                        suurim = suurus.index(i)
                w.append(suurim)
                suurim = -1
                for i in võitjad[1][1]:
                    if suurim < suurus.index(i):
                        suurim = suurus.index(i)
                w.append(suurim)
                if w[0] > w[1]:
                    print('Mängu võitis:', nimed[võitjad[0][2]])
                    return(nimed[võitjad[0][2]])
                elif w[0] < w[1]:
                    print('Mängu võitis:', nimed[võitjad[1][2]])
                    return(nimed[võitjad[1][2]])
                else:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], 'ja', nimed[võitjad[1][2]])
                    return(nimed[võitjad[0][2]], nimed[võitjad[1][2]])

        else:
            suurus = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
            if len(võitjad[0]) == 3:
                if võitjad[0][1] == võitjad[1][1]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], 'ja', nimed[võitjad[1][2]])
                    return(nimed[võitjad[0][2]], nimed[võitjad[1][2]])
                elif suurus.index(võitjad[0][1]) > suurus.index(võitjad[1][1]):
                    print('Mängu võitis:', nimed[võitjad[0][2]])
                    return(nimed[võitjad[0][2]])
                elif suurus.index(võitjad[0][1]) < suurus.index(võitjad[1][1]):
                    print('Mängu võitis:', nimed[võitjad[1][2]])
                    return(nimed[võitjad[1][2]])

            elif len(võitjad[0]) == 4 and võitjad[0][0] == 7:
                if võitjad[0][1:3] == võitjad[1][1:3]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]], 'ja', nimed[võitjad[1][3]])
                    return(nimed[võitjad[0][3]], nimed[võitjad[1][3]])
                elif suurus.index(võitjad[0][1]) > suurus.index(võitjad[1][1]):
                    print('Mängu võitis:', nimed[võitjad[0][3]])
                    return(nimed[võitjad[0][3]])
                elif suurus.index(võitjad[0][1]) < suurus.index(võitjad[1][1]):
                    print('Mängu võitis:', nimed[võitjad[1][3]])
                    return(nimed[võitjad[1][3]])
                elif suurus.index(võitjad[0][1]) == suurus.index(võitjad[1][1]):
                    if suurus.index(võitjad[0][2]) > suurus.index(võitjad[1][2]):
                        print('Mängu võitis:', nimed[võitjad[0][3]])
                        return(nimed[võitjad[0][3]])
                    elif suurus.index(võitjad[0][2]) < suurus.index(võitjad[1][2]):
                        print('Mängu võitis:', nimed[võitjad[1][3]])
                        return(nimed[võitjad[1][3]])

            elif len(võitjad[0]) == 4 and võitjad[0][0] == 3:
                esimene = []
                teine = []
                
                for i in võitjad[0][1:3]:
                    esimene.append(suurus.index(i))
                    esimene.sort()
                    esimene.reverse()
                for i in võitjad[1][1:3]:
                    teine.append(suurus.index(i))
                    teine.sort()
                    teine.reverse()
                if esimene[0] > teine[0]:
                    print('Mängu võitis:', nimed[võitjad[0][3]])
                    return(nimed[võitjad[0][3]])
                elif esimene[0] < teine[0]:
                    print('Mängu võitis:', nimed[võitjad[1][3]])
                    return(nimed[võitjad[1][3]])
                elif esimene[0] == teine[0]:
                    if esimene[1] == teine[1]:
                        print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]], 'ja', nimed[võitjad[1][3]])
                        return(nimed[võitjad[0][3]], nimed[võitjad[1][3]])
                    elif esimene[1] > teine[1]:
                        print('Mängu võitis:', nimed[võitjad[0][3]])
                        return(nimed[võitjad[0][3]])
                    elif esimene[1] < teine[1]:
                        print('Mängu võitis:', nimed[võitjad[1][3]])
                        return(nimed[võitjad[1][3]])
    #kolm sama kätt
    elif len(võitjad) == 3:
        
        suurus = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        if type(võitjad[0][1]) == list:
            if võitjad[0][1] == võitjad[1][1] == võitjad[2][1]:
                print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], ',', nimed[võitjad[1][2]], 'ja', nimed[võitjad[2][2]])
                return(nimed[võitjad[0][2]], nimed[võitjad[1][2]], nimed[võitjad[2][2]])
            else:
                suurim = -1
                w = []
                for i in võitjad[0][1]:
                    if suurim < suurus.index(i):
                        suurim = suurus.index(i)
                w.append(suurim)
                suurim = -1
                for i in võitjad[1][1]:
                    if suurim < suurus.index(i):
                        suurim = suurus.index(i)
                w.append(suurim)
                for i in võitjad[2][1]:
                    if suurim < suurus.index(i):
                        suurim = suurus.index(i)
                w.append(suurim)
                if w[0] > w[1] and w[0] > w[2]:
                    print('Mängu võitis:', nimed[võitjad[0][2]])
                    return(nimed[võitjad[0][2]])
                elif w[1] > w[0] and w[1] > w[2]:
                    print('Mängu võitis:', nimed[võitjad[1][2]])
                    return(nimed[võitjad[1][2]])
                elif w[2] > w[0] and w[2] > w[1]:
                    print('Mängu võitis:', nimed[võitjad[2][2]])
                    return(nimed[võitjad[2][2]])
                elif w[0] == w[1]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], 'ja', nimed[võitjad[1][2]])
                    return(nimed[võitjad[0][2]], nimed[võitjad[1][2]])
                elif w[0] == w[2]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], 'ja', nimed[võitjad[2][2]])
                    return(nimed[võitjad[0][2]], nimed[võitjad[2][2]])
                elif w[1] == w[2]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[1][2]], 'ja', nimed[võitjad[2][2]])
                    return(nimed[võitjad[1][2]], nimed[võitjad[2][2]])
                else:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], ',', nimed[võitjad[1][2]], 'ja', nimed[võitjad[2][2]])
                    return(nimed[võitjad[0][2]], nimed[võitjad[1][2]], nimed[võitjad[2][2]])

        else:
            suurus = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
            if len(võitjad[0]) == 3:
                if võitjad[0][1] == võitjad[1][1] == võitjad[2][1]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], ',', nimed[võitjad[1][2]], 'ja', nimed[võitjad[2][2]])
                    return(nimed[võitjad[0][2]], nimed[võitjad[1][2]], nimed[võitjad[2][2]])
                w = []
                for i in range(3):
                    w.append(suurus.index(võitjad[i][1]))

                if w[0] > w[1] and w[0] > w[2]:
                    print('Mängu võitis:', nimed[võitjad[0][2]])
                    return(nimed[võitjad[0][2]])
                elif w[1] > w[0] and w[1] > w[2]:
                    print(nimed[võitjad[1][2]])
                    return(nimed[võitjad[1][2]])
                elif w[2] > w[0] and w[2] > w[1]:
                    print('Mängu võitis:', nimed[võitjad[2][2]])
                    return(nimed[võitjad[2][2]])
                elif w[0] == w[1]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], 'ja', nimed[võitjad[1][2]])
                    return(nimed[võitjad[0][2]], nimed[võitjad[1][2]])
                elif w[0] == w[2]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], 'ja', nimed[võitjad[2][2]])
                    return(nimed[võitjad[0][2]], nimed[võitjad[2][2]])
                elif w[1] == w[2]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[1][2]], 'ja', nimed[võitjad[2][2]])
                    return(nimed[võitjad[1][2]], nimed[võitjad[2][2]])
                else:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][2]], ',', nimed[võitjad[1][2]], 'ja', nimed[võitjad[2][2]])
                    return(nimed[võitjad[0][2]], nimed[võitjad[1][2]], nimed[võitjad[2][2]])

            elif len(võitjad[0]) == 4 and võitjad[0][0] == 7:
                kolmik = []
                for i in range(len(võitjad)):
                    kolmik.append(suurus.index(võitjad[i][1]))
                paar = []
                for i in range(len(võitjad)):
                    paar.append(suurus.index(võitjad[i][2]))
                if kolmik[0] == kolmik[1] == kolmik[2] and paar[0] == paar[1] == paar[2]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]] + ',', nimed[võitjad[1][3]], 'ja', nimed[võitjad[2][3]])
                    return(nimed[võitjad[0][3]], nimed[võitjad[1][3]], nimed[võitjad[2][3]])
                elif kolmik[0] > kolmik[1] and kolmik[0] > kolmik[2]:
                    print('Mängu võitis:', nimed[võitjad[0][3]])
                    return(nimed[võitjad[0][3]])
                elif kolmik[1] > kolmik[0] and kolmik[1] > kolmik[2]:
                    print('Mängu võitis:', nimed[võitjad[1][3]])
                    return(nimed[võitjad[1][3]])
                elif kolmik[2] > kolmik[0] and kolmik[2] > kolmik[1]:
                    print('Mängu võitis:', nimed[võitjad[2][3]])
                    return(nimed[võitjad[2][3]])
                elif kolmik[0] == kolmik[1] == kolmik[2]:
                    if paar[0] > paar[1] and paar[0] > paar[2]:
                        print('Mängu võitis:', nimed[võitjad[0][3]])
                        return(nimed[võitjad[0][3]])
                    elif paar[1] > paar[0] and paar[1] > paar[2]:
                        print('Mängu võitis:', nimed[võitjad[1][3]])
                        return(nimed[võitjad[1][3]])
                    elif paar[2] > paar[0] and paar[2] > paar[1]:
                        print('Mängu võitis:', nimed[võitjad[2][3]])
                        return(nimed[võitjad[2][3]])
                    elif paar[0] == paar[1]:
                        print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]], 'ja', nimed[võitjad[1][3]])
                        return(nimed[võitjad[0][3]], nimed[võitjad[1][3]])
                    elif paar[0] == paar[2]:
                        print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]], 'ja', nimed[võitjad[2][3]])
                        return(nimed[võitjad[0][3]], nimed[võitjad[2][3]])
                    elif paar[1] == paar[2]:
                        print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[1][3]], 'ja', nimed[võitjad[2][3]])
                        return(nimed[võitjad[1][3]], nimed[võitjad[2][3]])
                elif kolmik[0] == kolmik[1]:
                    if paar[0] == paar[1]:
                        print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]], 'ja', nimed[võitjad[1][3]])
                        return(nimed[võitjad[0][3]], nimed[võitjad[1][3]])
                    elif paar[0] > paar[1]:
                        print('Mängu võitis:', nimed[võitjad[0][3]])
                        return(nimed[võitjad[0][3]])
                    elif paar[0] < paar[1]:
                        print('Mängu võitis:', nimed[võitjad[1][3]])
                        return(nimed[võitjad[1][3]])
                elif kolmik[0] == kolmik[2]:
                    if paar[0] == paar[2]:
                        print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]], 'ja', nimed[võitjad[2][3]])
                        return(nimed[võitjad[0][3]], nimed[võitjad[2][3]])
                    elif paar[0] > paar[2]:
                        print('Mängu võitis:', nimed[võitjad[0][3]])
                        return(nimed[võitjad[0][3]])
                    elif paar[0] < paar[2]:
                        print('Mängu võitis:', nimed[võitjad[2][3]])
                        return(nimed[võitjad[2][3]])
                elif kolmik[1] == kolmik[2]:
                    if paar[1] == paar[2]:
                        print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[1][3]], 'ja', nimed[võitjad[2][3]])
                        return(nimed[võitjad[1][3]], nimed[võitjad[2][3]])
                    elif paar[1] > paar[2]:
                        print('Mängu võitis:', nimed[võitjad[1][3]])
                        return(nimed[võitjad[1][3]])
                    elif paar[1] < paar[2]:
                        print('Mängu võitis:', nimed[võitjad[2][3]])
                        return(nimed[võitjad[2][3]])
            elif len(võitjad[0]) == 4 and võitjad[0][0] == 3:
                esimene = []
                teine = []
                kolmas = []
                for i in võitjad[0][1:3]:
                    esimene.append(suurus.index(i))
                    esimene.sort()
                    esimene.reverse()
                for i in võitjad[1][1:3]:
                    teine.append(suurus.index(i))
                    teine.sort()
                    teine.reverse()
                for i in võitjad[2][1:3]:
                    kolmas.append(suurus.index(i))
                    kolmas.sort()
                    kolmas.reverse()
                if esimene[0] == teine[0] == kolmas[0] and esimene[1] == teine[1] == kolmas[1]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]] + ',', nimed[võitjad[1][3]], 'ja', nimed[võitjad[2][3]])
                    return(nimed[võitjad[0][3]], nimed[võitjad[1][3]], nimed[võitjad[2][3]])
                elif esimene[0] > teine[0] and esimene[0] > kolmas[0]:
                    print('Mängu võitis:', nimed[võitjad[0][3]])
                    return(nimed[võitjad[0][3]])
                elif esimene[0] < teine[0] and teine[0] > kolmas[0]:
                    print('Mängu võitis:', nimed[võitjad[1][3]])
                    return(nimed[võitjad[1][3]])
                elif kolmas[0] > esimene[0] and kolmas[0] > esimene[0]:
                    print('Mängu võitis:', nimed[võitjad[2][3]])
                    return(nimed[võitjad[2][3]])
                elif esimene[0] == teine[0] == kolmas[0]:
                    if esimene[1] > teine[1] and esimene[1] > kolmas[1]:
                        print('Mängu võitis:', nimed[võitjad[0][3]])
                        return(nimed[võitjad[0][3]])
                    elif esimene[1] < teine[1] and teine[1] > kolmas[1]:
                        print('Mängu võitis:', nimed[võitjad[1][3]])
                        return(nimed[võitjad[1][3]])
                    elif kolmas[1] > esimene[1] and kolmas[1] > teine[1]:
                        print('Mängu võitis:', nimed[võitjad[2][3]])
                        return(nimed[võitjad[2][3]])
                    elif esimene[1] == teine[1]:
                        print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]], 'ja', nimed[võitjad[1][3]])
                        return(nimed[võitjad[0][3]], nimed[võitjad[1][3]])
                    elif esimene[1] == kolmas[1]:
                        print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]], 'ja', nimed[võitjad[2][3]])
                        return(nimed[võitjad[0][3]], nimed[võitjad[2][3]])
                    elif teine[1] == kolmas[1]:
                        print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[1][3]], 'ja', nimed[võitjad[2][3]])
                        return(nimed[võitjad[1][3]], nimed[võitjad[2][3]])
                elif esimene[0] == teine[0]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]], 'ja', nimed[võitjad[1][3]])
                    return(nimed[võitjad[0][3]], nimed[võitjad[1][3]])
                elif esimene[0] == kolmas[0]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[0][3]], 'ja', nimed[võitjad[2][3]])
                    return(nimed[võitjad[0][3]], nimed[võitjad[2][3]])
                elif teine[0] == kolmas[0]:
                    print('Mäng jäi viiki, võitu jagavad:', nimed[võitjad[1][3]], 'ja', nimed[võitjad[2][3]])
                    return(nimed[võitjad[1][3]], nimed[võitjad[2][3]])
                
                
                


                
def mängijate_nimed(mängijate_arv):
    jär = []
    for i in range(mängijate_arv):
        tekst = 'Sisesta ' + str(i+1) + '. mängija nimi: '
        nimi = input(tekst)
        jär.append(nimi)
    return jär
        

            
        
        

# Mitu mängijat mängib?
mängijate_arv = input('Sisesta mängijate arv: ')
while True:
    try:
        mängijate_arv = int(mängijate_arv)
        break 
    except:
        print("Sisestatud pole korrektne arv. Proovi uuesti!")
        mängijate_arv = input('Sisesta mängijate arv: ')

mängijate_arv = kontrolli_mängijate_arvu(mängijate_arv, 3)

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
    
    elif kontrolli_full_house(i)[0] == True:
        print('Mängijal', nimed[j], 'on Full House')
        käed[j] = (7, kontrolli_full_house(i)[1], kontrolli_full_house(i)[2])
    
    elif kontrolli_flush(i)[0] == True:
        print('Mängijal', nimed[j], 'on Flush')
        käed[j] = (6, kontrolli_flush(i)[1])
        
    elif kontrolli_straight(i)[0] == True:
        print('Mängijal', nimed[j], 'on Straight')
        käed[j] = (5, kontrolli_straight(i)[1])
    
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

võit = leia_võitja(käed)
print(type(võit))

#mängijate kaardid kättesaadavaks
mängijate_kaardid = []
for nimi in nimed:
    kaardid = [nimi]
    for a in range(2):
        kaart = sõnastik[nimi][a][0] + str(sõnastik[nimi][a][1])
        kaardid.append(kaart)
    mängijate_kaardid.append(kaardid)




#pygame
pygame.init()

#põhi, tekstid
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Pokker")
pealkirjafont = pygame.font.Font("fondid/peen.ttf", 65)
pealkiri = pealkirjafont.render("Lauakaardid", True, (255, 255, 255))
tekstifont = pygame.font.Font("fondid/peen.ttf", 30)
võidufont = pygame.font.Font("fondid/peen.ttf", 70)

if type(võit) == str:
    tekst = 'Võitis: ' + võit
    võitja = võidufont.render(tekst, True, (255, 129, 129))
elif len(võit) == 2:
    tekst = 'Viik: ' + võit[0] + ' ja ' + võit[1]
    võitja = võidufont.render(tekst, True, (255, 129, 129))
elif len(võit) == 3:
    tekst = 'Viik: ' + võit[0] + ', ' + võit[1] + ' ja ' + võit[2]
    võitja = võidufont.render(tekst, True, (255, 129, 129))



#flop + turn + river
def lauakaart(k, w, h):
    kaart = k[0] + str(k[1])
    kaart = pygame.image.load('pildid/' + kaart + '.png')
    kaart = pygame.transform.scale(kaart, (100, 144.5))
    return screen.blit(kaart, (w, h))

#mängijate käed
def mängijakaart(k, w, h, i):
    kaart = k[i]
    kaart = pygame.image.load('pildid/' + kaart + '.png')
    kaart = pygame.transform.scale(kaart, (80, 115.6))
    return screen.blit(kaart, (w, h))

         
#mäng
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #taust            
    screen.fill((0, 100, 0))
    
    #pealkiri ja lauakaardid
    screen.blit(pealkiri, (320, 10))
    laius = 100
    for k in laual[0]:
        lauakaart(k, laius, 100)
        laius += 175
        
    #kaardid vastavalt mängijatele    
    if mängijate_arv == 2:
        laius = 220
        tekstilaius = 220
        for k in mängijate_kaardid:
            for i in range(1, 3):
                mängijakaart(k, laius, 400, i)
                laius += 100
            laius += 180
            tekst = tekstifont.render(k[0], True, "white")
            screen.blit(tekst, (tekstilaius, 515))
            tekstilaius += 380
    elif mängijate_arv == 3:
        laius = 130
        tekstilaius = 130
        for k in mängijate_kaardid:
            for i in range(1, 3):
                mängijakaart(k, laius, 400, i)
                laius += 100
            laius += 80
            tekst = tekstifont.render(k[0], True, "white")
            screen.blit(tekst, (tekstilaius, 515))
            tekstilaius += 280 
    elif mängijate_arv == 4:
        laius = 20
        tekstilaius = 20
        for k in mängijate_kaardid:
            for i in range(1, 3):
                mängijakaart(k, laius, 400, i)
                laius += 100
            laius += 60
            tekst = tekstifont.render(k[0], True, "white")
            screen.blit(tekst, (tekstilaius, 515))
            tekstilaius += 260
    
    #võitja
    screen.blit(võitja, (100, 267))

    pygame.display.update()
