# script to detect languages in the whatsapp data

# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from langdetect import detect;
import langid;
import numpy as np;
#import matplotlib.pyplot as plt;

count = 0;x = [];
#out = open("lang.txt","w");
# ../data/messages.tsv
for line in sys.stdin:
    line = line.strip();
    line_split = line.split("\t");
    group_id = line_split[1];
    text = line_split[6].strip();
    if(text==""):
        continue;
#    x.append(len(text));
#    try:
#    lang = detect(text);
    lang = langid.classify(text);
    print group_id + "\t" + lang[0];
#    out.write(lang + "\n");
#    except:
#        print >> sys.stderr, text, "fx";
#        pass;
#    count += 1;
#    if(count%100==0):
#        print count;
#out.close();

#print np.mean(x), np.median(x);

#plt.hist(x,100);
#plt.xlim(0,10000);
#plt.show();
