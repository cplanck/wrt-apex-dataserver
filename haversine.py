import math as m

def haversine_formula(lat1, long1, lat2, long2):

    """ Calculate the distance between two lat/longs on a globe
    Reference here: https://www.movable-type.co.uk/scripts/latlong.html
    """

    R = 6371000

    phi1 = lat1 * m.pi/180
    phi2 = lat2 * m.pi/180 

    dphi = (lat2 - lat1) * m.pi/180
    dlam = (long2 - long1) * m.pi/180

    a = m.sin(dphi/2)**2 + m.cos(dphi)*m.cos(phi2)*(m.sin(dlam/2)**2)
    c = m.atan2(m.sqrt(a), m.sqrt(1-a))

    distance = R * c # distance in meters

    return(round(distance,3))


lat1 = 38.60186090
long1 = 42.12362500
lat2 = 38.60198150
long2 = 42.12410100

distance  = haversine_formula(lat1, long1, lat2, long2)

print(distance)


183621.080
183603.480

int(183603.480)