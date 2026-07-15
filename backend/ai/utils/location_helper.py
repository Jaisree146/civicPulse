from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2


class LocationHelper:

    EARTH_RADIUS = 6371000

    @staticmethod
    def distance(
        lat1,
        lon1,
        lat2,
        lon2
    ):

        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = (
            sin(dlat / 2) ** 2
            +
            cos(lat1)
            * cos(lat2)
            * sin(dlon / 2) ** 2
        )

        c = 2 * atan2(
            sqrt(a),
            sqrt(1 - a)
        )

        return (
            LocationHelper.EARTH_RADIUS * c
        )