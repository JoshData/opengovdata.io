# Convert data into format for openheatmap.com.

import csv
from math import log

writer = csv.writer(open("data/output.csv", "w"))
writer.writerow(['label', 'value', 'lat', 'lon'])

# read in lat/long data
latlng = {}
for rec in csv.DictReader(open("data/google_transit/stops.txt")):
	latlng[rec["stop_id"]] = (rec["stop_lat"], rec["stop_lon"])
	
# print out coordinates of stops in the historical file in the same
# order as in the historical file
for rec in csv.DictReader(open("data/Historical Rail Ridership By Station.csv"), delimiter=' '):
	writer.writerow([
		rec['Station'],
		log(float(rec['2010'])/float(rec['2009'])),
		latlng[rec["gtfs_stop_id"]][0],
		latlng[rec["gtfs_stop_id"]][1]])

