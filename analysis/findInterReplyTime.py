# script to get, for the top 20 groups (in terms of number of messages sent) 
# the patterns of replies

import sys;
import numpy as np;
import matplotlib.pyplot as plt;
from datetime import datetime;
from operator import itemgetter;

def movingAverage(mylist):
	N = 5;
	cumsum, moving_aves = [0], []

	for i, x in enumerate(mylist, 1):
		cumsum.append(cumsum[i-1] + x)
    		if i>=N:
        	    moving_ave = (cumsum[i] - cumsum[i-N])/N
        	    #can do stuff with moving_ave here
        	    moving_aves.append(moving_ave)
	return moving_aves;

f = open("../data/groups_activity.txt");
lines = f.readlines();
dict_group_id = {};

for line in lines[:]:
    line = line.strip();
    line_split = line.split(" ");
    dict_group_id[line_split[1]] = 1;

dict_group_interreply = {};
dict_group_weekday = {};

# ../data/messages.tsv
for line in sys.stdin:
    line = line.strip();
    line_split = line.split("\t");
    timestamp = line_split[7];
    if(timestamp==""):
        continue;
    timestamp = int(timestamp)/1000.0;
    weekday = datetime.fromtimestamp(timestamp).strftime("%A");
    group_id = line_split[1];
    if(group_id not in dict_group_id):
        continue;
    if(group_id in dict_group_weekday):
        tmp = dict_group_weekday[group_id];
        tmp[weekday] += 1;
        dict_group_weekday[group_id] = tmp;
        
    else:
        tmp = {"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0};
        tmp[weekday] = 1;
        dict_group_weekday[group_id] = tmp;

    if(group_id in dict_group_interreply):
        dict_group_interreply[group_id].append(timestamp);
    else:
        dict_group_interreply[group_id] = [timestamp];

#sys.exit();
#print dict_group_interreply["573023350079-1481614301@g.us"][:20];

for group in dict_group_interreply.keys():
    reply_times = dict_group_interreply[group];
    tmp_lis = [];
    x = []; y = [];
    for i in range(len(reply_times)-1):
        diff = reply_times[i+1]-reply_times[i];
        if(diff < 0):
            continue;
#        x.append(i);
#        y.append(diff);
        tmp_lis.append(diff);

    
    y = movingAverage(tmp_lis);
    x = range(1,len(y)+1)

    break;
#    print group, min(tmp_lis), np.mean(tmp_lis), np.median(tmp_lis), max(tmp_lis);

"""
plt.plot(x,y);
plt.ylim(0,2000);
plt.xlim(0,1000);
plt.show();
"""

count = 1;
myticks = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'];

for group in dict_group_weekday.keys():
    x = [1,2,3,4,5,6,7]; y = [];
    sorted_x = sorted(dict_group_weekday[group].items(), key=itemgetter(1), reverse=True)
    print group + "\t" + sorted_x[0][0];
    """
    if(dict_group_weekday[group]["Wednesday"]>2000):
        continue;
    y.append(dict_group_weekday[group]["Monday"]);
    y.append(dict_group_weekday[group]["Tuesday"]);
    y.append(dict_group_weekday[group]["Wednesday"]);
    y.append(dict_group_weekday[group]["Thursday"]);
    y.append(dict_group_weekday[group]["Friday"]);
    y.append(dict_group_weekday[group]["Saturday"]);
    y.append(dict_group_weekday[group]["Sunday"]);
    plt.plot(x,y,'-*');
    plt.xticks(x, myticks, rotation=45);
    plt.xlabel('Weekday');
    plt.ylabel('Number of messages per day');
    plt.xlim(0,8);
    plt.tight_layout();
    plt.savefig('tmp/' + str(count) + ".png");
#    plt.close();
    count += 1;
    """
