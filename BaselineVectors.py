## BASELINE VECTOR DETERMINATION ##

import numpy as np
import sys, os
import itertools

class TelescopeModel():

    def __init__(self):

        self.txt_path = "antennae_coordinates.txt"
        self.input_dimensions = ""
        self.coord_matrix = None
        self.baseline_dict = {}
        
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
            file = open(os.path.join(sys.path[0], self.txt_path), "r")
        except:
            print("Text file could not be opened")
            file = []

        coord_list = []
        for i, line in enumerate(file):
            # Extract length dimension
            if line.startswith("Length dimension"):
                try:
                    dim = line[line.index('=')+2:].strip()
                    if dim == "m" or dim == "ft":
                        self.input_dimensions = dim
                    else:
                        print("Invalid length dimension")
                        break
                except:
                    print("Could not find length dimension")
            # Extract coordinates  
            elif line.startswith("Coordinates"):
                try:
                    line = line[line.index('=')+2:].split(' ')
                    for coord_str in line:
                        coord_str = coord_str.replace("(","").replace(")","")
                        x,y,z = coord_str.split(",")
                        coord = (int(x), int(y), int(z))
                        coord_list.append(coord)
                except:
                    print("Invalid coordinates")
                    coord_list = []
                    self.input_dimensions = ""
                    break   

        try:
            file.close()
        except:
            print("Text file could not be closed")

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
        # Convert feet to metres
        if self.input_dimensions == 'ft':
            self.coord_matrix = self.coord_matrix * 0.3048

    def calculateBaselineVectors(self):
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
            z = ant2[1][2] - ant1[1][2]
            self.baseline_dict[(i1,i2)] = (x,y,z)

telescope_model = TelescopeModel()
telescope_model.extractInputData()
telescope_model.convertCoordinates()
telescope_model.calculateBaselineVectors()
print(telescope_model.baseline_dict)