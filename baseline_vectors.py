## BASELINE VECTOR DETERMINATION ##

import numpy as np
import sys, os
import itertools

class TelescopeModel():

    def __init__(self):

        self.txt_path = "antennae_coordinates.txt"
        self.input_dimensions = None
        self.coord_matrix = None
        self.baseline_dict = {}

        self.extractInputData()
        self.convertCoordinates()
        self.calculateBaselinePairs()
        
    def extractInputData(self):
        """
        Extracts coordinate values and length dimension of antennae distribution from text file

        Parameters
        -------
        self.txt_path : str 
            path to text file containing input data
        
        Returns
        -------
        self.input_dimensions : int
            length dimension of coordinates - m (metres) or ft (feet)
        self.coord_matrix : np.array
            2D numpy matrix containing cartesian coordinates of antennae

        """
        # Open text file from same directory
        try:
            text = open(os.path.join(sys.path[0], self.txt_path), "r")
        except:
            print("Text file could not be opened")
            text = []

        coord_list = []
        count = 0
        for i, line in enumerate(text):
            # Extract length dimension
            if line.startswith(">") and count == 0:
                count += 1
                dim = next(text).replace("\n", "")
                if dim == "m" or dim == "ft":
                    self.input_dimensions = dim
                else:
                    print("Invalid length dimension")
                    break
            # Extract coordinates  
            elif line.startswith(">") == False:
                try:
                    line = line.replace("\n", "")
                    x = line.split(",")[0].replace("(", "")
                    y = line.split(",")[1].replace(")", "")
                    coord = (int(x), int(y))
                except:
                    print("Invalid coordinates")
                    coord_list = []
                    break
                coord_list.append(coord)

        self.coord_matrix = np.array(coord_list)

    def convertCoordinates(self):
        """
        Converts coordinates to metres if in feet

        Parameters
        -------
        self.coord_matrix : np array
            2D numpy array containing antenna cartesian coordinates
        self.input_dimensions: str
            length dimension of coordinates - m (metres) or ft (feet)

        Returns
        -------
        self.coord_matrix : np.array
            2D numpy matrix containing antenna cartesian coordinates in metres
        """
        if self.input_dimensions == 'ft':
            self.coord_matrix = self.coord_matrix * 0.3048

    def calculateBaselinePairs(self):
        """
        Calculates baseline vectors for every pair of antennae in distribution

        Parameters
        -------
        self.coord_matrix : np array
            2D numpy array containing antenna cartesian coordinates
        
        Returns
        -------
        self.baseline_dict : dict
            dictionary with tuple of antenna pair indices as key and tuple of baseline vector as value
        """
        # Identify all combinations then calculate vector between each point
        comb_list = list(itertools.combinations(enumerate(self.coord_matrix), 2))
        for comb in comb_list:
            ant1 = comb[0]
            ant2 = comb[1]
            i1 = ant1[0]
            i2 = ant2[0]
            x = ant2[1][0] - ant1[1][0]
            y = ant2[1][1] - ant1[1][1]
            self.baseline_dict[(i1,i2)] = (x,y)

        print(self.baseline_dict)


TelescopeModel()