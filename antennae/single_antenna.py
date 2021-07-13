## SINGLE ANTENNA ##

import math
from typing import List

class SingleAntenna():

    def __init__(self, input_units : list, coord : list):

        self.units = input_units
        self.coord = coord

        self.coord = self.convertLengthFtToM(self.coord)
        self.coord = self.convertLatLongAltToCartesian(self.coord)

    def convertLengthFtToM(self, coord : list) -> List:
        """    
        Identifies any coordinates present as feet and converts them to metres

        Parameters
        -------
        coord : list
            coordinates of antenna in original units

        Returns
        -------
        coord : list
            coordinates of antenna with feet converted to metres
        """
        ft_to_metres = 0.3048
        converted_coord = []
        if len(self.units) == len(coord):
            for i, unit in enumerate(self.units):
                if unit == 'ft':
                    metre_coord = coord[i] * ft_to_metres
                    converted_coord.append(metre_coord)
                else:
                    converted_coord.append(coord[i])
        return(converted_coord)

    def convertLatLongAltToCartesian(self, coord : list) -> List:
        """    
        Identifies if first two dimensions are in degrees and converts to cartesian if so

        Parameters
        -------
        coord : list
            cartesian or lat-long-alt coordinates of antenna 

        Returns
        -------
        coord : list
            cartesian coordinates of antenna
        """
        converted_coord = []
        if len(self.units) == len(coord):
            if self.units.count('d') == 2:
                if self.units[0] == 'd' and self.units[1] == 'd':
                    lat, long, alt = coord
                    lat, long = math.radians(lat), math.radians(long)
                    r = 6378137
                    alt = alt + r
                    x = alt * math.cos(lat) * math.sin(long)
                    y = alt * math.cos(lat) * math.cos(long)
                    z = alt * math.sin(lat)
                    converted_coord.extend([x,y,z])
            else:
                converted_coord.extend(coord)
        return(converted_coord)