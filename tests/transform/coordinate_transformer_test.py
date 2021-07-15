## ROTATION MATRIX ##

import unittest
import numpy as np
from source.transform.coordinate_transformer import CoordinateTransformer

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

class ConvertLengthFtToMTest(unittest.TestCase):

    def test_convertLengthFtToM_3MInputUnits3DIntCoordinates_CoordinatesUnchanged(self):
        input_units = ['m','m','m']
        input_coord = [1,2,3]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLengthFtToM(input_units, input_coord)
        self.assertEqual(converted_coord, [1,2,3])

    def test_convertLengthFtToM_2Ft1MInputUnits3DIntCoordinates_2ConvertedCoordinates(self):
        input_units = ['ft','ft','m']
        input_coord = [1,2,3]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLengthFtToM(input_units, input_coord)
        self.assertEqual(converted_coord, [0.3048,0.6096,3])

    def test_convertLengthFtToM_2Ft1MInputUnits3DIntCoordinates_CoordinatesUnchanged(self):
        input_units = ['d','d','m']
        input_coord = [45,45,3]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLengthFtToM(input_units, input_coord)
        self.assertEqual(converted_coord, [45,45,3])

    def test_convertLengthFtToM_2D1FtInputUnits3DIntCoordinates_1ConvertedCoordinate(self):
        input_units = ['d','d','ft']
        input_coord = [45,45,3]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLengthFtToM(input_units, input_coord)
        self.assertTrue(checkListEqual(converted_coord, [45,45,0.9144], 4))

    def test_convertLengthFtToM_EmptyInputUnits3DIntCoordinates_EmptyCoordinates(self):
        input_units = []
        input_coord = [1,2,3]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLengthFtToM(input_units, input_coord)
        self.assertEqual(converted_coord, [])

    def test_convertLengthFtToM_3MInputUnitsEmptyCoordinates_EmptyCoordinates(self):
        input_units = ['m', 'm', 'm']
        input_coord = []
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLengthFtToM(input_units, input_coord)
        self.assertEqual(converted_coord, [])

    def test_convertLengthFtToM_EmptyInputUnitsEmptyCoordinates_EmptyCoordinates(self):
        input_units = []
        input_coord = []
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLengthFtToM(input_units, input_coord)
        self.assertEqual(converted_coord, [])

class ConvertLatLongAltToCartesianTest(unittest.TestCase):

    def test_convertLatLongAltToCartesian_3MInputUnits3DIntCoordinates_CoordinatesUnchanged(self):
        input_units = ['m','m','m']
        input_coord = [1,2,3]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLatLongAltToCartesian(input_units, input_coord)
        self.assertEqual(converted_coord, [1,2,3])

    def test_convertLatLongAltToCartesian_2D1MInputUnits3DIntCoordinates_LatLongAltConvertedToCartesian(self):
        input_units = ['d','d','m']
        input_coord = [45,45,100]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLatLongAltToCartesian(input_units, input_coord)
        output_coord = [3189118.5000000, 3189118.5000000, 4510094.6347149]
        self.assertTrue(checkListEqual(converted_coord, output_coord, 7))

    def test_convertLatLongAltToCartesian_2D1MInputUnits90Lat0Long100Alt_OnlyZCartesian(self):
        input_units = ['d','d','m']
        input_coord = [90,0,100]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLatLongAltToCartesian(input_units, input_coord)
        output_coord = [0,0,6378237]
        self.assertTrue(checkListEqual(converted_coord, output_coord, 7))

    def test_convertLatLongAltToCartesian_2D1MInputUnits0Lat0Long0Alt_OnlyYCartesian(self):
        input_units = ['d','d','m']
        input_coord = [0,0,100]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLatLongAltToCartesian(input_units, input_coord)
        output_coord = [0,6378237,0]
        self.assertTrue(checkListEqual(converted_coord, output_coord, 7))

    def test_convertLatLongAltToCartesian_2D1MInputUnits0Lat0Long0Alt_OnlyXCartesian(self):
        input_units = ['d','d','m']
        input_coord = [0,90,100]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLatLongAltToCartesian(input_units, input_coord)
        output_coord = [6378237,0,0]
        self.assertTrue(checkListEqual(converted_coord, output_coord, 7))

    def test_convertLatLongAltToCartesian_EmptyInputUnits3DIntCoordinates_EmptyCoordinates(self):
        input_units = []
        input_coord = [1,2,3]
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLatLongAltToCartesian(input_units, input_coord)
        self.assertEqual(converted_coord, [1,2,3])
       
    def test_convertLatLongAltToCartesian_3MInputUnitsEmptyCoordinates_EmptyCoordinates(self):
        input_units = ['m','m','m']
        input_coord = []
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLatLongAltToCartesian(input_units, input_coord)
        self.assertEqual(converted_coord, [])

    def test_convertLatLongAltToCartesian_EmptyInputUnitsEmptyCoordinates_EmptyCoordinates(self):
        input_units = []
        input_coord = []
        coord_trans = CoordinateTransformer()
        converted_coord = coord_trans.convertLatLongAltToCartesian(input_units, input_coord)
        self.assertEqual(converted_coord, [])

class RotateCartesianCoordinateSystemTest(unittest.TestCase):

    def test_rotateCartesianCoordinateSystem_3IntCoordinateRotate45DegAboutXAxis_XIntRotatedYZFloatCoordinate(self):
        coord = np.array([1,2,3])
        a = np.radians(45)
        xrot_matrix = np.array([[1,0,0], [0,np.cos(a),-1*np.sin(a)], [0,np.sin(a),np.cos(a)]])
        rotator = CoordinateTransformer()
        coord_rot = rotator.rotateCartesianCoordinateSystem(coord, xrot_matrix)
        self.assertIsNone(np.testing.assert_array_almost_equal(coord_rot, np.array([1, -0.7071067812, 3.535533906])))

    def test_rotateCartesianCoordinateSystem_3IntCoordinateRotate60DegAboutYAxis_YIntRotatedYZFloatCoordinate(self):
        coord = np.array([1,2,3])
        a = np.radians(60)
        yrot_matrix = np.array([[np.cos(a),0,np.sin(a)], [0,1,0], [-1*np.sin(a),0,np.cos(a)]])
        rotator = CoordinateTransformer()
        coord_rot = rotator.rotateCartesianCoordinateSystem(coord, yrot_matrix)
        self.assertIsNone(np.testing.assert_array_almost_equal(coord_rot, np.array([3.098076211, 2, 0.6339745962])))

    def test_rotateCartesianCoordinateSystem_3IntCoordinateRotate90DegAboutZAxis_ZIntRotatedXYFloatCoordinate(self):
        coord = np.array([1,2,3])
        a = np.radians(90)
        zrot_matrix = np.array([[np.cos(a),-1*np.sin(a),0], [np.sin(a),np.cos(a),0], [0,0,1]])
        rotator = CoordinateTransformer()
        coord_rot = rotator.rotateCartesianCoordinateSystem(coord, zrot_matrix)
        self.assertIsNone(np.testing.assert_array_almost_equal(coord_rot, np.array([-2, 1, 3])))

    def test_rotateCartesianCoordinateSystem_3IntCoordEmptyRotationMatrix_ZIntRotatedXYFloatCoordinate(self):
        coord = np.array([1,2,3])
        rot_matrix = np.array([[], [], []])
        rotator = CoordinateTransformer()
        coord_rot = rotator.rotateCartesianCoordinateSystem(coord, rot_matrix)
        self.assertIsNone(np.testing.assert_array_almost_equal(coord_rot, np.array([])))

    def test_rotateCartesianCoordinateSystem_EmptyCoordRotate90DegAboutZAxis_EmptyCoordinate(self):
        coord = np.array([])
        a = np.radians(90)
        zrot_matrix = np.array([[np.cos(a),-1*np.sin(a),0], [np.sin(a),np.cos(a),0], [0,0,1]])
        rotator = CoordinateTransformer()
        coord_rot = rotator.rotateCartesianCoordinateSystem(coord, zrot_matrix)
        self.assertIsNone(np.testing.assert_array_almost_equal(coord_rot, np.array([])))

    def test_rotateCartesianCoordinateSystem_OriginCoordRotate90DegAboutZAxis_EmptyCoordinate(self):
        coord = np.array([0,0,0])
        a = np.radians(90)
        zrot_matrix = np.array([[np.cos(a),-1*np.sin(a),0], [np.sin(a),np.cos(a),0], [0,0,1]])
        rotator = CoordinateTransformer()
        coord_rot = rotator.rotateCartesianCoordinateSystem(coord, zrot_matrix)
        self.assertIsNone(np.testing.assert_array_almost_equal(coord_rot, np.array([0,0,0])))

if __name__ == "__main__":
    unittest.main()
        
