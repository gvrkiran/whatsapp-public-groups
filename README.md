# whatsapp-public-groups
Code to get data from WhatsApp public groups

## Pre-requisites

1. A standalone Android phone. A rooted android phone will make your life much much easier.
2. A mobile network connection - required to set up WhatsApp.
3. Internet connection - to keep receiving messages.

## Data collection pipeline

Step 1: Collect a list of public WhatsApp groups for the problem you want to study.
For instance, if you want to study how people have been using WhatsApp for job search, look for potential groups <a href="https://aileensoul.wordpress.com/2017/11/02/whatsapp-group-links-for-job-seekers/" target=_blank>here</a>.
We also provide a list of ~3,000 groups that we could find on Google by looking for urls containing "chat.whatsapp.com".

Step 2: Once you have the list of groups that you want to join, use the script `joinWhatsappGroups.py`.
The script uses a python library for browser automation called Selenium and simulates the process of joining the groups one by one using the web interface of WhatsApp (web.whatsapp.com).
A one-time user input is required to scan the QR code needed to log into WhatsApp on the browser.

* Note 1: If you have a small number of groups (say, 10), you can skip this step and do the joining manually.

* Note 2: We tried this script with only 178 groups. I am not sure if the script can handle a much larger set, like joining 1000 groups.

Step 3: Once

## Ethics note

The data collection process and the (anonymised) dataset provided here is only for research purposes.
