from rich.console import Console
from rich.text import Text


class ConsoleManager:
    _instance = None

    @staticmethod
    def get_instance():
        if ConsoleManager._instance is None:
            ConsoleManager._instance = Console()
        return ConsoleManager._instance


def print_ascii_logo() -> None:
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


def print_divider(width: int = 105, text: str = None, text_style: str = "bold green") -> None:
    console = Console()

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
