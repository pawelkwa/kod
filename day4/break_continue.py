counter = 0
value = input('Podaj liczbę: ')
value = int(value)
# @TODO: wyświetl na ekran wartość counter
# @TODO: wyświetl tylko jesli counter jest nieparzysty
while counter < value:  # wartość inputa jest zmienną str
    if counter % 2:
        print(counter)
        counter += 1
    elif value > 1000:  # do zwrócenia uwagi na wartość początkową countera - parzysta/nieparzysta
        break
    else:
        counter += 1
        continue
print('bye')