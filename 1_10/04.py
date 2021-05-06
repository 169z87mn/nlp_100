aaaa = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
tori = [1, 5, 6, 7, 8, 9, 15, 16, 19]

result = {}

for i, o in enumerate(aaaa.replace('.', '').split(' '), start=1):
    c_s = o[:1] if i in tori else o[:2] 
    result.update({i: c_s})

print(result)
