#!/usr/bin/env python2.7

def higgsino_map_masses(lMasses):

    ''' map the masses of N1, N2, N3, N4, C1 and C2 to the mass parameters of
    the pMSSM mu and M1
    parameters:
        lMasses: List of masses in the following order: N1, N2, N3, N4, C1, C2;
                 masses are given in GeV
    return value:
        Tuple of pMSSM mass parameters: mu, M1; masses are given in GeV
    '''

    # Round input masses to one digit
    lMasses_rounded = []
    for mass in lMasses:
        lMasses_rounded.append(round(mass, 1))
    lMasses = lMasses_rounded
    del lMasses_rounded

    # Set up dictionary of masses
    dMasses = {}
    dMasses[(100,  300)] = [  92.8,  109.7,  304.6,  663.5,  101.1,  663.5]
    dMasses[(100,  400)] = [  96.1,  108.6,  401.9,  873.4,  102.3,  873.4]
    dMasses[(100,  500)] = [  98.0,  107.9,  500.0, 1082.8,  102.9, 1082.8]
    dMasses[(100,  600)] = [  99.3,  107.5,  598.6, 1291.5,  103.3, 1291.5]
    dMasses[(100,  800)] = [ 100.7,  106.8,  796.4, 1706.9,  103.7, 1706.9]
    dMasses[(100, 1000)] = [ 101.6,  106.5,  994.5, 2119.8,  104.0, 2119.8]
    dMasses[(100, 1200)] = [ 102.1,  106.2, 1192.9, 2530.6,  104.1, 2530.6]
    dMasses[(120,  300)] = [ 112.6,  130.2,  305.0,  663.5,  121.6,  663.5]
    dMasses[(120,  400)] = [ 116.5,  129.2,  402.1,  873.3,  122.9,  873.3]
    dMasses[(120,  500)] = [ 118.6,  128.6,  500.1, 1082.7,  123.5, 1082.7]
    dMasses[(120,  600)] = [ 119.9,  128.2,  598.7, 1291.4,  124.0, 1291.4]
    dMasses[(120,  800)] = [ 121.4,  127.6,  796.4, 1706.8,  124.5, 1706.8]
    dMasses[(120, 1000)] = [ 122.3,  127.2,  994.5, 2119.7,  124.7, 2119.7]
    dMasses[(120, 1200)] = [ 122.9,  127.0, 1192.9, 2530.5,  124.9, 2530.5]
    dMasses[(140,  300)] = [ 132.4,  150.7,  305.6,  663.6,  141.9,  663.6]
    dMasses[(140,  400)] = [ 136.8,  149.9,  402.3,  873.3,  143.4,  873.3]
    dMasses[(140,  500)] = [ 139.0,  149.3,  500.2, 1082.6,  144.2, 1082.6]
    dMasses[(140,  600)] = [ 140.5,  148.9,  598.7, 1291.3,  144.6, 1291.3]
    dMasses[(140,  800)] = [ 142.1,  148.3,  796.4, 1706.7,  145.2, 1706.7]
    dMasses[(140, 1000)] = [ 143.0,  148.0,  994.5, 2119.6,  145.5, 2119.6]
    dMasses[(140, 1200)] = [ 143.7,  147.8, 1192.9, 2530.3,  145.7, 2530.3]
    dMasses[(160,  300)] = [ 151.8,  171.3,  306.4,  663.7,  162.3,  663.6]
    dMasses[(160,  400)] = [ 156.9,  170.5,  402.6,  873.2,  163.9,  873.2]
    dMasses[(160,  500)] = [ 159.5,  169.9,  500.4, 1082.6,  164.8, 1082.5]
    dMasses[(160,  600)] = [ 161.0,  169.5,  598.8, 1291.2,  165.3, 1291.2]
    dMasses[(160,  800)] = [ 162.7,  169.0,  796.4, 1706.6,  165.9, 1706.6]
    dMasses[(160, 1000)] = [ 163.7,  168.7,  994.5, 2119.5,  166.2, 2119.5]
    dMasses[(160, 1200)] = [ 164.4,  168.5, 1192.9, 2530.2,  166.4, 2530.2]
    dMasses[(180,  300)] = [ 171.0,  191.8,  307.4,  663.8,  182.6,  663.7]
    dMasses[(180,  400)] = [ 177.0,  191.0,  402.9,  873.2,  184.4,  873.2]
    dMasses[(180,  500)] = [ 179.8,  190.5,  500.5, 1082.5,  185.4, 1082.5]
    dMasses[(180,  600)] = [ 181.5,  190.2,  598.8, 1291.2,  185.9, 1291.1]
    dMasses[(180,  800)] = [ 183.4,  189.7,  796.4, 1706.5,  186.5, 1706.5]
    dMasses[(180, 1000)] = [ 184.4,  189.4,  994.5, 2119.4,  186.9, 2119.4]
    dMasses[(180, 1200)] = [ 185.1,  189.2, 1192.9, 2530.1,  187.1, 2530.1]
    dMasses[(200,  300)] = [ 189.8,  212.3,  308.8,  663.9,  202.8,  663.9]
    dMasses[(200,  400)] = [ 197.0,  211.6,  403.3,  873.2,  204.9,  873.2]
    dMasses[(200,  500)] = [ 200.2,  211.1,  500.7, 1082.4,  205.9, 1082.4]
    dMasses[(200,  600)] = [ 202.0,  210.8,  598.9, 1291.1,  206.5, 1291.1]
    dMasses[(200,  800)] = [ 203.9,  210.4,  796.4, 1706.4,  207.2, 1706.4]
    dMasses[(200, 1000)] = [ 205.0,  210.1,  994.5, 2119.3,  207.5, 2119.3]
    dMasses[(200, 1200)] = [ 205.7,  209.9, 1192.9, 2530.0,  207.8, 2530.0]
    dMasses[(220,  300)] = [ 207.9,  232.8,  311.0,  664.1,  223.0,  664.0]
    dMasses[(220,  400)] = [ 216.8,  232.2,  403.9,  873.2,  225.3,  873.2]
    dMasses[(220,  500)] = [ 220.4,  231.7,  500.9, 1082.4,  226.4, 1082.4]
    dMasses[(220,  600)] = [ 222.4,  231.4,  599.0, 1291.0,  227.1, 1291.0]
    dMasses[(220,  800)] = [ 224.5,  231.0,  796.5, 1706.3,  227.8, 1706.3]
    dMasses[(220, 1000)] = [ 225.6,  230.7,  994.5, 2119.2,  228.2, 2119.2]
    dMasses[(220, 1200)] = [ 226.4,  230.6, 1192.8, 2530.0,  228.4, 2529.9]
    dMasses[(240,  300)] = [ 225.2,  253.3,  313.9,  664.3,  243.2,  664.2]
    dMasses[(240,  400)] = [ 236.5,  252.7,  404.6,  873.2,  245.7,  873.2]
    dMasses[(240,  500)] = [ 240.6,  252.3,  501.1, 1082.3,  246.9, 1082.3]
    dMasses[(240,  600)] = [ 242.8,  252.0,  599.1, 1290.9,  247.6, 1290.9]
    dMasses[(240,  800)] = [ 245.0,  251.6,  796.5, 1706.2,  248.4, 1706.2]
    dMasses[(240, 1000)] = [ 246.2,  251.4,  994.5, 2119.1,  248.8, 2119.1]
    dMasses[(240, 1200)] = [ 247.0,  251.2, 1192.8, 2529.9,  249.1, 2529.9]

    for key, value in dMasses.iteritems():
        if lMasses == value:
            return key

    raise ValueError('The higgsino masses {} could not be found in the '
                     'dictionary.'
                     .format(', '.join(str(x) for x in lMasses)))
