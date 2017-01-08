#!/usr/bin/python
import RNA ##install viennaRNA python binding first
import httplib2
import json
import csv

##for each gene, grab 3' most 100nt for folding
with open("/home/rf/Desktop/genes.csv", "rb") as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
		genename = row[0]
		if genename!="":
			print genename

##grabing gene info and sequence
			try:
 			 from urlparse import urlparse
			except ImportError:
 			 from urllib.parse import urlparse

			headers = {
			 'Accept': 'application/json',
			}

			uri = 'http://rest.genenames.org'
			path = '/fetch/symbol/'

			target = urlparse(uri+path+genename)
			method = 'GET'
			body = ''

			h = httplib2.Http()

			response, content = h.request(
			 target.geturl(),
			 method,
			 body,
			 headers)

			if response['status'] == '200':
			 data = json.loads(content)
			 try:
				accnumstr = str(data['response']['docs'][0]['refseq_accession'])
 				refnum = accnumstr[3:-2]
			 except IndexError:
				print "not found"
				continue
			 accnumstr = str(data['response']['docs'][0]['refseq_accession'])
			 refnum = accnumstr[3:-2]
			 print refnum

			 ##using refseq number to get sequence
			 import urllib2
			 url2 = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id="
			 urlsetting = "&rettype=fasta&retmode=text"
			 target2 = (url2+refnum+urlsetting)
			 resp = urllib2.urlopen(target2)
			 page = resp.read()
			 page2 = str(page.split("\n",1)[1:])
			 page3 = page2[2:-2]
			 geneseq = (page3.replace("\\n",""))
			 print (geneseq)
 
			 threeseq=geneseq[-100:]
			 folded=RNA.fold(threeseq)
			 foldtrack=folded[0]
			 foldenergy=folded[1]

			 ##output to txt
			 foldout = "/home/rf/Desktop/fold.txt"
			 outfile = open(foldout, 'a')
			 outfile.write(genename+"\t"+refnum+"\t"+foldtrack+"\t"+str(foldenergy)+"\n")
			 outfile.close()

			else:
			 print 'Error detected: ' + response['status']
			 continue
