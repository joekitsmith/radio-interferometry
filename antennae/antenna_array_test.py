## ANTENNA ARRAY TESTS ##

import unittest
import antenna_array

class CreateTelescopeArrayTest(unittest.TestCase):

    def test_createTelescopeArray_3MInputUnits3of3DIntCoordinates_Returns3ElementArrayList(self):
        input_units = ['m','m','m']
        input_coords = [[1,2,3], [4,5,6], [7,8,9]]
        array = antenna_array.AntennaArray()
        array_list = array.createTelescopeArray(input_units, input_coords)
        self.assertEqual(len(array_list), 3)

    def test_createTelescopeArray_2Ft1MInputUnits5Of5IntCoordinates_Returns5ElementArrayList(self):
        input_units = ['ft','ft','m']
        input_coords = [[1,2,3], [4,5,6], [7,8,9], [11,12,14], [18,19,20]]
        array = antenna_array.AntennaArray()
        array_list = array.createTelescopeArray(input_units, input_coords)
        self.assertEqual(len(array_list), 5)

    def test_createTelescopeArray_EmptyInputUnits3Of3IntCoordinates_ReturnsEmptyArrayList(self):
        input_units = []
        input_coords = [[1,2,3], [4,5,6], [7,8,9]]
        array = antenna_array.AntennaArray()
        array.createTelescopeArray(input_units, input_coords)
        self.assertEqual(array.array_list, [])

    def test_createTelescopeArray_3MInputUnitsEmptyCoordinates_ReturnsEmptyArrayList(self):
        input_units = ['m','m','m']
        input_coords = []
        array = antenna_array.AntennaArray()
        array.createTelescopeArray(input_units, input_coords)
        self.assertEqual(array.array_list, [])

    def test_createTelescopeArray_EmptyInputUnitsEmptyCoordinates_ReturnsEmptyArrayList(self):
        input_units = []
        input_coords = []
        array = antenna_array.AntennaArray()
        array.createTelescopeArray(input_units, input_coords)
        self.assertEqual(array.array_list, [])

if __name__ == '__main__':
    unittest.main()