#!/usr/bin/env python3
"""mapper.py"""

import sys
import json
# input comes from STDIN (standard input)
for line in sys.stdin:
    if line.strip():
        try:
            hon = 0
            hen = 0
            den = 0
            det = 0
            denna = 0
            denne = 0
            han = 0
            count = 0
            search_term1 = 'hon'
            search_term2 = 'hen'
            search_term3 = 'den'
            search_term4 = 'det'
            search_term5 = 'denna'
            search_term6 = 'denne'
            search_term7 = 'han'
            tweet = json.loads(line)
            if(tweet['retweeted']==False):
                current = tweet['text']
                if search_term1 in current:
                    hon = 1
                if search_term2 in current:
                    hen = 1
                if search_term3 in current:
                    den = 1
                if search_term4 in current:
                    det = 1
                if search_term5 in current:
                    denna = 1
                if search_term6 in current:
                    denne = 1
                if search_term7 in current:
                    han = 1
                print('%s\t%s' % (search_term1,hon))
                print('%s\t%s' % (search_term2,hen))
                print('%s\t%s' % (search_term3,den))
                print('%s\t%s' % (search_term4,det))
                print('%s\t%s' % (search_term5,denna))
                print('%s\t%s' % (search_term6,denne))
                print('%s\t%s' % (search_term7,han))
                print('count ',1)
except:
            continue
