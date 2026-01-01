###################
""" used modules"""
###################

import math
k = 8.988 * pow(10, 9)

########################################
""" q = -+ne --> modified equations """
########################################

def q_electric_charge1(n, e, electric_type):
    if electric_type == "p":
        result = n * e
    elif electric_type == "e":
        result = -n * e
    elif electric_type == "n":
        result = 0
    return result

def n_electric_number1(q, e):
    result = q / e
    return result

def e_elementry_charge1(q, n):
    result = q / n
    return result

########################################
""" f = k * ((q1 * q2) / r^2) --> modified equations """
########################################

def electric_force1(q1, q2, r, k):
    result = k * ((q1 * q2) / pow(r, 2))
    return result

def q1_value1(q2, F, r, k):
    result = (F * pow(r, 2)) / (k * q2)
    return result

def q2_value1(F, q1, r, k):
    result = (F * pow(r, 2)) / (k * q1)
    return result

def radius1(F, q1, q2):
    result = math.sqrt((k * q1 * q2) / F)
    return result

###############################################
""" V = IR --> modified equations """
###############################################

def volt1(I, R):
    result = I * R
    return result

def ampers1(V, R):
    result = V / R
    return result

def resistance1(V, I):
    result = V / I
    return result

#################################################
""" I = q / t --> modified equations """
#################################################

def ampers2(q, t):
    result = q / t
    return result

def q_electric_charge2(I, t):
    result = I * t
    return result

def time1(q, I):
    result = q / I
    return result

###################################################
""" p = VI --> modified equations """
###################################################

def power1(V, I):
    result = V * I
    return result

def volt2(I, p):
    result = p / I
    return result

def ampers3(V, p):
    result = p / V
    return result

###############################################
""" u = qV --> modified equations """
###############################################

def potential_energy1(q, V):
    result = q * V
    return result

def volt3(q, u):
    result = u / q
    return result

def q_electric_charge3(u, V):
    result = u / V
    return result

def potential_energy2(V, I, t):
    result = V * I * t
    return result

def q_electric_charge4(I, t):
    result = I * t
    return result

def potential_energy3(n, e):
    result = n * e
    return result

##############################################
""" R = p * L / A --> modified equations """
###############################################

def resistance2(p, L, A):
    result = p * (L / A)
    return result

def resistivity(R, L, A):
    result = (R * A) / L
    return result

def length1(R, p, A):
    result = (R * A) / p
    return result

def area1(R, L, p):
    result = (L * p) / R
    return result

##############################################
""" R = R1 + R2 + R3 + ... --> modified equations """
###############################################

def resistance_frequent(*resistances):
    result = sum(resistances)
    return result

def volt_series(*voltages):
    result = sum(voltages)
    return result

def ampers_series(I):
    result = I
    return result

##############################################
""" R = 1/R1 + 1/R2 + 1/R3 + ... --> modified equations """
###############################################

def resistance_parallel(*resistances):
    inverse_sum = sum(1 / r for r in resistances if r != 0)
    result = 1 / inverse_sum if inverse_sum != 0 else float('inf')
    return result

def volt_parallel(V):
    result = V
    return result

def ampers_parallel(*currents):
    result = sum(currents)
    return result
