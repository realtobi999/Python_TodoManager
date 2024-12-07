from typing import Callable, List
from rich.console import Console
from rich.text import Text


class ConsoleManager:
    _instance = None

    @staticmethod
    def get_instance():
        if ConsoleManager._instance is None:
            ConsoleManager._instance = Console()
        return ConsoleManager._instance

    @staticmethod
    def input_string(
        text: str,
        error_message: str = "Neplatný vstup, zkuste to prosím znova.",
        conditions: List[Callable[[str], bool]] = [],
    ) -> str:
        while True:
            console = ConsoleManager.get_instance()
            try:
                # prompt the user to enter a string
                string = console.input(text)

                # validate against conditions if provided
                if not all(condition(string) for condition in conditions):
                    console.print(error_message, style="italic red")
                    continue

                # return the valid string
                return string
            except ValueError:
                console.print(error_message, style="italic red")

    @staticmethod
    def input_int(text: str, error_message: str = "Neplatný vstup, zkuste to prosím znova.", conditions: List[Callable[[int], bool]] = []) -> int:
        while True:
            console = ConsoleManager.get_instance()
            try:
                # prompt the user to enter a number
                number = int(console.input(text))

                # validate against conditions if provided
                if not all(condition(number) for condition in conditions):
                    console.print(error_message, style="italic red")
                    continue

                # return the valid number
                return number
            except ValueError:
                console.print(error_message, style="italic red")

    @staticmethod
    def print_intro_ascii_logo() -> None:
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

    @staticmethod
    def print_divider(width: int = 105, text: str = None, text_style: str = "bold green") -> None:
        console = ConsoleManager().get_instance()

        base_line = Text("-" * width, style="bold white")

        if text:
            # calculate padding
            text_length = len(text)
            padding = (width - text_length - 2) // 2  # subtract 2 for spacing around the text

            # create the line with centered text
            styled_line = Text("-" * padding + f" {text} " + "-" * (width - padding - text_length - 2))

            styled_line.stylize(text_style, padding + 1, padding + 1 + text_length)
        else:
            styled_line = base_line

        console.print(styled_line)
