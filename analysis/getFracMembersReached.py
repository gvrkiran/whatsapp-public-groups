# script to get the fraction of members in each group reached by a message
# (on average)

import sys;
import numpy as np;

f = open("../data/group_ids_size.txt");
lines = f.readlines();
dict_size = {};

for line in lines:
    line = line.strip();
    line_split = line.split("\t");
    dict_size[line_split[1]] = float(line_split[0]);

x = [];
# LC_ALL=C cut -f2,29 ../data/messages.tsv
for line in sys.stdin:
    line = line.strip();
    line_split = line.split("\t");
    if(line_split[0] not in dict_size):
        continue;
#    print line_split[0] + "\t" + str(
    val = float(line_split[1])/dict_size[line_split[0]];
    if(val>1):
        val = 1;
    x.append(val);

print np.mean(x), np.median(x);
