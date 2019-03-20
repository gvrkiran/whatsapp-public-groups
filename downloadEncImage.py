#!/usr/bin/env python2
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import sys,glob,os,time;
from axolotl.kdf.hkdfv3 import HKDFv3
from axolotl.util.byteutil import ByteUtil
import binascii
import base64
from Crypto.Cipher import AES
import hashlib
import hmac


def decrypt(Url,MediaKey,filename,tipo):
	try:
		CipherData = urlopen(Url).read()
		CipherImage = CipherData[:-10]
		cryptKeys = getCryptKeys(tipo)

	#	SecretsRaw = HKDFv3().deriveSecrets(MediaKey, "WhatsApp Image Keys", 112)
		SecretsRaw = HKDFv3().deriveSecrets(MediaKey, binascii.unhexlify(cryptKeys), 112)
		Secrets = ByteUtil.split(SecretsRaw, 16, 32)
		iv = Secrets[0]
		CipherKey = Secrets[1]
		AES.key_size=128
		AESInstance = AES.new(key=CipherKey, mode=AES.MODE_CBC, IV=iv)
		PlainImage = AESInstance.decrypt(CipherImage)

		with open(filename, 'wb') as f:
			f.write(PlainImage)
			f.close()
		return "success";
	except:
		return;

def getCryptKeys(tipo):
	if tipo == "image":
		return '576861747341707020496d616765204b657973'
	if tipo == "audio" or tipo == "ptt":
		return '576861747341707020417564696f204b657973'
	if tipo == "video":
		return '576861747341707020566964656f204b657973'
	if tipo == "document" or tipo == "application":
		return '576861747341707020446f63756d656e74204b657973'
	return None


dict_urls = {};
count = 0;

for infile in glob.glob("whatsapp_files/*.txt"):
	fx = open(infile);
	linex = fx.read().strip().split(" ")[0];
	dict_urls[linex] = 1;
	count += 1;

#Url = "https://mmg-fna.whatsapp.net/d/f/Ao2eEj-oIAeK2rWeE7CUK11VLTB7s_5wsvuxvPOY3WBj.enc";
#MediaKey = "B52DC34D0DF63FCF99E8AB5B59694186134D5F089B885B982E9C7E7CFE54CA3F";

print >> sys.stderr, count;

#f = open("url_mediakey.txt");
f = open(sys.argv[1]);#open("/tmp/t");
lines = f.readlines();
dict_uniq = {};

for line in lines:
	line = line.strip();
	line_split = line.split(" ");
	if(len(line_split)<3):
		continue;
	url = line_split[0];
	if(url in dict_urls):
		continue;
	mediaExt = line_split[1].split("/")[-1].strip(";");
	mediaType = line_split[1].split("/")[0];
#	if(mediaType=="video"):
#		continue;
	if(mediaExt!="jpeg"): # only download images
		continue;
	mediaKey = line_split[-1]
	dict_uniq[url+ " " + mediaExt + " " + mediaKey] = 1;

print >> sys.stderr, len(dict_uniq.keys());

#for line in lines:
for keys in dict_uniq.keys():
	line = keys.strip();
	line_split = line.split(" ");
	if(len(line_split)<3):
		continue;
#	try:
	for idsf in range(1,2):
		url = line_split[0];
		mediaExt = line_split[1];#.split("/")[-1].strip(";");
		mediaKey = line_split[2];
		mediaKey = binascii.unhexlify(mediaKey)
		print line, mediaKey;
		count += 1;
		filename1 = "whatsapp_files1/" + str(count) + "." + mediaExt;
		filename2 = "whatsapp_files1/" + str(count) + ".txt";
		out = open(filename2,"w");
		out.write(line + "\n");
		out.close();
		return_val = decrypt(url,mediaKey,filename1,mediaType);
		print >> sys.stderr, count, mediaExt, return_val;
		if(return_val!="success"):
			continue;
		command1 = "file " + filename1 + " > /tmp/lfkas";
		os.system(command1);
		fx = open("/tmp/lfkas");
		linex = fx.read();
		print linex;
		if(linex.find("JPEG")==-1):
			command2 = "rm " + filename1;
			print >> sys.stderr, "failed", command2;
#			if(os.path.exists(filename1)):
#				os.system(command2);
	
	#	if(count>10):
	#		break;
#	except:
#		print >> sys.stderr, "faileeeeeeddd"
#		continue;
