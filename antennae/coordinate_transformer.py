## COORDINATE TRANSFORMER ##

import numpy as np
import math

class CoordinateTransformer():

    def convertLengthFtToM(self, units : list, coord : list) -> list:
        """    
        Identifies any coordinates present as feet and converts them to metres

        Parameters
        -------
        units : list
            units of dimensions in coordinate system
        coord : list
            coordinates of antenna in original units

        Returns
        -------
        coord : list
            coordinates of antenna with feet converted to metres
        """
        ft_to_metres = 0.3048
        converted_coord = []
        if len(units) == len(coord):
            for i, unit in enumerate(units):
                if unit == 'ft':
                    metre_coord = coord[i] * ft_to_metres
                    converted_coord.append(metre_coord)
                else:
                    converted_coord.append(coord[i])
        return(converted_coord)

    def convertLatLongAltToCartesian(self, units : list, coord : list) -> list:
        """    
        Identifies if first two dimensions are in degrees and converts to cartesian if so

        Parameters
        -------
        units : list
            units of dimensions in coordinate system
        coord : list
            cartesian or lat-long-alt coordinates of antenna 

        Returns
        -------
        coord : list
            cartesian coordinates of antenna
        """
        converted_coord = []
        if len(units) == len(coord):
            if units.count('d') == 2:
                if units[0] == 'd' and units[1] == 'd':
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

    def rotateCartesianCoordinateSystem(self, coord : np.array, rot_matrix : np.array) -> np.array:
        """
        Applies given rotation matirx to cartesian coordinate.
        
        Parameters
        -------
        coord : np.array
            input n-dimension cartesian coordinate to be rotated
        rotation_matrix: np.array
            square rotation matrix with n x n dimensions
        
        Returns
        -------
        coord_rot : np.array
            rotated n-dimension cartesian coordinate
        """
        coord_rot = np.array([])
        if coord.ndim == 1 and rot_matrix.ndim == 2:
            if coord.shape[0] == rot_matrix.shape[1]:
                coord_rot = rot_matrix.dot(coord)
        return(coord_rot)