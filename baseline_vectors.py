## BASELINE VECTOR DETERMINATION ##

import itertools
from text_parser.file_reader import FileReader
from text_parser.coordinate_extractor import CoordinateExtractor
from text_parser.data_validator import DataValidator
from antennae.antenna_array import AntennaArray

class BaselineVectorCalculator():
    
    def __init__(self):

        self.baseline_dict = {}

    def calculateBaselineVector(self, coord_1 : list, coord_2 : list) -> list:
        """    
        Calculate vector between two cartesian coordinates

        Parameters
        -------
        coord_1 : list
            cartesian coordinates of antenna 1
        coord_2: list
            cartesian coordinates of antenna 2

        Returns
        -------
        vector : list
            3D vector connecting antenna 1 and 2
        """
        vector = []
        if len(coord_1) == len(coord_2):
            for i, dim in enumerate(coord_2):
                dim_diff = dim - coord_1[i]
                vector.append(dim_diff)
        return(vector)

    def determineBaselineVectorsOfArray(self, array_list: list):
        """
        Calculates baseline vectors for every pair of antennae in distribution

        Parameters
        -------
        array_list : list
            list of SingleAntenna objects in array
        
        Returns
        -------
        self.baseline_dict : dict
            dictionary with antenna pair indices as keys and baseline vector as values
        """
        comb_list = list(itertools.combinations(enumerate(array_list), 2))
        for comb in comb_list:
            coord_1 = comb[0][1].coord
            coord_2 = comb[1][1].coord
            index_1 = comb[0][0]
            index_2 = comb[1][0]
            vector = self.calculateBaselineVector(coord_1, coord_2)
            self.baseline_dict[(index_1, index_2)] = vector

    def displayBaselineVectors(self):
        """
        Prints baseline vectors for each antennae pair in separate statements

        Parameters
        -------
        self.baseline_dict : dict
            dictionary with antenna pair indices as keys and baseline vector as valuesself.array_list : list
        """
        for index_pair, vector in self.baseline_dict.items():
            print(f"Baseline vector in metres between antennae {index_pair[0]+1} and {index_pair[1]+1} is {vector}.")

if __name__ == '__main__':
    parser = FileReader()
    text = parser.extractText("input_coordinates.txt")

    coord_extractor = CoordinateExtractor()
    input_units = coord_extractor.extractCoordinateListFromText('Units =', text)[0]
    input_coords = coord_extractor.extractCoordinateListFromText('Coordinates =', text)

    data_validator = DataValidator()
    overall_pass = data_validator.determineDataPass(input_units, input_coords)

    if overall_pass == True:
        antenna_array = AntennaArray()
        antenna_array.array_list = antenna_array.createTelescopeArray(input_units, input_coords)

        baseline_vector_calc = BaselineVectorCalculator()
        baseline_vector_calc.determineBaselineVectorsOfArray(antenna_array.array_list)
        baseline_vector_calc.displayBaselineVectors()