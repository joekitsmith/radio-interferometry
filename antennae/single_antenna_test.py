## SINGLE ANTENNA TESTS ##

import unittest
import single_antenna

def checkListEqual(list_1, list_2, dec_places):
    """
    Check values in two lists are equal to defined number of decimal places. 
    Lists must be same length and contain only floats or integers
    """
    true_list = []
    for i, value in enumerate(list_1):
        diff = round(value, dec_places) - round(list_2[i], dec_places) 
        if diff == 0:
            true_list.append(True)
    if true_list == [True] * len(list_1):
        return(True)
    else:
        return(False)
        
class SingleAntennaConstructorTest(unittest.TestCase):

    def test_SingleAntennaConstructor_3MInputUnits3DIntCoordinates_CoordinatesUnchanged(self):
        input_units = ['m','m','m']
        input_coord = [1,2,3]
        antenna = single_antenna.SingleAntenna(input_units, input_coord)
        self.assertEqual(antenna.coord, [1,2,3])

    def test_SingleAntennaConstructor_2Ft1MInputUnits3DIntCoordinates_2ConvertedCoordinates(self):
        input_units = ['ft','ft','m']
        input_coord = [1,2,3]
        antenna = single_antenna.SingleAntenna(input_units, input_coord)
        output_coord = [0.3048, 0.6096, 3]
        self.assertEqual(antenna.coord, output_coord)

    def test_SingleAntennaConstructor_2D1MInputUnits3DIntCoordinates_LatLongAltConvertedToCartesian(self):
        input_units = ['d','d','m']
        input_coord = [45,45,100]
        antenna = single_antenna.SingleAntenna(input_units, input_coord)
        output_coord = [3189118.5000000, 3189118.5000000, 4510094.6347149]
        self.assertTrue(checkListEqual(output_coord, antenna.coord, 7))

    def test_SingleAntennaConstructor_2D1FtInputUnits3DIntCoordinates_LatLongAltConvertedToCartesianAndFtToM(self):
        input_units = ['d','d','ft']
        input_coord = [45,45,100]
        antenna = single_antenna.SingleAntenna(input_units, input_coord)
        output_coord = [3189083.7400000, 3189083.7400000, 4510045.4766515]
        self.assertTrue(checkListEqual(output_coord, antenna.coord, 7))

    def test_SingleAntennaConstructor_EmptyInputUnits3DIntCoordinates_EmptyCoord(self):
        input_units = []
        input_coord = [1,2,3]
        antenna = single_antenna.SingleAntenna(input_units, input_coord)
        self.assertEqual(antenna.coord, [])

    def test_SingleAntennaConstructor_3MInputUnitsEmptyCoordinates_EmptyCoord(self):
        input_units = ['m', 'm', 'm']
        input_coord = []
        antenna = single_antenna.SingleAntenna(input_units, input_coord)
        self.assertEqual(antenna.coord, [])

    def test_SingleAntennaConstructor_EmptyInputUnitsEmptyCoordinates_EmptyCoord(self):
        input_units = []
        input_coord = []
        antenna = single_antenna.SingleAntenna(input_units, input_coord)
        self.assertEqual(antenna.coord, [])

class ConvertLengthFtToMTest(unittest.TestCase):

    def test_convertLengthFtToM_3MInputUnits3DIntCoordinates_CoordinatesUnchanged(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = ['m','m','m']
        input_coord = [1,2,3]
        antenna.units = input_units
        coord = antenna.convertLengthFtToM(input_coord)
        self.assertEqual(coord, [1,2,3])

    def test_convertLengthFtToM_2Ft1MInputUnits3DIntCoordinates_2ConvertedCoordinates(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = ['ft','ft','m']
        input_coord = [1,2,3]
        antenna.units = input_units
        coord = antenna.convertLengthFtToM(input_coord)
        self.assertEqual(coord, [0.3048,0.6096,3])

    def test_convertLengthFtToM_2Ft1MInputUnits3DIntCoordinates_CoordinatesUnchanged(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = ['d','d','m']
        input_coord = [45,45,3]
        antenna.units = input_units
        coord = antenna.convertLengthFtToM(input_coord)
        self.assertEqual(coord, [45,45,3])

    def test_convertLengthFtToM_2D1FtInputUnits3DIntCoordinates_1ConvertedCoordinate(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = ['d','d','ft']
        input_coord = [45,45,3]
        antenna.units = input_units
        coord = antenna.convertLengthFtToM(input_coord)
        self.assertTrue(checkListEqual(coord, [45,45,0.9144], 4))

    def test_convertLengthFtToM_EmptyInputUnits3DIntCoordinates_EmptyCoordinates(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = []
        input_coord = [1,2,3]
        antenna.units = input_units
        coord = antenna.convertLengthFtToM(input_coord)
        self.assertEqual(coord, [])

    def test_convertLengthFtToM_3MInputUnitsEmptyCoordinates_EmptyCoordinates(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = ['m', 'm', 'm']
        input_coord = []
        antenna.units = input_units
        coord = antenna.convertLengthFtToM(input_coord)
        self.assertEqual(coord, [])

    def test_convertLengthFtToM_EmptyInputUnitsEmptyCoordinates_EmptyCoordinates(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = []
        input_coord = []
        antenna.units = input_units
        coord = antenna.convertLengthFtToM(input_coord)
        self.assertEqual(coord, [])

class ConvertLatLongAltToCartesianTest(unittest.TestCase):

    def test_convertLatLongAltToCartesian_3MInputUnits3DIntCoordinates_CoordinatesUnchanged(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = ['m','m','m']
        input_coord = [1,2,3]
        antenna.units = input_units
        coord = antenna.convertLatLongAltToCartesian(input_coord)
        self.assertEqual(coord, [1,2,3])

    def test_convertLatLongAltToCartesian_2D1MInputUnits3DIntCoordinates_LatLongAltConvertedToCartesian(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = ['d','d','m']
        input_coord = [45,45,100]
        antenna.units = input_units
        coord = antenna.convertLatLongAltToCartesian(input_coord)
        output_coord = [3189118.5000000, 3189118.5000000, 4510094.6347149]
        self.assertTrue(checkListEqual(coord, output_coord, 7))

    def test_convertLatLongAltToCartesian_EmptyInputUnits3DIntCoordinates_EmptyCoordinates(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = []
        input_coord = [1,2,3]
        antenna.units = input_units
        coord = antenna.convertLatLongAltToCartesian(input_coord)
       
    def test_convertLatLongAltToCartesian_3MInputUnitsEmptyCoordinates_EmptyCoordinates(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = ['m','m','m']
        input_coord = []
        antenna.units = input_units
        coord = antenna.convertLatLongAltToCartesian(input_coord)
        self.assertEqual(coord, [])

    def test_convertLatLongAltToCartesian_EmptyInputUnitsEmptyCoordinates_EmptyCoordinates(self):
        antenna = single_antenna.SingleAntenna([], [])
        input_units = []
        input_coord = []
        antenna.units = input_units
        coord = antenna.convertLatLongAltToCartesian(input_coord)
        self.assertEqual(coord, [])

if __name__ == '__main__':
    unittest.main()