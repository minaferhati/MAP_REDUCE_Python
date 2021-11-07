#!/usr/bin/env python3

import sys, re
regex = re.compile('[^a-zA-Z]')
# input comes from STDIN (standard input)
for line in sys.stdin:

    userDept = "~"
    userTel = "~"
    userVille = "~"
    userVers = "~"

    # remove leading and trailing whitespace
    line = line.strip()
    splits = line.split(",")
    if len(splits) == 5:
        userTel = splits[2]
        userDept = splits[3]
        if (str(userDept) == '78') :
            userVille = splits[4]
#afficher le  userVille,UserTel
            print ("%s,%s,%s" % (userVille,1,userTel))
    else : 
        userVers = splits[1]
#afficher userVers
        print ("%s"% (userVers))

    
    
        

    

  



