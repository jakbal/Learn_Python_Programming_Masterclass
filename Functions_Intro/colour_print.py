import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, *effects: str) -> None:
    """
    Print `text` using ANSI sequences to change colour, etc

    :param text: the text to print
    :param effects: the effects we want. Zero or more of the constants
        defined and the start of this module.
    """
    effects_string = "".join(effects)
    output = "{0}{1}{2}".format(effects_string, text, RESET)
    print(output)

colorama.init()
colour_print("Hello, Red", RED)
colour_print("Hello, Red and Bolded", RED, BOLD)
colour_print("Hello, Red, Bolded and Reversed", RED, BOLD, REVERSE)
colorama.deinit()
