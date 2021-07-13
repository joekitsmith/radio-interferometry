## DATA VALIDATOR ##

class DataValidator():

    def __init__(self):

        self.allowed_units = ['m', 'ft', 'd']

    def validateDimensionUnits(self, input_units : list) -> bool:
        """
        Checks if input dimension units match allowed units

        Parameters
        -------
        input_units : list 
            units of coordinates in input data
        self.allowed_units : list
            list of allowed units

        Returns
        -------
        is_valid : bool
            True if all input units match allowed units, otherwise False
        """
        pass_list = []
        for unit in input_units:
            if unit in self.allowed_units:
                pass_list.append(True)
            else:
                pass_list.append(False)
                print(f"{unit} not a valid unit. Valid units are m, ft and d for metres, feet and degrees")
        if pass_list == [True]*len(input_units) and len(input_units) != 0:
            is_valid= True
        else:
            is_valid = False
        return(is_valid)

    def validateDimensionCoordinateSystem(self, input_units : list) -> bool:
        """
        Checks if input coordinate system is of allowed type - i.e cartesian or lat-long-alt

        Parameters
        -------
        input_units : list 
            units of coordinates in input data
        
        Returns
        -------
        is_valid : bool
            True if zero or two degree units present, False otherwise
        """
        if input_units.count('d') == 0 or input_units.count('d') == 2:
            is_valid = True
        else:   
            is_valid = False
            print(f"Coordinate system not valid. Input must be all length (cartesian) or two degree units and one length unit (lat-long-alt)")
        return(is_valid)
        
    def validate3DCoordinates(self, coord : list) -> bool:
        """
        Checks if input coordinate contains 3 dimensions

        Parameters
        -------
        coord : list 
            list containing one set of coordinates from input data
        
        Returns
        -------
        is_valid : bool
            True if coordinates have 3 dimensions, False otherwise
        """
        if len(coord) == 3:
            is_valid = True
        else:
            print(f"{coord} is not a 3D coordinate")
            is_valid = False
        return(is_valid)

    def determineDataPass(self, input_units : list, coord_list : list) -> bool:
        """
        Runs all validation checks on input data and determines if it passes

        Parameters
        -------
        input_units : list 
            units of coordinates in input data
        coord_list : list of list
            list of list coordinates in input data
        
        Returns
        -------
        is_pass : bool
            True if all validation checks are successful, False otherwise
        """
        dim_pass_unit = self.validateDimensionUnits(input_units)
        dim_pass_sys = self.validateDimensionCoordinateSystem(input_units)
        dim_pass_3d = self.validate3DCoordinates(input_units)
        pass_list = [dim_pass_unit, dim_pass_sys, dim_pass_3d]
        for coord in coord_list:
            coord_pass_3d = self.validate3DCoordinates(coord)
            pass_list.append(coord_pass_3d)

        if pass_list == [True] * len(pass_list):
            is_pass = True
        else:
            is_pass = False
        return(is_pass)