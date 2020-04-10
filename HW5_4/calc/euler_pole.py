import math as m
import numpy as np

#-- Utility Functions --------------------------------------------------------

def alpha(lat_p,lon_p,lat_x,lon_x):
    # """
    # lat_p: latitude of rotation pole P 
    # lon_p: longitude of roation pole P 
    # lat_x: latitude of point x on plate boundary 
    # lon_x: longitude of point x on plate boundary 
    # """
    return m.acos(np.cos(1.5708-lat_x)*np.cos(1.5708-lat_p) + np.sin(1.5708-lat_x)*np.sin(1.5708-lat_p)*np.cos(lon_p-lon_x))

def C(lat_p,lon_p,lat_x,lon_x, a):
        # """
    # lat_p: latitude of rotation pole P 
    # lon_p: longitude of roation pole P 
    # lat_x: latitude of point x on plate boundary 
    # lon_x: longitude of point x on plate boundary 
    # R    : Radius of earth
    # a    : a from alpha
    # """
    #return ((m.asin(m.cos(lat_p))*(m.sin(lon_p-lon_x))*(m.sin(a))))
    return m.asin((np.cos(lat_p)*np.sin(lon_p-lon_x))/np.sin(a))
    

def velocity(omega,a,R):
    # """
    # omega: angular velocity about rotaion pole
    # R    : Radius of earth
    # a    : a from alpha
    # """    
    return omega*R*(m.sin(a))
