import zipcode as zp
entryzip = '84339'
myzip = zp.isequal(entryzip)
print "Zip code: " 
print entryzip
print myzip.state
print myzip.city
print myzip.to_dict()

coor = (41.640085, -111.935210)
print "within 10 miles:"
print zp.isinradius(coor, 10)
print "within 20 miles:"
print zp.isinradius(coor, 20)
print "within 50 miles:"
print zp.isinradius(coor, 50)
print "within 200 miles:"
print zp.isinradius(coor, 200)
