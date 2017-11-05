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
with open("Shootings-data-10-31-2017-.csv", "r") as datafile, open("shootings_radius.csv", "a") as outputfile:
	data = csv.reader(datafile)
	output = csv.writer(outputfile)
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
			output_line =[date, zipcode, 1, 1, 1, event_zip] 
			print output_line
			output.writerow(output_line)
			count += 1
		for zipcode in fifmile:
			if zipcode not in tfmile:
				count += 1
				output_line = [date, zipcode, 0, 1, 1, event_zip] 
				output.writerow(output_line)
				print output_line
		hundcount = 0
		for zipcode in hundmile:
			if zipcode not in tfmile and zipcode not in fifmile:
				hundcount += 1
				output_line = [date, zipcode, 0, 0, 1, event_zip] 
				output.writerow(output_line)
				print output_line
		if flag is True:
			flag = False
		#print "fifties and twenties"
		#print count
		#print "len(hhundreds)"
		#print len(hundmile)
		#print "hundreds"
		#print hundcount
