import sys, re
from collections import Counter
regex = re.compile('[^a-zA-Z]')
#calcul d'occurance de chaque userVers:
current_userVers= None
current_count=0
for line in sys.stdin: 
    line = line.strip()
    splits= line.split(',') 
    if len(splits)==1 :
        userVers=splits[0]


        if current_userVers == userVers: 
            current_count += 1
        else : 
            if current_userVers: 
                print ('%s,%s' % (current_userVers, current_count))
            current_count = 1
            current_userVers= userVers
    else :
        userTel=splits[2]
        userVille=splits[0]
#afficher la userVille et userTel
        print ('%s,%s' % (userVille,userTel))
            
#afficher  userVers et son occurance 
if current_userVers == userVers: 
    print ('%s,%s' % (current_userVers, current_count))
