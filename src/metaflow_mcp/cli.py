import sys

import typer
from rich.console import Console

from metaflow_mcp import __version__

app = typer.Typer(
    pretty_exceptions_show_locals=False,
    help="Metaflow MCP CLI tool",
    no_args_is_help=True,
)

console = Console(color_system="truecolor")


def version_callback(value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"metaflow-mcp version: {__version__}")
        raise typer.Exit(0)


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """Metaflow MCP CLI tool."""


def run() -> None:
    """Run the CLI application."""
    try:
        app()
    except typer.Exit:
        raise
    except (typer.BadParameter, typer.Abort) as e:
        console.print(f"[red]Error: {e!s}[/red]")
        sys.exit(1)
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user[/yellow]")
        sys.exit(130)
    except RuntimeError as e:
        console.print(f"[red]Runtime Error: {e!s}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    run()
