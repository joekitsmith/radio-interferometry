## BASELINE VECTOR DETERMINATION ##

import numpy as np
import sys, os
import itertools

class TelescopeModel():

    def __init__(self):

        self.txt_path = "antennae_coordinates.txt"
        self.input_dimensions = ""
        self.coord_matrix = None
        
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

telescope_model = TelescopeModel()
telescope_model.extractInputData()
telescope_model.convertCoordinates()