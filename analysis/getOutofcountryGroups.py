# script to get the number of groups that have an out of country member

import matplotlib.pyplot as plt;
from pymining import itemmining;

f = open("../data/group_admins_members.txt");
lines = f.readlines();

dict_group_num_countries = {};

for line in lines:
    line = line.strip();
    line_split = line.split("\t");
    group_id = line_split[2].split("/")[-1];
    members = line_split[3].split(";");
    if(len(members)<100):
        continue;
    for member in members:
        member_country = member.split(" ")[0];
        if(member_country=="" or member_country=="You"):
            continue;
        if(group_id in dict_group_num_countries):
            tmp = dict_group_num_countries[group_id];
            tmp[member_country] = 1;
            dict_group_num_countries[group_id] = tmp;
        else:
            tmp = {};
            tmp[member_country] = 1;
            dict_group_num_countries[group_id] = tmp;

x = [];y = [];
count = 1;
val = [];
for keys in dict_group_num_countries.keys():
    if(len(dict_group_num_countries[keys].keys())>10):
        print keys;
    val.append(dict_group_num_countries[keys].keys());
    x.append(len(dict_group_num_countries[keys].keys()));
    count += 1;

#plt.hist(x,20);
#plt.xlabel("Number of countries per group",fontsize=18);
#plt.ylabel("Number of groups",fontsize=18);
#plt.savefig('groups_countries_hist.pdf');

#relim_input = itemmining.get_relim_input(val)
#report = itemmining.relim(relim_input, min_support=100)
#print report;
