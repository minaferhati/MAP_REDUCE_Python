import sys, re
from collections import Counter
regex = re.compile('[^a-zA-Z]')


Users={}
list1=[]
cle=0
Villes={}
for line in sys.stdin:
    line = line.strip()
    splits = line.split(",")
    if len(splits) == 3:
        userTel=splits[2]
        userVille=splits[0]
        occ=splits[1]
        try: 
            occ=int(occ)
        except ValueError:
            continue 
#on stock dans un dictionnaire Users userTel,UserVille, nombre d'occurances
        Users[cle]=(userTel,userVille,occ)
        cle=cle+1
    else : 
        for k in Users.keys():
         #pour chaque UserTel on test s'il existe dans userVers
            if Users[k][0]==splits[0]:
                cle=Users[k][1]
                if cle in Villes.keys():
         #on incremente le nombre d'occurence
                    Villes[cle]=Villes[cle]+Users[k][2]
                else :
                    Villes[cle]=Users[k][2]
            else :
                continue 
#on affiche les villes having count>2
for k in Villes.keys():
    if Villes[k]>2 :
        print("%s,%s" % (k,Villes[k]))