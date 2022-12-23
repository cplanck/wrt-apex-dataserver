# convert UTM coordinates to global lat/longs
import utm

# format input as to_latlon(EASTING, NORTHING, ZONE)
# EASTING should have 6 digits, NORTHING should have 7 digits

# lat_multiplier = 100000
# long_multiplier = 10000


# # BELLOWS
# db_lat = 23.64193610
# db_long = 63.36393500
# zone_number = 4
# lat, long = utm.to_latlon(db_long*long_multiplier, db_lat*lat_multiplier, zone_number, northern=True)
# print('LAT LONG: {},{}'.format(lat,long))

# # ROBINSON
# db_lat = 38.50735550
# db_long = 56.24086500
# zone_number = 17
# lat, long = utm.to_latlon(db_long*long_multiplier, db_lat*lat_multiplier, zone_number, northern=True)
# print('LAT LONG: {},{}'.format(lat,long))

# CROFT
northing = 3860094.02
easting = 421135.66
zone_number = 17
lat, long = utm.to_latlon(easting, northing, zone_number, northern=True)
print('LAT LONG: {},{}'.format(lat,long))
