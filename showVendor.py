#!/python33/python
#Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address
print ("Content-Type: text/html\n")

# author: Pawel Jurkiw
# email: 314275@uwr.edu.pl

import urllib.request as urllib2
import json
import codecs
import sys

#API base url,you can also use https if you need
url = "http://macvendors.co/api/"
reader = codecs.getreader("utf-8")

companies = []
count = []
macs = []

filename = str(sys.argv[1])
file = open(filename, 'r').read()
lines = file.split('\n')

for line in lines:
    #Mac address to lookup vendor from
    mac_address = line

    request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
    response = urllib2.urlopen( request )
    #Fix: json object must be str, not 'bytes'
    obj = json.load(reader(response))

    try:
        if obj['result']['company'] not in companies:
            companies.append(obj['result']['company'])
            count.append(1)
            macs.append(obj['result']['mac_prefix'])
        else:
            ind = companies.index(obj['result']['company'])
            count[ind] += 1
    except KeyError:
        print('Adres: ',mac_address,' nie zostal znaleziony w bazie i zostal pomieniety')

#SORTOWANIE BĄBELKOWE
k=0
while k < len(count)-1:
    j=0
    while j < len(count)-1:
        if count[j] < count[j+1]:
            tmp=count[j]
            count[j]=count[j+1]
            count[j+1]=tmp
            tmp2=companies[j]
            companies[j]=companies[j+1]
            companies[j+1]=tmp2
            tmp3=macs[j]
            macs[j]=macs[j+1]
            macs[j+1]=tmp3
        j += 1
    k += 1

for i in range(len(companies)):
    #Print company name
    print('Lp.:',i+1,'; Device count: ',count[i],'; Vendor name: ',companies[i],'; Vendor prefix:',macs[i]);
