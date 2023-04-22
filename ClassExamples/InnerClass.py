def uppercase_string(string, custom_formatter=None):
    """Function that has a default value to format a string.
    A custom formatter can be provided as long as it takes
    exactly one str as parameter"""

    class DefaultStringFormatter:
        """Format a string in uppercase."""
        def __init__(self, format_string):
            self.format_string = format_string

        def format(self, format_string):
            self.format_string = format_string
            return str(self.format_string).upper()

    if not custom_formatter:
        custom_formatter = DefaultStringFormatter(string)

    return custom_formatter.format(string)


if __name__ == '__main__':
    hello_string = "hello world, how are you today?"
    print(" input: " + hello_string)
    print("output: " + uppercase_string(hello_string))
