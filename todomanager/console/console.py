from typing import Callable, List
from rich.console import Console
from rich.text import Text


class ConsoleManager:
    _instance = None

    @staticmethod
    def get_instance():
        """
        Gets a instance of the Console object from the rich library.
        """
        if ConsoleManager._instance is None:
            ConsoleManager._instance = Console()
        return ConsoleManager._instance

    @staticmethod
    def input_string(
        text: str,
        error_message: str = "Neplatný vstup, zkuste to prosím znova.",
        conditions: List[Callable[[str], bool]] = None,
    ) -> str:
        """
        Prompts the user to input a string and  validates  it  against  optional
        conditions.

        Args:
            text (str): The prompt message displayed to the user.  error_message
            (str): The error message shown to the  user  when  input  fails  the
            validation. Defaults to 'Neplatný vstup, zkuste to  prosím  znova.'.
            conditions (List[Callable[[str], bool]]): A list of callables,  such
            as lambda functions, that define the validation rules. Each callable
            takes a string as input and returns a bool

        Returns:
            str: The validated input string provided by the user.
        """
        while True:
            console = ConsoleManager.get_instance()
            try:
                # Prompt the user to enter a string.
                string = console.input(text)

                # Validate against conditions if provided.
                if conditions and not all(condition(string) for condition in conditions):
                    console.print(error_message, style="italic red")
                    continue

                # Return the valid string.
                return string
            except ValueError:
                console.print(error_message, style="italic red")

    @staticmethod
    def input_int(text: str, error_message: str = "Neplatný vstup, zkuste to prosím znova.", conditions: List[Callable[[int], bool]] = None) -> int:
        """
        Prompts the user to input a int number and validates it against optional
        conditions.

        Args:
            text (str): The prompt message displayed to the user.
            error_message (str): The error message shown to the user when  input
            fails the validation. Defaults to 'Neplatný vstup, zkuste to  prosím
            znova.'.
            conditions (List[Callable[[int], bool]]): A list of callables,  such
            as lambda functions, that define the validation rules. Each callable
            takes a int as input and returns a bool

        Returns:
           int: The validated input number provided by the user.
        """
        while True:
            console = ConsoleManager.get_instance()
            try:
                # Prompt the user to enter a number.
                number = int(console.input(text))

                # Validate against conditions if provided.
                if conditions and not all(condition(number) for condition in conditions):
                    console.print(error_message, style="italic red")
                    continue

                # Return the valid number.
                return number
            except ValueError:
                console.print(error_message, style="italic red")

    @staticmethod
    def print_divider(width: int = 105, text: str = None, text_style: str = "bold green") -> None:
        """
        Prints a styled divider line to the console,  optionally  with  centered
        text.

        Args:
            width (int, optional): The total width of the divider line. Defaults
            to 105.
            text (str, optional): The text to center within  the  divider  line.
            Defaults to None.
            text_style (str, optional): The style to apply to the centered text.

        Returns:
            None: This function prints directly to  the  console  and  does  not
            return a value.
        """
        console = ConsoleManager().get_instance()

        base_line = Text("-" * width, style="bold white")

        if text:
            # Calculate padding.
            text_length = len(text)
            padding = (width - text_length - 2) // 2  # Subtract 2 for spacing around the text.

            # Create the line with centered text
            styled_line = Text("-" * padding + f" {text} " + "-" * (width - padding - text_length - 2))

            # Add the padding.
            styled_line.stylize(text_style, padding + 1, padding + 1 + text_length)
        else:
            styled_line = base_line

        console.print(styled_line)

    @staticmethod
    def clear_console() -> None:
        """
        Clears the console.
        """
        console = ConsoleManager().get_instance()
        console.clear()

    @staticmethod
    def print_intro_ascii_logo() -> None:
        """
        Prints a ASCII logo text to the console.
        """
        console = ConsoleManager.get_instance()
        console.print(
            """
 ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀█▄▄   ▄▀▀▀▀▄       ▄▀▀▄ ▄▀▄  ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀█▄   ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
█    █  ▐ █      █ █ ▄▀   █ █      █     █  █ ▀  █ ▐ ▄▀ ▀▄ █  █ █ █ ▐ ▄▀ ▀▄ █        ▐  ▄▀   ▐ █   █   █ 
▐   █     █      █ ▐ █    █ █      █     ▐  █    █   █▄▄▄█ ▐  █  ▀█   █▄▄▄█ █    ▀▄▄   █▄▄▄▄▄  ▐  █▀▀█▀  
   █      ▀▄    ▄▀   █    █ ▀▄    ▄▀       █    █   ▄▀   █   █   █   ▄▀   █ █     █ █  █    ▌   ▄▀    █  
 ▄▀         ▀▀▀▀    ▄▀▄▄▄▄▀   ▀▀▀▀       ▄▀   ▄▀   █   ▄▀  ▄▀   █   █   ▄▀  ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄   █     █   
█                  █     ▐               █    █    ▐   ▐   █    ▐   ▐   ▐   ▐         █    ▐   ▐     ▐   
▐                  ▐                     ▐    ▐            ▐                          ▐                  
            """,
            style="bright_green",
        )

    @staticmethod
    def print_error_ascii_logo() -> None:
        """
        Prints a ASCII error text to the console.
        """
        console = ConsoleManager.get_instance()
        console.print(
            """
 ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄ 
▐  ▄▀   ▐ █   █   █ █   █   █ █      █ █   █   █ 
  █▄▄▄▄▄  ▐  █▀▀█▀  ▐  █▀▀█▀  █      █ ▐  █▀▀█▀  
  █    ▌   ▄▀    █   ▄▀    █  ▀▄    ▄▀  ▄▀    █  
 ▄▀▄▄▄▄   █     █   █     █     ▀▀▀▀   █     █   
 █    ▐   ▐     ▐   ▐     ▐            ▐     ▐   
 ▐                                               
            """,
            style="bright_red",
        )
