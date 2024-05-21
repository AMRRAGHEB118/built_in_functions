def string_repeat(string: str, number: int = 2, sep: str = "", start_str: str = "", end_str: str = "") -> str:
    """
    Repeat the given string a specified number of times, with optional separator, start, and end strings.

    Args:
        string (str): The string to repeat.
        number (int, optional): The number of times to repeat the string. Defaults to 2.
        sep (str, optional): The separator to use between repeated strings. Defaults to "".
        start_str (str, optional): The string to prepend at the beginning. Defaults to "".
        end_str (str, optional): The string to append at the end. Defaults to "".

    Raises:
        TypeError: If number is not an integer or if any of the inputs are not strings.
        ValueError: If number < 0.

    Returns:
        str: The resulting string after repeating.
    """

    if not isinstance(number, int):
        raise TypeError("Invalid number of times to repeat. Must be an integer.")

    if not all(isinstance(s, str) for s in [string, sep, start_str, end_str]):
        raise TypeError("Invalid input. string, sep, start_str, and end_str must be strings.")

    if number < 0:
        raise ValueError("Invalid number of times to repeat. Must be a positive integer or 0.")

    if string == '':
        return ''
    return start_str + sep.join([string] * number) + end_str
