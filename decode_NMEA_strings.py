# functions for handling NMEA GPS strings
import utm
import re


def lat_ddmm_to_decimal(lat):

    """ 
    Converts a latitude in format DDMM.MM... to a degree decimal format. 
    """

    lat_deg = float(lat[0:2])
    lat_min = float(lat[2:])/60
    decimal_lat = lat_deg+lat_min
    return decimal_lat

def long_dddmm_to_decimal(long):

    """ 
    Converts a longitude in format DDDMM.MM... to a degree decimal format. 
    """

    long_deg = float(long[0:3])
    long_min = float(long[3:])/60
    decimal_long = long_deg+long_min
    return decimal_long


def discover_gps_format(string):

    """
    Discovers the GPS format given a GPS string by examining the number of decimals after the latitude. If
    the number of decimals is 2, it assumes SLAM. If it's > 2, it assumes RTK.
    """

    split_string = string.split(',')
    
    raw_lat = split_string[2]
    split_lat = raw_lat.split('.')

    if len(split_lat[1]) == 2:
        return('SLAM')

    else:
        return('RTK')



def parse_RTK(string):

    """ 
    Parses data from a GNGGA string.
    Ex. string = "$GNGGA,014910.90,2120.75158442,N,15758.39210789,W,4,23,0.6,-10.720,M,15.015,M,0.9,0015*50"
    Also converts ddmm.mmmm format lat/longs to decimal lat/longs.
    """

    split_string = string.split(',')

    print(split_string)

    nmea_code = split_string[0]
    gps_hhmmss = float(split_string[1])
    raw_lat = split_string[2]
    lat_dir = split_string[3]
    raw_long = split_string[4]
    long_dir = split_string[5]

    lat = round(lat_ddmm_to_decimal(raw_lat),12)
    long = round(long_dddmm_to_decimal(raw_long),12)

    if lat_dir == 'S':
        lat = -lat
    if long_dir == 'W':
        long = -long

    return({'nmea_code': nmea_code, 'gps_hhmmss': gps_hhmmss, 'latitude': lat, 'longitude': long})


def parse_SLAM(string, zone):

    """
    Parses SLAM formatted GPS data from a GPS string.
    Ex. string = "$GPGGA,173351.82,3860198.47,N,421240.07,E,1,00,0.000,217.57,M,0.000,M,0.000,0001*45"
    Note: zone format is "zone_number + zone_letter", e.g, 32N
    Most zone_numbers are N, which I believe just means "norther"
    """

    split_string = string.split(',')

    print(split_string)

    nmea_code = split_string[0]
    gps_hhmmss = float(split_string[1])
    northing = float(split_string[2])
    easting = float(split_string[4])

    zone_num = int(re.findall('\d*', zone)[0])
    zone_letter = re.findall('\D', zone)[0]

    converted_lat, converted_long = utm.to_latlon(easting, northing, zone_num, zone_letter)

    return({'nmea_code': nmea_code, 'gps_hhmmss': gps_hhmmss, 'latitude': round(converted_lat,12), 'longitude': round(converted_long,12)})

# test cases
string = '$GNGGA,074501.50,5219.47015988,N,00447.36817686,E,4,24,0.6,-2.579,M,43.014,M,0.5,0029*76'
return_dict = parse_RTK(string)
print(return_dict)
print('https://www.google.com/maps/@{},{},9.99z'.format(return_dict['latitude'],return_dict['longitude']))


string = '$GNGGA,074552.50,5219.44766379,N,00447.35302713,E,4,26,0.6,-2.541,M,43.015,M,1.5,0029*7C'
return_dict = parse_RTK(string)
print(return_dict)
print('https://www.google.com/maps/@{},{},9.99z'.format(return_dict['latitude'],return_dict['longitude']))



