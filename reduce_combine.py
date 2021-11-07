import sys, re
from collections import Counter
regex = re.compile('[^a-zA-Z]')

Users={}
list1=[]
cle=0
Villes={}

#Récupérer ligne par ligne
for line in sys.stdin: 
    line = line.strip()
    splits= line.split(',') 
    champs_1=splits[0]
    champs_2=splits[1]
    # si le premier champs est un entier, donc on est sur la ligne qui contient (UserVers, occurence)
    if champs_1.isdigit() :
        userVers=champs_1
        occ_userVers=champs_2
        try: 
            occ_userVers=int(occ_userVers)
        except ValueError:
            continue 
        #On fait la jointure en comprant chaque UserTel avec UserVers
        for k in Users.keys():
        	if userVers == Users[k][0] :
        		ville= Users[k][1]
                #On affecte le nombre d'occurence de userVers à la ville 
        		if ville in Villes.keys(): 
        			Villes[ville]=Villes[ville]+ occ_userVers
        		else : 
        			Villes[ville]=occ_userVers
    #On est sur les lignes (UserVille, UserTel)
    else :
    	userVille=champs_1
    	userTel= champs_2
        #On stocke les couples dans un dictionnaire nommé Users
    	Users[cle]=(userTel,userVille)
    	cle=cle+1



for v in Villes.keys(): 
	print ('%s,%s' % (v, Villes[v]))
