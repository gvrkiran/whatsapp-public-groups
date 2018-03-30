import sys,glob,os;

count = 1;
for infile in glob.glob("../WhatsApp/encrypted/2017-10/*"):
    command = "python decrypt12.py key " + infile + " ../WhatsApp/Databases/2017-10/msgstore" + str(count) + ".db";
    print command;
    count += 1;
    os.system(command);
