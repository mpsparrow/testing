# testing/main.py


class Object:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        """Gets name

        Returns:
            str: name
        """
        return self.name


def adding(num1: int, num2: int) -> int:
    """Sums two numbers

    Args:
        num1 (int): first number
        num2 (int): second number

    Returns:
        int: Sum of numbers
    """
    return num1 + num2
