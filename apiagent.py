import os
from pathlib import Path
from langchain_anthropic import ChatAnthropic
import controlflow as cf
import controlflow.tools.code
import controlflow.tools.filesystem
from pydantic import BaseModel



# Swap to Anthropic from OpenAI in controlflow
model  = ChatAnthropic(
    model_name='claude-3-5-sonnet-20240620', 
    temperature=0.0, 
) 

# load the instructions
instructions = open(Path(__file__).parent / "instructions.md").read()

# create the agent
agent = cf.Agent(
    "API Agent",
    instructions=instructions,
    tools=[
        *controlflow.tools.filesystem.ALL_TOOLS,
        controlflow.tools.code.python,
        controlflow.tools.code.shell,
    ],
    model=model
)


class DesignDoc(BaseModel):
    goals: str
    design: str
    implementation_details: str
    criteria: str


@cf.flow(agents=[agent])
def run_agent():

    # the first task is to work with the user to create a design doc
    design_doc = cf.Task(
        "Learn about the API the user wants to build",
        instructions="""
                Interact with the user to understand the API they want to
                build. What is its purpose? 
                What does it need to do? Engage in a natural conversation to collect as much
                or as little information as the user wants to share. Once you have
                enough, write out a design document to complete the task.
                """,
        user_access=True,
        result_type=DesignDoc,
    )

    # next we create a directory for any files
    mkdir = cf.Task(
        "Create a directory for the API",
        instructions="""
            Create a directory to store the API and any related files.
            The directory should be named after the API. Return the path.
            """,
        result_type=str,
        tools=[controlflow.tools.filesystem.mkdir],
        agents=[agent],
    )

    # the final task is to write the API
    api = cf.Task(
        "Finish the API",
        instructions="""
            Mark this task complete when the api runs as expected and the
            user can invoke it. Until then, continue to build the API.

            All files must be written to the provided root directory.
            """,
        result_type=None,
        context=dict(design_doc=design_doc, root_dir=mkdir),
        agents=[agent],
    )
    return api


if __name__ == "__main__":
    run_agent()
    