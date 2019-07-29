def do_FMLN_encoding(peplist, m=8, n=3):
    """
    First m last n. e.g. for FELT encoding, the default, m=8, n=3
    :param peplist: the list of peptides to encode
    :param m: use the first m residues
    :param n: concatenated with the last n residues
    :returns: encoded peptide list
    """
    return [p[0:m] + p[-n:] for p in peplist]


def do_5d_encoding(peplist):
    """
    5D encoding using amino acid multi dimensional scaling properties
    :param peplist: the list of peptides to encode
    :returns: encoded peptide list
    """
    e = []
    for p in peplist:
        d = []
        for c in p:
            d = d + aa5d[c]
        e.append(d)

    return e


aa5d = {
    "A": [0.354311, 3.76204, -11.0357, -0.648649, 2.82792],
    "R": [7.5734, -10.135, 2.48594, -4.29106, -5.6871],
    "N": [11.2937, 1.06685, 2.71827, 1.96258, -0.859314],
    "D": [13.4195, -1.60027, -0.325263, 3.7422, 2.43733],
    "C": [-5.84613, 4.88503, 1.62632, 9.39709, -5.84334],
    "Q": [6.59904, -5.16578, -0.696992, 0.582121, -1.74988],
    "E": [9.78784, -7.86097, -7.31842, 2.61123, 4.73404],
    "G": [9.65497, 15.7781, -0.557594, 0.299376, 1.65613],
    "H": [1.01864, -4.96926, 0.952556, 4.65696, -0.328102],
    "I": [-15.634, 1.99332, -2.04451, -3.24324, -1.67176],
    "L": [-11.8251, 0.505348, -6.15677, -4.55717, 3.21852],
    "K": [10.7622, -9.51739, -1.02226, -5.40541, -0.421845],
    "M": [-10.585, -3.95856, -3.60113, 5.33888, 1.20304],
    "F": [-14.571, -0.645723, 1.67278, -0.033264, 3.24977],
    "P": [7.66197, 8.02942, 9.45586, -3.57588, 5.99957],
    "S": [8.81349, 6.68183, -0.348496, -1.13098, -3.06228],
    "T": [3.01164, 4.12701, -0.348496, -2.19543, -4.28095],
    "W": [-13.1095, -5.22193, 9.03767, 1.38046, 4.6403],
    "Y": [-6.24473, -1.60027, 9.87406, -1.59667, -1.42177],
    "V": [-12.1352, 3.81819, -4.34459, -3.25988, -4.67154],
    "X": [0.0, 0.0, 0.0, 0.0, 0.0]
}
# note the final amino acid, X. this is in some of the test data (rarely though)
