# script to get the number of the user who created a group

import sys,re,glob;
from bs4 import BeautifulSoup;

patt = re.compile("Created by \+[0-9\(\)\- ]+");

for infile in glob.glob("../group_data_html/*"):
#    print infile;
    f = open(infile);
    line = f.read().strip();
    admin_num = re.findall(patt,line)[0].replace("Created by ",""); 
    admin_num1 = admin_num.replace(" ","").replace("+","").replace("(","").replace(")","").replace("-","");

    soup = BeautifulSoup(line, "lxml");
    users = soup.find_all("span", class_="participant-text");
    tmp_str = "";
    for user in users:
        user = str(user);
        user = user.replace("<span class=\"participant-text\">","").replace("</span>","");
        tmp_str += user + ";";

    if(tmp_str==""):
        continue;

    print admin_num + "\t" + admin_num1 + "\t" + infile + "\t" + tmp_str;


#    break;

