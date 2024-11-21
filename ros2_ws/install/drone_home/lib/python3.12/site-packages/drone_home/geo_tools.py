import math
import numpy as np

class GeoTools:
    @staticmethod
    def get_bearing(lat1, lon1, lat2, lon2):
        dLon = (lon2 - lon1)

        y = math.sin(dLon) * math.cos(lat2)
        x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)

        brng = math.atan2(y, x)

        brng = np.rad2deg(brng)

        # north is 0 east is 90 west is -90
        # east is 0
        return brng + 90

    @staticmethod
    def geo_distance(lat1, lon1, lat2, lon2):
        """
        Calculate the distance between two points on the Earth's surface using the haversine formula.
        Returns distance in meters.
        """
        EARTH_RADIUS = 6371.0008 * 1000  # Earth radius in meters

        # Convert latitude and longitude from degrees to radians
        lat1_r = math.radians(lat1)
        lon1_r = math.radians(lon1)
        lat2_r = math.radians(lat2)
        lon2_r = math.radians(lon2)

        # Haversine formula
        dlat = lat2_r - lat1_r
        dlon = lon2_r - lon1_r
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1_r) * math.cos(lat2_r) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Distance in meters
        return EARTH_RADIUS * c
