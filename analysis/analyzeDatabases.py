# script  to process data that we decrypted from the whatsapp databases

import sys,sqlite3;

data_folder = "WhatsApp/Databases/2017-06/";

sqlite_file = data_folder + "msgstore1.db";

conn = sqlite3.connect(sqlite_file);
c = conn.cursor();

table_name = "chat_list";

c.execute('SELECT subject FROM {tn}'. format(tn=table_name))
all_rows = c.fetchall()

for row in all_rows:
    if(row[0] is not None):
        print row[0].encode('utf-8');

conn.close();
