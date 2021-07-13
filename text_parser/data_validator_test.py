## DATA VALIDATOR TESTS ##

import unittest
import data_validator

class ValidateDimensionUnitsTest(unittest.TestCase):

    def test_validateDimensionUnits_3MInputUnits_ReturnsTrue(self):
        input_units = ['m','m','m']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionUnits(input_units)
        self.assertTrue(is_valid)

    def test_validateDimensionUnits_2Ft1MInputUnits_ReturnsTrue(self):
        input_units = ['ft','ft','m']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionUnits(input_units)
        self.assertTrue(is_valid)

    def test_validateDimensionUnits_3FtInputUnits_ReturnsTrue(self):
        input_units = ['ft','ft','ft']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionUnits(input_units)
        self.assertTrue(is_valid)

    def test_validateDimensionUnits_2D1MInputUnits_ReturnsTrue(self):
        input_units = ['ft','ft','m']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionUnits(input_units)
        self.assertTrue(is_valid)

    def test_validateDimensionUnits_1InvalidAnd2ValidInputUnits_ReturnsFalse(self):
        input_units = ['b','y','m']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionUnits(input_units)
        self.assertFalse(is_valid)

    def test_validateDimensionUnits_ListOfEmptyString_ReturnsFalse(self):
        input_units = ['']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionUnits(input_units)
        self.assertFalse(is_valid)

class ValidateDimensionCoordinateSystemTest(unittest.TestCase):

    def test_validateDimensionCoordinateSystem_3MInputUnits_ReturnsTrue(self):
        input_units = ['m','m','m']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionCoordinateSystem(input_units)
        self.assertTrue(is_valid)

    def test_validateDimensionCoordinateSystem_2Ft1MInputUnits_ReturnsTrue(self):
        input_units = ['ft','ft','m']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionCoordinateSystem(input_units)
        self.assertTrue(is_valid)

    def test_validateDimensionCoordinateSystem_3FtInputUnits_ReturnsTrue(self):
        input_units = ['ft','ft','ft']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionCoordinateSystem(input_units)
        self.assertTrue(is_valid)

    def test_validateDimensionCoordinateSystem_2D1MInputUnits_ReturnsTrue(self):
        input_units = ['d','d','m']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionCoordinateSystem(input_units)
        self.assertTrue(is_valid)

    def test_validateDimensionCoordinateSystem_1D2MInputUnits_ReturnsFalse(self):
        input_units = ['d','m','m']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionCoordinateSystem(input_units)
        self.assertFalse(is_valid)

    def test_validateDimensionCoordinateSystem_3DInputUnits_ReturnsFalse(self):
        input_units = ['d','d','d']
        print(input_units.count('d'))
        data_val = data_validator.DataValidator()
        is_valid = data_val.validateDimensionCoordinateSystem(input_units)
        self.assertFalse(is_valid)

class Validate3DCoordinatesTest(unittest.TestCase):

    def test_validate3DCoordinates_3DStrCoordinate_ReturnsTrue(self):
        input_coord = ['m','m','m']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validate3DCoordinates(input_coord)
        self.assertTrue(is_valid)

    def test_validate3DCoordinates_3DIntCoordinate_ReturnsTrue(self):
        input_coord = [1,2,3]
        data_val = data_validator.DataValidator()
        is_valid = data_val.validate3DCoordinates(input_coord)
        self.assertTrue(is_valid)

    def test_validate3DCoordinates_3DFloatCoordinate_ReturnsTrue(self):
        input_coord = [1.5,2.5739,3.899]
        data_val = data_validator.DataValidator()
        is_valid = data_val.validate3DCoordinates(input_coord)
        self.assertTrue(is_valid)

    def test_validate3DCoordinates_2DStrCoordinate_ReturnsFalse(self):
        input_coord = ['m', 'm']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validate3DCoordinates(input_coord)
        self.assertFalse(is_valid)

    def test_validate3DCoordinates_EmptyStrCoordinate_ReturnsFalse(self):
        input_coord = ['']
        data_val = data_validator.DataValidator()
        is_valid = data_val.validate3DCoordinates(input_coord)
        self.assertFalse(is_valid)

class DetermineDataPassTest(unittest.TestCase):

    def test_determineDataPass_3MInputUnits3Of3DIntCoordinates_ReturnsTrue(self):
        input_units = ['m', 'm', 'm']
        input_coords = [[1,2,3], [2,4,6], [7,8,9]]
        data_val = data_validator.DataValidator()
        is_pass = data_val.determineDataPass(input_units, input_coords)
        self.assertTrue(is_pass)

    def test_determineDataPass_2Ft1MInputUnits3Of3DIntCoordinates_ReturnsTrue(self):
        input_units = ['ft', 'ft', 'm']
        input_coords = [[1,2,3], [2,4,6], [7,8,9]]
        data_val = data_validator.DataValidator()
        is_pass = data_val.determineDataPass(input_units, input_coords)
        self.assertTrue(is_pass)

    def test_determineDataPass_2D1MInputUnits3Of3DIntCoordinates_ReturnsFalse(self):
        input_units = ['d', 'd', 'm']
        input_coords = [[1,2,3], [2,4,6], [7,8,9]]
        data_val = data_validator.DataValidator()
        is_pass = data_val.determineDataPass(input_units, input_coords)
        self.assertTrue(is_pass)

    def test_determineDataPass_1D2MInputUnits3Of3DIntCoordinates_ReturnsFalse(self):
        input_units = ['d', 'm', 'm']
        input_coords = [[1,2,3], [2,4,6], [7,8,9]]
        data_val = data_validator.DataValidator()
        is_pass = data_val.determineDataPass(input_units, input_coords)
        self.assertFalse(is_pass)

    def test_determineDataPass_3DInputUnits3Of3DIntCoordinates_ReturnsFalse(self):
        input_units = ['d', 'd', 'd']
        input_coords = [[1,2,3], [2,4,6], [7,8,9]]
        data_val = data_validator.DataValidator()
        is_pass = data_val.determineDataPass(input_units, input_coords)
        self.assertFalse(is_pass)

    def test_determineDataPass_3MInputUnits3Of2DIntCoordinates_ReturnsFalse(self):
        input_units = ['m', 'm', 'm']
        input_coords = [[1,2], [2,4], [7,8]]
        data_val = data_validator.DataValidator()
        is_pass = data_val.determineDataPass(input_units, input_coords)
        self.assertFalse(is_pass)

    def test_determineDataPass_2MInputUnits3Of3DIntCoordinates_ReturnsFalse(self):
        input_units = ['m', 'm']
        input_coords = [[1,2,3], [2,4,6], [7,8,9]]
        data_val = data_validator.DataValidator()
        is_pass = data_val.determineDataPass(input_units, input_coords)
        self.assertFalse(is_pass)

    def test_determineDataPass_EmptyStrInputUnits3Of3DIntCoordinates_ReturnsFalse(self):
        input_units = ['']
        input_coords = [[1,2,3], [2,4,6], [7,8,9]]
        data_val = data_validator.DataValidator()
        is_pass = data_val.determineDataPass(input_units, input_coords)
        self.assertFalse(is_pass)

    def test_determineDataPass_3MInputUnitsEmptyStrCoordinates_ReturnsFalse(self):
        input_units = ['m', 'm', 'm']
        input_coords = ['']
        data_val = data_validator.DataValidator()
        is_pass = data_val.determineDataPass(input_units, input_coords)
        self.assertFalse(is_pass)

    def test_determineDataPass_InvalidInputUnits3Of3DIntCoordinates_ReturnsFalse(self):
        input_units = ['m', 'm', 'x']
        input_coords = [[1,2,3],[2,4,6],[7,8,9]]
        data_val = data_validator.DataValidator()
        is_pass = data_val.determineDataPass(input_units, input_coords)
        self.assertFalse(is_pass)

if __name__ == '__main__':
    unittest.main()