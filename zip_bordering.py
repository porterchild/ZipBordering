import zipcode as zp
#entryzip = '84339'
#myzip = zp.isequal(entryzip)
#print "Zip code: " 
#print entryzip
#print myzip.state
#print myzip.city
#print myzip.to_dict()

#coor = (41.640085, -111.935210)
#print "within 10 miles:"
#print zp.isinradius(coor, 10)


import csv
data = csv.reader(open("Shootings-data-10-31-2017-.csv"))
next(data, None) #skip labels
for row in data:
	date = row[0]
	print date
	event_zip = row[2]
	if event_zip is None:
		continue
	database = csv.reader(open("US Zip Codes from 2013 Government Data"))
	for entry in database:
		if str(entry[0]) == str(event_zip):
			coor = entry[1:3]
			coor[0] = float(coor[0])
			coor[1] = float(coor[1])
			coor = tuple(coor)
			print event_zip
			print coor
			tfmile = [str(x).replace("<Zip: ", "").replace(">", "") for x in zp.isinradius(coor,25)]
			fifmile = [str(x).replace("<Zip: ", "").replace(">", "") for x in zp.isinradius(coor,50)]
			hundmile = [str(x).replace("<Zip: ", "").replace(">", "") for x in zp.isinradius(coor,100)]
			if len(hundmile) == 0:
				string = input("stop")
			print "25: \n" + str(tfmile)
			print "fifty: \n" + str(fifmile)
			print "hundred: \n" + str(hundmile)
			break
