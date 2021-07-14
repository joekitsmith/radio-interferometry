## ANTENNA ARRAY ##

from source.antennae.single_antenna import SingleAntenna

class AntennaArray():

    def __init__(self):

        self.array_list = []

    def createTelescopeArray(self, input_units : list, input_coords : list):
        """    
        Creates an array of SingleAntenna objects from coordinate matrix and stores them in a list

        Parameters
        -------
        input_units: list
            units of dimensions in coordinate system
        input_coord : list
            list of lists containing coordinates of antenna in array

        Returns
        -------
        self.array_list : list
            list of SingleAntenna objects in array
        """
        array_list = []
        for coord in input_coords:
            antenna = SingleAntenna(input_units, coord)
            array_list.append(antenna)
        return(array_list)