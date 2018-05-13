def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    if get_length(nucleotide) == 0:
        return 0
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    >>> contains_sequence('ATCGGC', '')
    False
    """
    if get_length(dna2) == 0:
        return False
    return dna2 in dna1


def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if dna contains only A, T, C and G.

    >>> is_valid_sequence("ATCGAT")
    True
    >>> is_valid_sequence("ATcG")
    False
    >>> is_valid_sequence("")
    False
    '''
    valid_nucleotide = 'ATCG'
    if get_length(dna) == 0:
        return False
    for nucleotide in dna:
        if nucleotide not in valid_nucleotide:
            return False
    return True


def insert_sequence(dna1, dna2, position):
    ''' (str, str, int) -> str

    Inserts dna2 into dna1 at position and returns the result.

    >>> insert_sequence("CCGG", "AT", 2)
    "CCATGG"
    >>> insert_sequence("AAA", "TT", 0)
    "TTAAA"
    >>> insert_sequence("AAA", "TT", 3)
    "AAATT"
    '''
    return dna1[:position] + dna2 + dna1[position:]

def get_complement(nucleotide):
    ''' (str) -> str

    Returns the complement of nucleotide. A <-> T and C <-> G

    >>> get_complement("A")
    "T"
    >>> get_complement("T")
    "A"
    >>> get_complement("G")
    "C"
    >>> get_complement("C")
    "G"
    >>> get_complement("")
    ""
    '''
    if not is_valid_sequence(nucleotide):
        return ""
    if nucleotide == "A":
        return "T"
    elif nucleotide == "T":
        return "A"
    elif nucleotide == "C":
        return "G"
    else:
        return "C"

def get_complementary_sequence(dna):
    ''' (str) -> str

    Returns the complementary sequence of dna

    >>> get_complementary_sequence("AT")
    "TA"
    >>> get_complementary_sequence("CG")
    "GC"
    >>> get_complementary_sequence("ATCG")
    "TAGC"
    >>> get_complementary_sequence("ATCGca")
    ""
    '''
    complementary = ""
    if not is_valid_sequence(dna):
        return ""
    for nucleotide in dna:
        complementary = complementary + get_complement(nucleotide)
    return complementary
