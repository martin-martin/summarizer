# Summarizer

Example scaffolding for a Python text completion project that uses the GPT-4 through the OpenAI API.

## Setup

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your-api-key
```

You can generate your [API key](https://platform.openai.com/account/api-keys) in your OpenAI account settings.

Move the `.env` file into the `summarizer/` package folder.

## Install

```bash
(venv) $ python -m pip install -r requirements.txt
(venv) $ python -m pip install -e .
```

## Usage

```bash
(venv) $ python summarizer --help
usage: summarizer [-h] [--file FILE]

Summarize text using the OpenAI API

options:
  -h, --help   show this help message and exit
  --file FILE  Path to file with text to summarize
```

Read text content from a file and receive the summary in your console:

```bash
(venv) $ python summarizer --file test.md
```
