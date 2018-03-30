# whatsapp-public-groups

Code and dataset from our ICWSM 2018 dataset paper <b>WhatsApp, Doc? A First Look at WhatsApp Public Group Data</b>.

Code to get data from WhatsApp public groups.

The following repository contains details of the data collection and an anonymised version of the dataset.
For details, please refer to our <a href="https://users.ics.aalto.fi/kiran/content/whatsapp.pdf">paper</a>.

## Pre-requisites

1. A standalone Android phone. A rooted android phone will make your life much much easier.
2. A mobile network connection - required to set up WhatsApp.
3. Internet connection - to keep receiving messages.

## Data collection pipeline

Step 1: Collect a list of public WhatsApp groups for the problem you want to study.
For instance, if you want to study how people have been using WhatsApp for job search, look for potential groups <a href="https://aileensoul.wordpress.com/2017/11/02/whatsapp-group-links-for-job-seekers/" target=_blank>here</a>.
We also provide a list of ~3,000 groups that we could find on Google by looking for urls containing "chat.whatsapp.com".
These groups represent a pretty diverse set of topics which we mention in the paper, including: sports, politics, entertainment, job search, etc. You can use the file `getGroupTitles.py` to get the group titles for a set of groups.

Step 2: Once you have the list of groups that you want to join, use the script `joinWhatsappGroups.py`.
The script uses a python library for browser automation called Selenium and simulates the process of joining the groups one by one using the web interface of WhatsApp (web.whatsapp.com).
A one-time user input is required to scan the QR code needed to log into WhatsApp on the browser.

* Note 1: If you have a small number of groups (say, 10), you can skip this step and do the joining manually.

* Note 2: We tried this script with only 178 groups. I am not sure if the script can handle a much larger set, like joining 1000 groups.

Step 3: Once you join the groups, the data gets collected on the Android device. The data is stored on the device in an encrypted database. The next challenge is to decrypt the database and extract the messages. It is much much easier to decrypt the database if your phone is rooted. The process to follow is <a href="http://jameelnabbo.com/breaking-whatsapp-encryption-exploit/" target=_blank>here</a>. The process for unrooted Android phones is <a href="https://forum.xda-developers.com/showthread.php?t=2770982" target=_blank>here</a> and the code <a href="https://github.com/EliteAndroidApps/WhatsApp-Key-DB-Extractor" target=_blank>here</a> (We haven't tested these, and so can't vouch for them). We describe the process for rooted phones below:

* The decrypted database is stored in a path that looks like this: `Device Storage/WhatsApp/Databases`, containing a filename `msgstore.db.crypt12`

* Note that we recommend using a stand-alone phone that only can be used for this data collection, since rooting your phone is <a href="https://www.bullguard.com/bullguard-security-center/mobile-security/mobile-threats/android-rooting-risks.aspx target=_blank"> not a great idea</a>.

* After you have rooted your phone, following the tons of tutorials available online, you can look for the decryption key on your phone.

* WhatsApp saves this key in your system storage. To open the system folder you can use an app such as ES File Explorer. Look for ES File Explorer File Manager – Android Apps on Google Play.

* Navigate to the location `/data/data/com.whatsapp/files/key` on the file explorer app.

* Copy the `key` file to a convenient location. This is the decryption key.

* Then use the code in the `WhatsApp-Crypt12-Decrypter` folder to decrypt the database. Copy the `key` file to this folder.
The WhatsApp-Crypt12-Decrypter code was obtained (and slightly modified) from <a href="https://github.com/EliteAndroidApps/WhatsApp-Crypt12-Decrypter/" target=_blank>here</a>.

* Use the `decrypt12.py`. It takes the key file and the encrypted database as input. `python decrypt12.py key msgstore.db.crypt12 msgstore.db`. The decrypted database is stored in the file named `msgstore.db`.

* If you reached till here, Congrats! Almost done! The file msgstore.db is a simple sqlite3 database which can be manipulated programmatically. You can browse the contents using a database browsing tool like <a href="http://sqlitebrowser.org/">DB Browser for SQLite</a> (on Linux, Mac and Windows). You can export the contents of the database to a tsv file using the file `saveDataAsTSV.py`. 

## Data
The dataset contains anonymised information.

## Contact

For any questions regarding the data collection or the dataset itself, please contact Kiran Garimella (kiran.garimella@epfl.ch) or Gareth Tyson (gareth.tyson@qmul.ac.uk).

## Ethics note

* The data collection process and the (anonymised) dataset provided here are only for research purposes.

* Please understand what you are doing before doing any of the stuff mentioned above.

* Use the tools mentioned above at your own risk. We do not take any responsibility.
