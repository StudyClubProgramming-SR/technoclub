# variabel itu apa sih?
# buat nampung tipe data yang ada di dalamnya

# primitif
'string' # string
3 # integer
0.5 # float
True # boolean
False # boolean

# ini tuh buat nyimpen nama
nama = 'Budi'

# comment inline

# comment multiline
"""
lorem ipsum dolor sit amet

dnaosdnoasnd

saya orang
"""

# collection
# list = array
arr = [1, 0.5, 'saya', True, False] # tipe data list
arr2 = arr

nama = arr[2]
print(nama)
try:
    print(arr[10])
except IndexError:
    print('ini kosong')
    
tuple = (1, 0.5, 'saya', True, False)

# dictionary = object
# key : value
obj = {
    'nama': 'Budi',
    'umur': 20,
    'alamat': 'Jl. ABC'
}
print(obj['nama'])
print(obj.get('umur'))