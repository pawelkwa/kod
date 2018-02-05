a = 7
b = 4
result = a // b #niejawna konwersja typów - robi intiger
print(result)

result1 = a / b
print(result1)

# @TODO:  Sprawdzić co oznacza '^'
c = 7
print('before', c)
c +=2
print('after', c)

#dzielenie z resztą

c = c % 2
print(c)

# teks z apostrofem - takie angielskie
text = 'Ala ma kota'
eng = "Tom's hause" #zamiast " moża użyć beckslesh - ESCAPING SHARACTERS
eng1 = 'Tom\'s hause'
print(eng, eng1)

#znaki ze stringu - string liczony jako całość - spacje są liczone i pozycje znaków liczne od 0
# minusowe indeksy - od tyłu od ostatniego znaku - -1, -2, -3

print(text[0]) #drukuje literke A z Ala ma kota
print(len(text))
#length = len(text)
#last_char = text[length] # tutaj pojawi się błąd o index poza rangą

przedzial = text[4:8] #prawa strona niedoknięta! czyli tak naprawdę do 7 znaku drukuje
print(przedzial)

przedzial1 = text[-4:-1]
print(przedzial1)
print(text)

przedzial_kroki = text[0:10:2]
print(przedzial_kroki)

#slice...?
dunno = text[0:15]
print(id(text))

text2 = text[::-1]  # odwrócenie stringa
print(text2)

# jak damy zmienną i kropkę to pojawi się różne podpowiedzi co można na stringi porobić - zamiana literek na duże i takie takie text.

# podmiana jedenej literki
# stringi są niemutowalne (niezmienialne) - STRING ARE IMMUTABLE
text_O = 'O' + text[1:] #zamieniami literki poprzez łączenie stribgów
print(text_O)

text3 = "Ala ma kota, kot bardzo lubi Ale"
old = 'kot'
new = 'pies'
text3_replaced = text3.replace(old, new)
print(text3)
print(text3_replaced)

print(text3, id(text3))
print(text3_replaced, id(text3_replaced))

count = 1
text31_replaced = text3.replace(old, new, count)

print(text31_replaced)