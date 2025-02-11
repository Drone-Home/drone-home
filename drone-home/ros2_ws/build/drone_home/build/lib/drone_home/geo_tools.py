import math
import os
import numpy as np

class GeoTools:

    
    @staticmethod
    def get_bearing(lat1, lon1, lat2, lon2):
        """
        Returns bearing from one point to another using standard where east is 0
        """
        dLon = (lon2 - lon1)

        y = math.sin(dLon) * math.cos(lat2)
        x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)

        brng = math.atan2(y, x)

        brng = np.rad2deg(brng)

 
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

    @staticmethod
    def compute_tile_coordinate(latitude, longitude, zoom):
        MAX_ZOOM = 20
        """Compute tile coordinates for a given GPS point (latitude, longitude) and zoom level."""
        if zoom > MAX_ZOOM:
            raise ValueError(f"Zoom level {zoom} too high.")
        if latitude < -85.0511 or latitude > 85.0511:
            raise ValueError(f"Latitude {latitude} is out of bounds.")
        if longitude < -180 or longitude > 180:
            raise ValueError(f"Longitude {longitude} is out of bounds.")

        lat_rad = math.radians(latitude)
        n = 1 << zoom  # Equivalent to 2^zoom
        x = n * ((longitude + 180) / 360.0)
        y = n * (1 - (math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi)) / 2
        return x, y

    @staticmethod
    def euler_from_quaternion(quaternion):
        w = quaternion.w
        z = quaternion.z
        x = quaternion.x
        y = quaternion.y

        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
     
        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
     
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
     
        return roll_x, pitch_y, yaw_z # in radians
    
    @staticmethod
    def generate_kml(lat, lon, alt, heading, waypoints):
        #heading = 180
        kml_data = f"""<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>Vehicle Pose and Waypoints</name>
        
        <!-- Vehicle Pose -->
        <Placemark>
            <name>Vehicle Pose</name>
            <description>Vehicle position with updated pose.</description>
            <Point>
                <coordinates>{lon},{lat},{alt}</coordinates> <!-- Updated position -->
            </Point>
            <Style>
                <IconStyle>
                    <Icon>
                        <href>http://maps.google.com/mapfiles/kml/shapes/arrow.png</href> <!-- Default arrow icon -->
                    </Icon>
                    <heading>{heading}</heading> <!-- Updated heading/rotation -->
                </IconStyle>
            </Style>
        </Placemark>
        
        <!-- Waypoints -->
        """

        # Add waypoints to the KML data
        for lat, lon in waypoints:
            kml_data += f"""
        <Placemark>
            <name>Waypoint</name>
            <Point>
                <coordinates>{lon},{lat}</coordinates> <!-- Waypoint location -->
            </Point>
        </Placemark>
            """

        # Close the KML document
        kml_data += """
    </Document>
    </kml>"""
        
        # Write the KML data to a file
        file_path = os.path.expanduser('~/vehicle_pose.kml')
        with open(file_path, "w") as file:
            file.write(kml_data)
    @staticmethod
    def generate_kml2(lat, lon, alt, heading, waypoints):
        # Create KML structure for vehicle pose
        kml_data = f"""<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>Vehicle Pose and Waypoints</name>
        
        <!-- Vehicle Pose -->
        <Placemark>
            <name>Vehicle Pose</name>
            <description>Vehicle position with updated pose.</description>
            <Point>
                <coordinates>{lon},{lat},{alt}</coordinates> <!-- Updated position -->
            </Point>
            <Style>
                <IconStyle>
                    <Icon>
                        <href>http://maps.google.com/mapfiles/kml/shapes/arrow.png</href> <!-- Default arrow icon -->
                    </Icon>
                    <heading>{heading}</heading> <!-- Updated heading/rotation -->
                </IconStyle>
            </Style>
        </Placemark>
        
        <!-- Waypoints -->
        """

        # Add waypoints to the KML data
        for lat, lon in waypoints:
            kml_data += f"""
        <Placemark>
            <name>Waypoint</name>
            <Point>
                <coordinates>{lon},{lat}</coordinates> <!-- Waypoint location -->
            </Point>
        </Placemark>
            """

        # Close the KML document
        kml_data += """
    </Document>
    </kml>"""