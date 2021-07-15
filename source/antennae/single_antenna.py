## SINGLE ANTENNA ##

import math
from typing import List
from source.transform.coordinate_transformer import CoordinateTransformer

class SingleAntenna():

    def __init__(self, input_units : list, coord : list):

        self.units = input_units
        self.coord = coord

        coord_trans = CoordinateTransformer()
        self.coord = coord_trans.convertLengthFtToM(self.units, self.coord)
        self.coord = coord_trans.convertLatLongAltToCartesian(self.units, self.coord)
        