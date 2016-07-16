import xml.etree.cElementTree as ET
import json
import xmltodict
from urllib.request import urlopen

file = urlopen('http://mozlnmiit.github.io/atom.xml')
data = file.read()
file.close()
data = xmltodict.parse(data)

with open('/home/sonali/Desktop/my_file.json', 'a') as f:
	json.dump(data,f)
