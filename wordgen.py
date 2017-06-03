#A password guessing tool for dictionary based attack
import itertools
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]
kunci=raw_input("masukan kata kunci: ").split()
maks=int(raw_input("Panjang maksimal: "))
while True:
     trig=raw_input("reverse all? (y/n): ")
     if trig=="y" or trig=="n":
        break
     print "goblok"
kunci=list(kunci)
rev=[]
if trig=="y":
     for i in kunci:
         rev.append(reverse(i))
     for i in rev:
         kunci.append(i)

words=[]
for i in range(len(kunci)+1):
    
    for c in itertools.combinations(kunci,i):
        words.append(''.join(c))
     
    for c in itertools.permutations(kunci,i):
        words.append(''.join(c))
    
 

words=[x for x in words if len(x)<=maks]
words=[x for x in words if len(x)>0]
daftar=[]
for i in words:
    if i not in daftar:
       daftar.append(i)
   
def capitalize(line):
    return ''.join(s[0].upper() + s[1:] for s in line.split())
kap=[]
for word in daftar:
    kap.append(capitalize(word))
print(len(daftar)+len(kap))  
kuwalik=[]
kuwalikap=[]

for k in daftar:
    kuwalik.append(reverse(k))
for k in kuwalik:
    kuwalikap.append(capitalize(k))
for k in kuwalik:
    if k not in daftar:
       daftar.append(k)
for k in kuwalikap:
    if k not in kap:
       kap.append(k)
        
f_file=open('words.txt','w')
for i in daftar:
    f_file.write(i+'\n')
for c in kap:
    f_file.write(c+'\n')
f_file.close()

        
