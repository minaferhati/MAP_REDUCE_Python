#!/usr/bin/env python
import sys

current_ville = None
current_count = 0
ville = None 

for line in sys.stdin: 
    line = line.strip()
    ville, count = line.split(',') 

    try: 
        count = int(count) 
    except ValueError:
        continue 

    # this IF-condition only works because Hadoop sorts map output by key (here: userVille) before it is passed to the reducer
    if current_ville == ville: 
        current_count += count
    else:
        if current_ville: 
            print ('%s\t%s' % (current_ville, current_count))
        current_count = count 
        current_ville = ville

if current_ville == ville: 
    # afficher les villes having count >2 et le nombre d'occurance 
    if current_count > 2:
        print ('%s\t%s' % (current_ville, current_count))

    