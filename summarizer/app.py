from pathlib import Path
import tomllib
from typing import List

import openai

SECRETS_PATH = Path.cwd() / "summarizer" / "secrets.toml"
SETTINGS_PATH = Path.cwd() / "summarizer" / "settings.toml"

with SECRETS_PATH.open(mode="rb") as secrets_file:
    secrets = tomllib.load(secrets_file)
    openai.api_key = secrets["OPENAI"]["api_key"]

with SETTINGS_PATH.open(mode="rb") as fp:
    config = tomllib.load(fp)

MODEL = config["general"]["model"]  # gpt-4
ROLE_PROMPT = config["prompts"]["role_prompt"]
INSTRUCTIONS = config["prompts"]["instructions"]


def _read_input_text(input_file: str) -> str:
    """Read the text content that should be summarized from a file."""
    input_file_path = Path(input_file)
    with input_file_path.open("r") as file:
        content = file.read()
    return content

def _assemble_messages(content: str) -> List[dict]:
    """Combine all messages into a well-formatted dictionary."""
    messages = [
        {"role": "system", "content": ROLE_PROMPT},
        {"role": "user", "content": f"CONTENT START>>>{content}<<<CONTENT END\n\n"},
        {"role": "user", "content": INSTRUCTIONS},
    ]
    return messages

def summarize(file: str, model: str = MODEL) -> str:
    """Assemble all prompts and send the API request."""
    content = _read_input_text(file)
    messages = _assemble_messages(content)

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
    )
    return response["choices"][0]["message"]["content"]
