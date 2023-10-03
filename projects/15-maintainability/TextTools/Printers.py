import sys


def print_head(text, width=80, file=sys.stdout):
    """
    Prints a boxed headline.
    :param text: the text to put in the box
    :param width: the width in characters of the headline
    :param file: the file stream in which this message should be written. Default: on screen
    :returns: None

    Example:
    >>> print_head('headline', 40)
    ########################################
    #               headline               #
    ########################################
    """

    formattext = "{" + f":^{width - 4}" + "}"  # e.g. "{:^36}"
    print("#" * width, file=file)
    print("# " + formattext.format(text) + " #", file=file)
    print("#" * width, file=file)


def print_decobar(width: int = 80, file=sys.stdout):
    """
    Prints a one-line wave of defined width on screen
    :param width: The number of characters the decoline should have
    :param file: the file stream in which this message should be written. Default: on screen
    :returns: None
    """

    sequence = "°º¤ø,¸¸,ø¤º°`"  # source: https://1lineart.kulaone.com/#/
    full_sequences, remainder = divmod(width, len(sequence))

    print(sequence * full_sequences, sequence[:remainder], sep="", file=file)
