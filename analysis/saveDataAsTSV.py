# file to save sqlite3 tables as TSV (tab separated) files.
# please edit the file names below before running the scripts.

import csv
import sqlite3

# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def to_utf8(lst):
    return [unicode(elem).encode('utf-8') for elem in lst]

data_folder = "WhatsApp/Databases/2017-10/"; # folder containing the sqlite3 database (msgstore.db file)
table_name = "chat_list"; # the table you want to dump as tsv.
fileid = "1";
data_folder_tsv = "WhatsApp/Databases/2017-10/" + table_name + "_" + fileid + ".tsv"; # output filename.

sqlite_file = data_folder + "msgstore" + fileid + ".db";

connection = sqlite3.connect(sqlite_file)  # open connection to your database
cursor = connection.cursor()  # get a cursor for it
cursor.execute("SELECT * FROM " + table_name)  # execute the query
rows = cursor.fetchall()  # collect the data

out = open(data_folder_tsv,"w");
for row in rows:
    tmp_str = "";
    for val in row:
        if(val is None):
            val = "";
        tmp_str += str(val).replace("\n"," ").replace("\t"," ") + "\t";
    tmp_str = tmp_str.strip("\t");
    out.write(tmp_str + "\n");

out.close();

"""
#rows = to_utf8(rows);
with open(data_folder_tsv, "w") as f:  # On Python 3.x use "w" mode and newline=""
    writer = csv.writer(f, delimiter="\t")  # create a CSV writer, tab delimited
    writer.writerows(rows)  # write your SQLite data
"""
