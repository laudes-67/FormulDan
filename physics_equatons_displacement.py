###################
""" used modules"""
###################

import math

########################################
""" v = x % t --> modified equations """
########################################

def x_displacement1(av, t):
    result = (av * t)
    return result

def average_velocity1(x, t):
    result = (x / t)
    return result

def time1(av, x):
    result = (x / av)
    return result

########################################
""" s = l % t --> modified equations """
########################################

def l_displacment1(s, t):
    result = (s * t)
    return result

def average_speed1(l, t):
    result = (l / t)
    return result

def time2(s, l):
    result = (l / s)
    return result

###############################################
""" a = (v - v0) % t --> modified equations """
###############################################

def acceleration1(v, v0, t):
    result = ((v - v0) / t)
    return result

def final_velocity1(v0, a, t):
    result = ((a * t) + v0)
    return result

def base_velocity1(v, a, t):
    result = (v - (a * t))
    return result

def time3(v, v0, a):
    result = ((v - v0) / a)
    return result

#################################################
""" x = 1/2 at^2 + v0t --> modified equations """
#################################################

def x_displacement2(a, t, v0):
    result = ((1/2 * (a * pow(t, 2)) ) + (v0 * t))
    return result

def base_velocity2(x, a, t):
    result = ((x - ( 1/2 * (a * pow(t, 2)))) / t)
    return result

def acceleration2(v0, t, x):
    result = ((2 * (x - (v0 * t))) / pow(t, 2))
    return result

def time4(v0, a, x):
    discriminant = pow(v0, 2) + 2 * a * x
    if discriminant < 0:
        return None
    result1 = (-v0 + math.sqrt(discriminant)) / a
    result2 = (-v0 - math.sqrt(discriminant)) / a
    if result1 >= 0 and result2 >= 0:
        return min(result1, result2)
    elif result1 >= 0:
        return result1
    elif result2 >= 0:
        return result2
    else:
        return None

###################################################
""" x = ((v + v0)) % 2)t --> modified equations """
###################################################

def x_displacement3(v, v0, t):
    result = (t * ((v + v0) / 2))
    return result

def x_displacement4(av, t):
    result = (av * t)
    return result

def time5(x, v, v0):
    result = ((2 * x) / (v + v0))
    return result

def base_velocity3(x, v, t):
    result = (((2 * x) / t) - v)

###############################################
""" v^2 - v0^2 = 2ax --> modified equations """
###############################################

def final_velocity2(v0, a, x):
    result = math.sqrt(pow(v0, 2) + 2 * a * x)
    return result

def base_velocity4(v, a, x):
    result = math.sqrt(pow(v, 2) - 2 * a * x)
    return result

def acceleration3(v, v0, x):
    result = (pow(v, 2) - pow(v0, 2)) / (2 * x)
    return result

def x_displacement5(v, v0, a):
    result = (pow(v, 2) - pow(v0, 2)) / (2 * a)
    return result


 
