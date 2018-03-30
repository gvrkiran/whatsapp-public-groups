from operator import itemgetter;

f = open("lang_group.txt");
lines = f.readlines();
dict_group = {};
dict_num_messages = {};

for line in lines:
    line = line.strip();
    line_split = line.split("\t");
    group = line_split[0];
    lang = line_split[1];

    if(group in dict_num_messages):
        dict_num_messages[group] += 1;
    else:
        dict_num_messages[group] = 1;

    if(group in dict_group):
        tmp = dict_group[group];
        if(lang in tmp):
            tmp[lang] += 1;
        else:
            tmp[lang] = 1;
        dict_group[group] = tmp;
    else:
        tmp = {};
        tmp[lang] = 1;
        dict_group[group] = tmp;

for keys in dict_group.keys():
    num_messages = dict_num_messages[keys];
    dict_countries = dict_group[keys];
    sorted_x = sorted(dict_countries.items(), key=itemgetter(1), reverse=True)
    try:
        x1 = sorted_x[0][1]*1.0/num_messages;
        x2 = sorted_x[1][1]*1.0/num_messages;

        print keys + "\t" + str(x1) + "\t" + str(x2);#str(len(dict_group[keys].keys()));
    except:
        pass;
