## PHASE DIFFERENCE ##

import math

def wrapRadians(angle):
    """Takes angle in radians and wraps into 0 -> 2pi window"""
    angle = angle / math.pi % 2
    return(angle*math.pi)

def calculate2DPhaseDifference(d, wav, alpha):
    """
    Calculate phase difference between two radio antenna in 2D

    Parameters
    -------
    d : float
        baseline separation of two antenna
    lambda: float
        wavelength of radiowave
    alpha: int
        angle of radio source to baseline vector
        
    Returns
    -------
    phi : int
        phase difference between two antenna
    """
    phi = wrapRadians((2 * math.pi * d * math.cos(alpha)) / wav)
    return(phi)

def calculate3DPhaseDifference(d, wav, alt, az):
    """
    Calculate phase difference between two radio antenna using altitude and azimuth

    Parameters
    -------
    d : int
        baseline separation of two antenna
    alt : int
        altitude of radio source from surface of earth
    az : int
        azimuthal angle of radio source clockwise from North
    lambda: float
        wavelength of radiowave

    Returns
    -------
    phi : int
        phase difference between two antenna
    """
    cos_theta = math.cos(alt) * math.cos(az)
    phi = wrapRadians((2 * math.pi * d * cos_theta) / wav)
    return(phi)
