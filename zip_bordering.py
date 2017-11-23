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
		for line in zips:#
			if str(line[0]) == str(zipcode) and str(line[1]) == str(dist):
				#print line[2:]
				return line[2:]
		print "this zip is still missing: " + str(zipcode)
		raise ValueError('')

def pull_from_hardcoded_coors(zipcode):
	with open("missing_coors.csv", "r") as file:
		coordinates = csv.reader(file)
		coor = []
		for line in coordinates:
			if str(line[0]) == str(zipcode):
				coor = line[1:3]
				coor[0] = float(coor[0])
				coor[1] = float(coor[1])
				print "just kidding, found them"
				return tuple(coor)	
		print "this coor is still missing: " + str(zipcode)
		raise ValueError('')

def get_radii(coor, event_zip):
	tfmile = [str(x).replace("<Zip: ", "").replace(">", "") for x in zp.isinradius(coor,25)]
	fifmile = [str(x).replace("<Zip: ", "").replace(">", "") for x in zp.isinradius(coor,50)]
	hundmile = [str(x).replace("<Zip: ", "").replace(">", "") for x in zp.isinradius(coor,100)]
	if len(hundmile) == 0:
		#string = raw_input("stop")
		tfmile = pull_from_hardcoded_zips(event_zip, 25)
		fifmile = pull_from_hardcoded_zips(event_zip, 50)
		hundmile = pull_from_hardcoded_zips(event_zip, 100)
	#print "25: \n" + str(tfmile)
	#print "fifty: \n" + str(fifmile)
	#print "hundred: \n" + str(hundmile)
	return tfmile, fifmile, hundmile


import csv
#with open("Shootings-data-10-31-2017-.csv", "r") as datafile, open("shootings_radius.csv", "a") as outputfile:
with open("zips.csv", "r") as datafile, open("shootings_radius1.csv", "a") as outputfile:
	data = csv.reader(datafile)
	output = csv.writer(outputfile)
	next(data, None) #skip labels
	for row in data:#every shooting
		date = row[1]
		#date = row[0]
		event_zip = row[2]
		if event_zip is '':
			print "missing event_zip"
			continue
		if len(event_zip) == 4:#missing leading zero
			event_zip = '0' + event_zip
		database = csv.reader(open("US Zip Codes from 2013 Government Data"))
		coor = []
		tfmile = []
		fifmile = []
		hundmile = []
		for entry in database:#loop through database until you get the coordinates
			if str(entry[0]) == str(event_zip):
				coor = entry[1:3]
				coor[0] = float(coor[0])
				coor[1] = float(coor[1])
				coor = tuple(coor)
				print event_zip
				print coor
				tfmile, fifmile, hundmile = get_radii(coor, event_zip)
				break
		if len(coor) == 0:
			print "no coordinates for " + str(event_zip)
			coor = pull_from_hardcoded_coors(event_zip)
			print coor
			#string = raw_input()
			tfmile, fifmile, hundmile = get_radii(coor, event_zip)
			
			
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
		#print "fifties and twenties"
		#print count
		#print "len(hhundreds)"
		#print len(hundmile)
		#print "hundreds"
		#print hundcount
