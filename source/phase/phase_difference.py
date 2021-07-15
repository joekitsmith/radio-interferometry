## PHASE DIFFERENCE ##

import math

class PhaseDifferenceCalculator():

    def wrapRadians(self, angle : float) -> float:
        """Takes angle in radians and wraps into 0 -> 2pi window"""
        angle = angle / math.pi % 2
        return(angle*math.pi)

    def calculate2DPhaseDifference(self, d : float, wav : float, alpha : float) -> float:
        """
        Calculate phase difference between two radio antenna in 2D

        Parameters
        -------
        d : float
            baseline separation of two antenna
        lambda: float
            wavelength of radiowave
        alpha: float
            angle of radio source to baseline vector in degrees
        
        Returns
        -------
        phi : float
            phase difference between two antenna in degrees
        """
        alpha_rad = math.radians(alpha)
        phi_rad = self.wrapRadians((2 * math.pi * d * math.cos(alpha_rad)) / wav)
        return(math.degrees(phi_rad))

    def calculate3DPhaseDifference(self, d : float, wav : float, alt : float, az : float) -> float:
        """
        Calculate phase difference between two radio antenna using altitude and azimuth

        Parameters
        -------
        d : float
            baseline separation of two antenna
        alt : float
            altitude of radio source from surface of earth in degrees
        az : float
            azimuthal angle of radio source clockwise from North in degrees
        lambda: float
            wavelength of radiowave

        Returns
        -------
        phi : float
            phase difference between two antenna in degrees
        """
        alt_rad, az_rad = math.radians(alt), math.radians(az)
        cos_theta = math.cos(alt_rad) * math.cos(az_rad)
        phi_rad = self.wrapRadians((2 * math.pi * d * cos_theta) / wav)
        return(math.degrees(phi_rad))