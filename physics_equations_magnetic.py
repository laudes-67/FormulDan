######################################
""" F = qvb --> modified equations """
######################################
def force1(q, V, B):
    result = (q * V * B)
    return result

def charge1(F, V, B):
    result = (F / (V * B))
    return result

def voltage1(F, q, B):
    result = (F / (q * B))
    return result

def magnetic_field1(F, q, V):
    result = (F / (q * V))

######################################
""" F = BIL --> modified equations """
######################################
def force2(B, I, L):
    result = (B * I * L)
    return result

def current1(F, B, L):
    result = (F / (B * L))
    return result

def length1(F, I, B):
    result = (F / (B * I))
    return result

def magnetic_field2(F, I, L):
    result = (F / (I * L))

####################################################
""" B = (2 * 10^-7) * I/R --> modified equations """
####################################################
def magnetic_field3(I, R):
    result = ((2 * pow(10, -7)) * (I / R))
    return result

def current2(B, R):
    result = ((B * R) / (2 * pow(10, -7)))
    return result

def resistance1(B, I):
    result = ((I / B) * (2 * pow(10, -7)))
    return result

######################################################
""" B = (12 * 10^-7) * NI/L --> modified equations """
######################################################
def magnetic_field3(N, I, L):
    result = ((12 * pow(10, -7)) * ((N * I) / L))
    return result

def current3(B, N, L):
    result = ((B * L) / (N * (12 * pow(10, -7))))
    return result

def turns1(B, I, L):
    result = ((B * L) / (I * (12 * pow(10, -7))))
    return result

def length2(I, B, N):
    result = ((N * I) / (B * (12 * pow(10, -7))))
    return result
