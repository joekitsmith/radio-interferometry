## PHASE DIFFERENCE TEST ##

import unittest
import math
import PhaseDifference

class Calculate2DPhaseDifferenceTest(unittest.TestCase):

    def test_calculate2DPhaseDifference_SourcePerpendicularToBaselineAndWavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, alpha = 0.5, 1, math.pi/2
        phi = PhaseDifference.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 0)

    def test_calculate2DPhaseDifference_SourceParallelToBaselineAndWavelengthDoubleBaseline_PhaseDifferencePi(self):
        d, wav, alpha = 0.5, 1, 0
        phi = PhaseDifference.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, math.pi)

    def test_calculate2DPhaseDifference_SourceParallelToBaselineAndWavelengthEqualsBaseline_PhaseDifferenceZero(self):
        d, wav, alpha = 1, 1, 0
        phi = PhaseDifference.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 0)

class Calculate3DPhaseDifferenceTest(unittest.TestCase):

    def test_calculate3DPhaseDifference_Azimuth0Altitude0WavelengthDoubleBaseline_PhaseDifferencePi(self):
        d, wav, azi, alt = 0.5, 1, 0, 0
        phi = PhaseDifference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, math.pi)

    def test_calculate3DPhaseDifference_Azimuth0Altitude0WavelengthEqualsBaseline_PhaseDifferenceZero(self):
        d, wav, azi, alt = 1, 1, 0, 0
        phi = PhaseDifference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

    def test_calculate3DPhaseDifference_Azimuth0Altitude90degWavelengthWavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, azi, alt = 0.5, 1, 0, math.pi/2
        phi = PhaseDifference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

    def test_calculate3DPhaseDifference_Azimuth90degAltitude90degWavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, azi, alt = 0.5, 1, math.pi/2, math.pi/2
        phi = PhaseDifference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

    def test_calculate3DPhaseDifference_Azimuth90degAltitude0WavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, azi, alt = 0.5, 1, math.pi/2, 0
        phi = PhaseDifference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

if __name__ == '__main__':
    unittest.main()       