# variabel // untuk menampung nilai tipe data
nama = 'Haikal'
arr = []
num = nama

# looping
for i in range(10):
    print(i)

i = 0
while (True):
    if (i == 100):
        break
        
    print('ini while')
    
    i = i + 1

# operator logika
# """and""" # &&
if (True and True):
    print('ini and')

# """or""" # ||
if (True or False):
    print('ini or')
    
# """not""" # !
if (not False):
    print('ini not')

# Boolean dalam bentuk integer
# 0 = False
# 1 = True

# operator perbandingan (outputnya Boolean)
"""
== sama dengan
> lebih dari
< kurang dari
>= lebih dari sama dengan (2 statement)
<= kurang dari sama dengan (2 statement)
"""
print (10 == 1) # False
print (10 > 1) # True
print (10 < 1) # False
print (10 >= 12)
print (10 <= 12)
"""
12 >= 10
# 12 == 10 or 12 > 10
"""

# operator aritmatika
"""
+ tambah
- kurang
* kali
/ bagi
% modulus
** pangkat
"""
a = 12
print(a + 1)
print(a - 1)
print(a * 1)
print(a / 1)
print(12 % 10)
print(12 ** 3) # 12 * 12 * 12
print(12 // 10)

# operator assignment
a = 12 
print(a)

# a += 1 # a = a + 1 # a = 13
print(a)

# a -= 12 # a = a - 12 # a = 1
print(a)

# a *= 3 # a = a * 3 # a = 3
print(a)

# function

# function prosedur
def printNama():
    print('Haikal')
    
    
printNama()
myname = printNama()
    
# function return (fungsi)
def kembalikanNama():
    return 'Haikal'

myname = kembalikanNama()
print(myname)

def hello_world(name = 'tidak ada', age = 0, ukuran_baju = 'Tidak Ada'):    
    return 'Hello ' + name + ' umur ' + str(age) + ' ukuran baju ' + ukuran_baju

myname = hello_world('Haikal', 20, 'M')
print(myname)

"""
x = 2
f(x) = x + 1

f(2) = 2 + 1 = 3
"""

arr = [
    {
        'no': 1,
        'nama': 'Underground',
        'kelas': 'IF24A'
    },
    {
        'no': 2,
        'nama': 'Child Prone',
        'kelas': 'IF23C'
    }
]

for i in arr:
    print(str(i['no']) + ' ' + i['nama'] + ' ' + i['kelas'])