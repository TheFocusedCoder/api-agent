# Landing Page Critique API

This API scrapes the landing page of a given URL, analyzes the copywriting using OpenAI's GPT-4, and returns a critique in JSON format.

## Project Structure

```
service_landing_page_critique_api/
├── main.py
├── pyproject.toml
└── README.md
```

## Installation

1. Clone this repository
2. Navigate to the project directory
3. Install dependencies using Poetry:

```bash
poetry install
```

## How to Run with Modal

1. Make sure you have Modal CLI installed and configured:

```bash
pip install modal
modal token new
```

2. Set up your OpenAI API key as a Modal secret:

```bash
modal secret create openai-api-key OPENAI_API_KEY=your_api_key_here
```

3. Deploy the API:

```bash
modal deploy main.py
```

4. To run the API locally for testing:

```bash
modal run main.py
```

The API will be accessible at the URL provided by Modal after deployment.