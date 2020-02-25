#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, re, sys, json
from xml.etree import ElementTree as ET
from tabulate import tabulate

res = requests.get('https://maltworm.cz/dnes-na-cepu/', headers={'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
res.encoding = 'utf-8'
html = res.text

reg = re.compile('(<body.*</body>)', re.MULTILINE | re.DOTALL)
body = reg.search(html).group(0)
content = re.sub('<script.*</script>', '', body, flags=re.MULTILINE | re.DOTALL)

table = ET.XML(content)
articles = table.findall(".//article")

headers = ['Pivo', 'Typ', 'EPM', 'Alk.', 'IBU', 'Pivovar', 'Město']
output = []
for article in articles:
	beer = article.find(".//p[@class='elementor-heading-title elementor-size-default']")
	info = article.findall(".//span[@class='elementor-icon-list-text']")
	info = iter(info)
	values = [beer.text] + ["".join(i.itertext()) for i in info]

	# get rid of 'IBU:' prefix
	ibu_pos = headers.index('IBU')
	values[ibu_pos] = values[ibu_pos].replace('IBU:', '')

	output = output + [values]
	#print(dict(zip(headers, values)))

if len(sys.argv) > 1 and sys.argv[1] == 'json':
	print(json.dumps({'headers': headers, 'beers': output}, ensure_ascii=False))
else: 
	print(tabulate(output, headers=headers))
