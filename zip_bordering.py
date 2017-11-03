import zipcode as zp
#entryzip = '84339'
#myzip = zp.isequal(entryzip)
#print "Zip code: " 
#print entryzip
#print myzip.state
#print myzip.city
#print myzip.to_dict()
#print zp.isinradius(coor, 10)

def pull_from_hardcoded_zips(zipcode, dist):
	with open("missing_zips.csv", "r") as file:
		zips = csv.reader(file)
		for line in zips:
			if str(line[0]) == str(zipcode) and str(line[1]) == str(dist):
				#print line[2:]
				return line[2:]

import csv
data = csv.reader(open("Shootings-data-10-31-2017-.csv"))
output = csv.writer(open("shootings_radius.csv"))
next(data, None) #skip labels
for row in data:#every shooting
	flag = False
	date = row[0]
	event_zip = row[2]
	if event_zip is '':
		print "missing event_zip"
		continue
	database = csv.reader(open("US Zip Codes from 2013 Government Data"))
	for entry in database:
		if str(entry[0]) == str(event_zip):
			coor = entry[1:3]
			coor[0] = float(coor[0])
			coor[1] = float(coor[1])
			coor = tuple(coor)
			#print event_zip
			#print coor
			tfmile = [str(x).replace("<Zip: ", "").replace(">", "") for x in zp.isinradius(coor,25)]
			fifmile = [str(x).replace("<Zip: ", "").replace(">", "") for x in zp.isinradius(coor,50)]
			hundmile = [str(x).replace("<Zip: ", "").replace(">", "") for x in zp.isinradius(coor,100)]
			if len(hundmile) == 0:
				print event_zip
				#string = raw_input("stop")
				tfmile = pull_from_hardcoded_zips(event_zip, 25)
				fifmile = pull_from_hardcoded_zips(event_zip, 50)
				hundmile = pull_from_hardcoded_zips(event_zip, 100)
				flag = True
			#print "25: \n" + str(tfmile)
			#print "fifty: \n" + str(fifmile)
			#print "hundred: \n" + str(hundmile)
			break
	output_line = []
	count = 0
	for zipcode in tfmile:
		print [date, zipcode, 1, 1, 1, event_zip] 
		count += 1
	for zipcode in fifmile:
		if zipcode not in tfmile:
			count += 1
			print [date, zipcode, 0, 1, 1, event_zip] 
	hundcount = 0
	for zipcode in hundmile:
		if zipcode not in tfmile and zipcode not in fifmile:
			hundcount += 1
			print [date, zipcode, 0, 0, 1, event_zip] 
	if flag is True:
		flag = False
	#print "fifties and twenties"
	#print count
	#print "len(hhundreds)"
	#print len(hundmile)
	#print "hundreds"
	#print hundcount
