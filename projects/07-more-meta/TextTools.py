"""
Text Tools

This module offers helper tools for putting nice text on terminal outputs
"""


def print_head(text: str, width: int = 80):
    """
    Prints a boxed headline.
    :param text: the text to put in the box
    :param width: the width in characters of the headline
    :returns: None

    Example:
    >>> print_head('headline', 40)
    ########################################
    #               headline               #
    ########################################
    """

    formattext = "{" + f":^{width - 4}" + "}"  # e.g. "{:^36}"

    print("#" * width)
    print("# " + formattext.format(text) + " #")
    print("#" * width)


def print_decobar(width: int = 80):
    """
    Prints a one-line wave of defined width on screen
    :param width: The number of characters the decoline should have
    :returns: None
    """

    sequence = "°º¤ø,¸¸,ø¤º°`"  # source: https://1lineart.kulaone.com/#/
    full_sequences, remainder = divmod(width, len(sequence))

    print(sequence * full_sequences, sequence[:remainder], sep="")
