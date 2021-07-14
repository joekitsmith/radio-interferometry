## BASELINE VECTOR DETERMINATION TESTS ##

import unittest
from source.baseline.baseline_vectors import BaselineVectorCalculator
from source.antennae.single_antenna import SingleAntenna
from deepdiff import DeepDiff

class CalculateBaselineVectorTest(unittest.TestCase):

    def test_calculateBaselineVector_2x3IntCoordinates_Returns3IntVector(self):
        coord_1, coord_2 = [1,2,3], [2,3,4]
        bv_calc = BaselineVectorCalculator()
        vector = bv_calc.calculateBaselineVector(coord_1, coord_2)
        self.assertEqual(vector, [1,1,1])

    def test_calculateBaselineVector_2x3FloatCoordinates_Returns3FloatVector(self):
        coord_1, coord_2 = [1.1, 4.56, 6.78], [3.56, 9.213, 7.897]
        bv_calc = BaselineVectorCalculator()
        vector = bv_calc.calculateBaselineVector(coord_1, coord_2)
        self.assertEqual(vector, [2.46, 4.653, 1.117])

    def test_calculateBaselineVector_EmptyCoordinates_ReturnsEmptyVector(self):
        coord_1, coord_2 = [], []
        bv_calc = BaselineVectorCalculator()
        vector = bv_calc.calculateBaselineVector(coord_1, coord_2)
        self.assertEqual(vector, [])

    def test_calculateBaselineVector_EmptyCoordinate1_ReturnsEmptyVector(self):
        coord_1, coord_2 = [], [1,2,3]
        bv_calc = BaselineVectorCalculator()
        vector = bv_calc.calculateBaselineVector(coord_1, coord_2)
        self.assertEqual(vector, [])

    def test_calculateBaselineVector_EmptyCoordinate2_ReturnsEmptyVector(self):
        coord_1, coord_2 = [1,2,3], []
        bv_calc = BaselineVectorCalculator()
        vector = bv_calc.calculateBaselineVector(coord_1, coord_2)
        self.assertEqual(vector, [])

    def test_calculateBaselineVector_2xNon3DimensionCoordinate_ReturnsSameDimensionVector(self):
        coord_1, coord_2 = [1,2,3,4,5], [6,7,8,9,10]
        bv_calc = BaselineVectorCalculator()
        vector = bv_calc.calculateBaselineVector(coord_1, coord_2)
        self.assertEqual(vector, [5,5,5,5,5])

class DetermineBaselineVectorsOfArray(unittest.TestCase):

    def test_determineBaselineVectorsOfArray_3x3IntCoordinateArrayList_Returns3ElementDictWith3IntVectorValues(self):
        antenna_1 = SingleAntenna(['m','m','m'], [1,2,3])
        antenna_2 = SingleAntenna(['m','m','m'], [4,5,6])
        antenna_3 = SingleAntenna(['m','m','m'], [7,8,9])
        array_list = [antenna_1, antenna_2, antenna_3]
        bv_calc = BaselineVectorCalculator()
        bv_calc.determineBaselineVectorsOfArray(array_list)
        output_dict = {(0,1): [3,3,3], (0,2): [6,6,6], (1,2): [3,3,3]}
        diff = DeepDiff(output_dict, bv_calc.baseline_dict)
        self.assertFalse(diff)

    def test_determineBaselineVectorsOfArray_2x3FloatCoordinateArrayList_Returns2ElementDictWith3FloatVectorValues(self):
        antenna_1 = SingleAntenna(['m','m','m'], [0.0064739,0.0045282,0.00463748])
        antenna_2 = SingleAntenna(['m','m','m'], [0.0090293,0.0028101,0.57498302])
        array_list = [antenna_1, antenna_2]
        bv_calc = BaselineVectorCalculator()
        bv_calc.determineBaselineVectorsOfArray(array_list)
        output_dict = {(0,1): [0.0025554, -0.0017181, 0.57034554]}
        diff = DeepDiff(output_dict, bv_calc.baseline_dict, significant_digits=15)
        self.assertFalse(diff)

    def test_determineBaselineVectorsOfArray_4x3IntCoordinateArrayList_Returns6ElementDictWith3IntVectorValues(self):
        antenna_1 = SingleAntenna(['m','m','m'], [1,2,3])
        antenna_2 = SingleAntenna(['m','m','m'], [4,5,6])
        antenna_3 = SingleAntenna(['m','m','m'], [7,8,9])
        antenna_4 = SingleAntenna(['m','m','m'], [10,11,12])
        array_list = [antenna_1, antenna_2, antenna_3, antenna_4]
        bv_calc = BaselineVectorCalculator()
        bv_calc.determineBaselineVectorsOfArray(array_list)
        output_dict = {(0,1): [3,3,3], (0,2): [6,6,6], (1,2): [3,3,3], (0,3): [9,9,9], (1,3): [6,6,6], (2,3): [3,3,3]}
        diff = DeepDiff(output_dict, bv_calc.baseline_dict)
        self.assertFalse(diff)

    def test_determineBaselineVectorsOfArray_3x4IntCoordinateArrayList_Returns3ElementDictWith4IntVectorValues(self):
        antenna_1 = SingleAntenna(['m','m','m','m'], [1,2,3,4])
        antenna_2 = SingleAntenna(['m','m','m','m'], [4,5,6,7])
        antenna_3 = SingleAntenna(['m','m','m','m'], [7,8,9,10])
        array_list = [antenna_1, antenna_2, antenna_3]
        bv_calc = BaselineVectorCalculator()
        bv_calc.determineBaselineVectorsOfArray(array_list)
        output_dict = {(0,1): [3,3,3,3], (0,2): [6,6,6,6], (1,2): [3,3,3,3]}
        diff = DeepDiff(output_dict, bv_calc.baseline_dict)
        self.assertFalse(diff)

    def test_determineBaselineVectorsOfArray_EmptyArrayList_ReturnsEmptyDict(self):
        array_list = []
        bv_calc = BaselineVectorCalculator()
        bv_calc.determineBaselineVectorsOfArray(array_list)
        output_dict = {}
        diff = DeepDiff(output_dict, bv_calc.baseline_dict)
        self.assertFalse(diff)

    def test_determineBaselineVectorsOfArray_ArrayListWithEmptySingleAntenna_Returns3ElementDictWithEmptyVectors(self):
        antenna_1 = SingleAntenna([], [])
        antenna_2 = SingleAntenna([], [])
        antenna_3 = SingleAntenna([], [])
        array_list = [antenna_1, antenna_2, antenna_3]
        bv_calc = BaselineVectorCalculator()
        bv_calc.determineBaselineVectorsOfArray(array_list)
        output_dict = {(0,1): [], (0,2): [], (1,2): []}
        diff = DeepDiff(output_dict, bv_calc.baseline_dict)
        self.assertFalse(diff)

if __name__ == '__main__':
    unittest.main()