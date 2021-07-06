## TEST BASELINE VECTOR DETERMINATION ##

import sys, os
import unittest
import baseline_vectors

class TestTelescopeModel(unittest.TestCase):

    def performTest(self, text):
        file = open(os.path.join(sys.path[0], "antennae_coordinates.txt"), "w")
        file.write(text)
        file.close()
        telescope_model = baseline_vectors.TelescopeModel()
        telescope_model.extractInputData()
        telescope_model.convertCoordinates()
        telescope_model.calculateBaselinePairs()

    def test_randomData(self):
        text = "> Length dimension\n" + "ft" +"\n> Coordinates\n" + "(1,1)\n(1,2)\n(3,5)\n(6,7)"
        self.performTest(text)

    def test_invalidDimension(self):
        text = "> Length dimension\n" + "b" + "\n> Coordinates\n" + "(1,1)\n(1,2)\n(3,5)\n(6,7)"
        self.performTest(text)

    def test_invalidCoordinates(self):
        text = "> Length dimension\n" + "ft" + "\n> Coordinates\n" + "(1,1)\n(1,2)\n(3,5)\n(6,7)"
        self.performTest(text)

    def test_emptyTextFile(self):
        text = " "
        self.performTest(text)

if __name__ == "__main__":
    unittest.main()