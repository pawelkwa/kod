a = 0
b = 2.34
a = b
text = 'abc'

if b > a:
    print ( 'b > a')
elif b == a:
    print('b = a')
else:
    print('b < a')
if b < a:
    print ('b < a')
else:
    print ('b > a')

result = a > b
print(type(result), result)

if text: #domyślnie text = true
    print ('text is not empty')

x = 1
y = 2
z = 3
if x < y < z:
    print('hurra')

#@ TODO: if 'a' < 'y' < 'z'


something = 'abc'
another = 'xyz'

if something == 'abc' and another == 'xyz':
    print('string are the same')


is_rest_equal_to_zero = 4 % 3
print(is_rest_equal_to_zero)

if not is_rest_equal_to_zero:
    print('the number is even')

name = 'Jan'
lastname = 'Kowalski'

#sprawdzenie czy liczna jest parzysta

digit = input ('podaj liczbe: ')
digit = int(digit)
reszta_dzielenia = digit % 2
print(reszta_dzielenia)
print(bool(reszta_dzielenia))
if not reszta_dzielenia:
    print('jest parzsta')
else:
    print('nie jest')


# if - if bool(text) - to robi i sprawdza czy jest prawda