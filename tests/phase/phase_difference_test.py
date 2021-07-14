## PHASE DIFFERENCE TEST ##

import unittest
import math
from source.phase.phase_difference import PhaseDifferenceCalculator

class Calculate2DPhaseDifferenceTest(unittest.TestCase):

    def test_calculate2DPhaseDifference_SourcePerpendicularToBaselineAndWavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, alpha = 0.5, 1, 90
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 0)

    def test_calculate2DPhaseDifference_SourceParallelToBaselineAndWavelengthDoubleBaseline_PhaseDifferencePi(self):
        d, wav, alpha = 0.5, 1, 0
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 180)

    def test_calculate2DPhaseDifference_SourceParallelToBaselineAndWavelengthEqualsBaseline_PhaseDifferenceZero(self):
        d, wav, alpha = 1, 1, 0
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 0)

    def test_calculate2DPhaseDifference_SourceParallelToBaselineAndWavelengthNotMultipleOfBaseline_PhaseDifferenceKnownFloat(self):
        d, wav, alpha = 0.456, 1.102, 0
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 148.9655172)

    def test_calculate2DPhaseDifference_Source45DegToBaselineAndWavelengthEqualsBaseline_PhaseDifferenceKnownFloat(self):
        d, wav, alpha = 1, 1, 45
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 254.5584412)

    def test_calculate2DPhaseDifference_Source22DegToBaselineWavelength20TimesBaseline_PhaseDifferenceKnownFloat(self):
        d, wav, alpha = 10, 0.5, 22.5
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate2DPhaseDifference(d, wav, alpha)
        self.assertAlmostEqual(phi, 171.9326341)

class Calculate3DPhaseDifferenceTest(unittest.TestCase):

    def test_calculate3DPhaseDifference_Azimuth0Altitude0WavelengthDoubleBaseline_PhaseDifferencePi(self):
        d, wav, azi, alt = 0.5, 1, 0, 0
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 180)

    def test_calculate3DPhaseDifference_Azimuth0Altitude0WavelengthEqualsBaseline_PhaseDifferenceZero(self):
        d, wav, azi, alt = 1, 1, 0, 0
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

    def test_calculate3DPhaseDifference_Azimuth0Altitude0WavelengthNotMultipleOfBaseline_PhaseDifferenceKnownFloat(self):
        d, wav, azi, alt = 0.754, 1, 0, 0
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 271.4400000)

    def test_calculate3DPhaseDifference_Azimuth0Altitude90degWavelengthWavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, azi, alt = 0.5, 1, 0, 90
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

    def test_calculate3DPhaseDifference_Azimuth90degAltitude90degWavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, azi, alt = 0.5, 1, 90, 90
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

    def test_calculate3DPhaseDifference_Azimuth90degAltitude0WavelengthBaselineAny_PhaseDifferenceZero(self):
        d, wav, azi, alt = 0.5, 1, 90, 0
        phase_calc = PhaseDifferenceCalculator()
        phi = phase_calc.calculate3DPhaseDifference(d, wav, azi, alt)
        self.assertAlmostEqual(phi, 0)

if __name__ == '__main__':
    unittest.main()       