# script to look at what urls are being shared

import sys;
import tldextract;

f = open("../data/fake_news_websites.txt");
lines = f.readlines();
dict_fake = {};

for line in lines:
    line = line.strip().lower();
    dict_fake[line] = 1;

# LC_ALL=C cut -f9 ../data/messages.tsv
for line in sys.stdin:
    line = line.strip();
#    line_split = line.split("\t");
    if(line=="" or len(line)<10):
        continue;
    res = tldextract.extract(line);
    domain = res.domain + '.' + res.suffix;
#    if(domain=="php."):
#        continue;
#    print domain;
    if(domain.lower() in dict_fake):
        print domain;
