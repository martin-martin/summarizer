import argparse

from app import summarize


def main() -> None:
    args = cli_prompt()
    print("Summarizing...")
    print(summarize(args.file))


def cli_prompt() -> argparse.Namespace:
    """Parse the arguments provided through the CLI."""
    parser = argparse.ArgumentParser(
        description="Summarize text with OpenAI's API"
    )
    parser.add_argument("--file", help="Path to file with text to summarize")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
