 #!/usr/bin/env python{"keys": ["alt+shift+f"], "command": "reindent", "args": {"single_line": false}}
import sys

ville={}
k=0
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    splits = line.split(",")
    if len(splits) == 5:
        userTel = splits[2]
        userDept = splits[3]

        if (str(userDept) == '78' ):
            userVille = splits[4]
            # on stock les villes et le userTel associé dans un dictionnaire ville  
            ville[k]=(userTel,userVille)
            k=k+1
        else: 
            continue


    else : 
        for i in ville.keys():
            # on teste si le userTel existe dans UserVers
            if ville[i][0]==splits[1]:
                print('%s,%s' % (ville[i][1],1))
            else:
                continue
