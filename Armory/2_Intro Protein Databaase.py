import biolib
import requests
import re

base_url = 'http://www.uniprot.org/uniprot/%s.txt'
pattern = 'DR\s{3}GO;\sGO:\d{7};\sP:'
with open('../dataset.txt', 'r') as ds:
    for line in ds:
        uniprot_data = requests.get(base_url % line.strip())
        prot_txt = uniprot_data.text
        data_list = prot_txt.split("\n")
        for _ in data_list:
            if re.search(pattern, _):
                print(_[23:].split(';')[0])