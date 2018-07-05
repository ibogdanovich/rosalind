import biolib
import requests
import re

motif = 'N[^P][S|T][^P]'

with open('dataset.txt', 'r') as ds:
    ids = []
    uniprot_url = "http://www.uniprot.org/uniprot/{}.fasta"
    for line in ds:
        matches = []
        r = requests.get(uniprot_url.format(line.strip()))
        if r.status_code == requests.codes.ok:
            for name, seq in biolib.read_fasta_stream(r.text):
                for i in range(0, len(seq)-3):
                    if re.match(motif, seq[i:i+4]) != None:
                        matches.append(str(i+1))
            if len(matches) != 0:

                print(line.rstrip())
                print(' '.join(matches))
        else:
            print('Bad request')

