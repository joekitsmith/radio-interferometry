## PHASE DIFFERENCE TEST ##

import unittest
import math
import phase_difference

class Calculate2DPhaseDifferenceTest(unittest.TestCase):

    def test_calculate2DPhaseDifference_SourcePerpendicularToBaselineAndWavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, alpha = 0.5, 1, math.pi/2
        phi = phase_difference.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 0)

    def test_calculate2DPhaseDifference_SourceParallelToBaselineAndWavelengthDoubleBaseline_PhaseDifferencePi(self):
        d, wav, alpha = 0.5, 1, 0
        phi = phase_difference.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, math.pi)

    def test_calculate2DPhaseDifference_SourceParallelToBaselineAndWavelengthEqualsBaseline_PhaseDifferenceZero(self):
        d, wav, alpha = 1, 1, 0
        phi = phase_difference.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 0)

    def test_calculate2DPhaseDifference_SourceParallelToBaselineAndWavelengthNotMultipleOfBaseline_PhaseDifferenceKnownFloat(self):
        d, wav, alpha = 0.456, 1.102, 0
        phi = phase_difference.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 2.5999387)

    def test_calculate2DPhaseDifference_Source45DegToBaselineAndWavelengthEqualsBaseline_PhaseDifferenceKnownFloat(self):
        d, wav, alpha = 1, 1, math.pi/4
        phi = phase_difference.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 4.4428829)

    def test_calculate2DPhaseDifference_Source22DegToBaselineWavelength20TimesBaseline_PhaseDifferenceKnownFloat(self):
        d, wav, alpha = 10, 0.5, math.pi/8
        phi = phase_difference.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 3.0007906)

class Calculate3DPhaseDifferenceTest(unittest.TestCase):

    def test_calculate3DPhaseDifference_Azimuth0Altitude0WavelengthDoubleBaseline_PhaseDifferencePi(self):
        d, wav, azi, alt = 0.5, 1, 0, 0
        phi = phase_difference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, math.pi)

    def test_calculate3DPhaseDifference_Azimuth0Altitude0WavelengthEqualsBaseline_PhaseDifferenceZero(self):
        d, wav, azi, alt = 1, 1, 0, 0
        phi = phase_difference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

    def test_calculate3DPhaseDifference_Azimuth0Altitude0WavelengthNotMultipleOfBaseline_PhaseDifferenceKnownFloat(self):
        d, wav, azi, alt = 0.754, 1, 0, 0
        phi = phase_difference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 4.7375217)

    def test_calculate3DPhaseDifference_Azimuth0Altitude90degWavelengthWavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, azi, alt = 0.5, 1, 0, math.pi/2
        phi = phase_difference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

    def test_calculate3DPhaseDifference_Azimuth90degAltitude90degWavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, azi, alt = 0.5, 1, math.pi/2, math.pi/2
        phi = phase_difference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

    def test_calculate3DPhaseDifference_Azimuth90degAltitude0WavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, azi, alt = 0.5, 1, math.pi/2, 0
        phi = phase_difference.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

if __name__ == '__main__':
    unittest.main()       