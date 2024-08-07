# API-Agent

![Experimental](https://img.shields.io/badge/Status-Experimental-yellow)    


API-Agent is a powerful tool designed to create micro Python APIs faster by leveraging the Claude 3.5 Sonnet model. This project aims to streamline the API development process by using AI to generate code based on user prompts.


## Features

- Supports rapid API prototyping
- Generates project structure, including Dockerfile and necessary configuration files
- Generates code for endpoints and custom logic


## Getting Started

The easiest way to get started with API-Agent is by using GitHub Codespaces or a Dev Container. This ensures you have a consistent development environment with all the necessary dependencies pre-installed.


### Quick Start with GitHub Codespaces

You can quickly set up and start using API-Agent with GitHub Codespaces. Just click the button below to open this project in a Codespace:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=839018747)

This will create a new Codespace with all the necessary dependencies and configurations pre-installed, allowing you to start using API-Agent right away.



### Using Dev Containers with VsCode or Cursor

1. Clone the repository or fork it to your GitHub account.
2. Open the repository in VS Code with the Dev Containers extension installed.
3. VS Code or Cursor will detect the Dev Container configuration in the `.devcontainer` folder and prompt you to reopen the project in a container. Click "Reopen in Container" to proceed.
4. The development environment will be automatically set up based on the configuration in the `.devcontainer` folder.

For more information on using Dev Containers, refer to the [official documentation](https://code.visualstudio.com/docs/devcontainers/containers).

### Run API Agent Locally
⚠️ **Warning**: API-Agent has access to the file system and can perform remote code execution. It is strongly recommended to run it in a sandboxed environment or in a container.

1. Clone the repository
    ```
    git clone https://github.com/tfcbot/api-agent.git
    cd api-agent
    ```
2. Install dependencies listed in devcontainer.json. 

## Start the API Agent

1. Install dependencies using Poetry:
    ```
    poetry install
    ```


2. Start a virtual environment
    ```
    poetry shell
    ```


2. Set up your ANTHROPIC API key. ControlFlow expects OPENAI_API_KEY to be set so we need to set CONTROLFLOW_LLM_MODEL to use the Claude model.
    ```
    export export CONTROLFLOW_LLM_MODEL="anthropic/claude-3-5-sonnet-20240620"
    export ANTHROPIC_API_KEY=<your-api-key>
    ```

3. Run the agent
    ```
    python apiagent.py
    ```
    
The agent will start and prompt you for the API you want to build. Follow the prompts to describe the API you want to build. The Agent will guide you through the process and generate the necessary code.

## Prompt Best Practices

When describing your API requirements:
- Be specific about the endpoints you want
- Provide hints about implementation details such as libraries to use and steps to take
- Refer to the example prompts in the `example-prompts` directory for guidance


See the example prompts for what is working. 

## Known Limitations 

This is a reference implementation meant for POCs, demos, and learning so there are some limitations. As of now there are no plans to add addtional features. 

- The API Agent may not always generate flawless code.
- API agent only supports Claude 3.5 Sonnet model. Other LLMs can be configured by modifying apiagent.py. 
- Creating complex APIs with multiple endpoints (5+) and custom logic can be challenging for the Agent. Start with simple APIs and build up from there. 
- The Agent works on completing one prompt and cannot be interrupted. 
- It is best to build stateless APIs that do not require complex database queries

If you want to build a more complex API, consider using the [Software Engineer Agent](https://controlflow.ai/examples/agent-engineer) which this agent is based on. 


## Acknowledgements

[ControlFlow](https://controlflow.ai/) for building predicatable agents. 

[FastAPI](https://fastapi.tiangolo.com/) for simple and fast API development. 

[Poetry](https://python-poetry.org/) for great dependency management. 

[LangChain](https://python.langchain.com/docs/get_started/introduction) for managing llms.

[Claude 3.5 Sonnet](https://docs.anthropic.com/claude-3-sonnet/reference/claude-3-sonnet-model-parameters) for generating code. 


[![Sponsored by the Agent Developer Toolkit](https://img.shields.io/badge/Sponsored%20by-The%20Agent%20Developer%20Toolkit-blue?style=for-the-badge)](https://swiy.co/agent-toolkit)

