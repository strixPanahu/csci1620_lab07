"""
    CSCI 1620 001/851
    Professor Owora
    Week 07 - Lab 07
    05/03/2024

    https://github.com/strixPanahu/csci1620_lab07
"""
from warnings import warn


def power(base_input, exponent):
    """
    Calculate power value,
    :param base_input: Base value to be calculated; differentiated as input for exception exactitude
    :param exponent: Raised exponent for the base
    :return: The solution of the base raised to the exponent provided
    """
    base = None
    try:
        base = int(base_input)
        exponent = int(exponent)
    except ValueError:
        if base is None:
            warn("Base value provided is not a whole numeric value")
        else:
            warn("Exponent value provided is not a whole numeric value.")
        return None

    if exponent < 0:
        return None
    elif exponent > 1:
        return base * power(base, exponent - 1)
    else:
        return base


def cat_ears(quantity):
    """
    Calculate cat ears
    :param quantity: Whole-value positive integer quantity of cats
    :return: Quantity of cat ears, based on the quantity of cats provided
    """
    try:
        quantity = int(quantity)
    except ValueError:
        warn("Exponent value provided is not a whole numeric value.")
        return None

    if quantity < 1:
        return 0
    else:
        return 2 + cat_ears(quantity - 1)


def alien_ears(quantity):
    """
    Calculate alien ears
    :param quantity: Whole-value positive integer quantity of aliens
    :return: Quantity of alien ears, based on the quantity of aliens provided
    """
    try:
        quantity = int(quantity)
    except ValueError:
        warn("Exponent value provided is not a whole numeric value.")
        return None

    if quantity < 1:
        return None
    if quantity == 1:
        return 3
    elif quantity % 2 == 0:  # if value is even
        return 2 + alien_ears(quantity - 1)
    else:  # if value is odd
        return 3 + alien_ears(quantity - 1)
