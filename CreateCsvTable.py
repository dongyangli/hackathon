import argparse
import json
import ssl
import sys
import urllib2
import csv
import time
import os
import glob


#delete file of certain ages
def delete_aged_files():
	one_hour_ago = time.time() - 10 # make it shorter so far for testing
	folder = '.'
	os.chdir(folder)
	for f in glob.glob("*.csv"):
		st=os.stat(f)
		mtime=st.st_mtime
		if mtime < one_hour_ago:
			print('remove %s'%f)
			#os.unlink(f)

def request(securities, fields, startDate, endDate, periodicity):
	req = urllib2.Request('https://http-api.openbloomberg.com/request?ns=blp&service=refdata&type=HistoricalDataRequest')
	req.add_header('Content-Type', 'application/json')

	ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	ctx.load_verify_locations('bloomberg.crt')
	ctx.load_cert_chain('client.crt', 'client.key')

	try:
		data = {
			"securities" : securities,
			"fields": fields,
			"startDate": startDate,
			"endDate": endDate,
			"periodicitySelection": periodicity
		}

		res = urllib2.urlopen(req, data=json.dumps(data), context=ctx)
	except Exception as e:
		e
		print e
		return {}    
	return(json.loads(res.read()))

def createTable(securities, fields, startDate, endDate, periodicity):

	#delete_aged_files()

	result = request(securities, fields, startDate, endDate, periodicity)
	files = []
	for i in range(0, len(securities)):
		securityData = result['data'][i]['securityData']['fieldData']
		filename = securities[i]+'.csv'
		filename = filename.replace(" ", "_")
		files.append(filename)
		with open(filename, 'wb') as csvfile:
			writer = csv.writer(csvfile, delimiter=',')
			writer.writerow(fields)
			for data in securityData:
				row = []
				for field in fields:
					row.append(data[field])
				writer.writerow(row)

	return files

if __name__ == "__main__":
	securities = ["IBM US Equity", "AAPL US Equity"]
	fields = ["PX_LAST", "OPEN"]
	startDate = "20120101"
	endDate = "20120301"
	periodicity = "DAILY"

	createTable(securities, fields, startDate, endDate, periodicity)




