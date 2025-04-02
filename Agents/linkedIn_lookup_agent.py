# importing libraries
import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain import hub
from agent_tools.tools import get_profile_url_tavily
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)

# loading env file
load_dotenv(override=True)
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


def lookup(name: str):
    llm = ChatOpenAI(
        temperature=0,
        model='gpt-4o-mini'
    )

    template = 'given the full name {name_of_person} i want to you to get me a link to their linkedin profile page your answer should contain only a URL'

    prompt_template = PromptTemplate(
        input_variables=['name_of_person'],
        template=template
    )
    tools_for_agent = [
        Tool(
            name = "Crawl google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description = 'useful when you need to get the linkedin  page url'
        )
    ]

    react_prompt = hub.pull('hwchase17/react')
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_exe = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_exe.invoke(
        input={'input':prompt_template.format(name_of_person=name)}
    )

    linked_profile_url = result['output']
    return linked_profile_url

if __name__ == '__main__':
    lookup('Sunil Gorintla')