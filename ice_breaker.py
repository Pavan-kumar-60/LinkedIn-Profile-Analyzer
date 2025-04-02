# importing all the necessary libraries
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAI
from third_parties.linkedin import scrape_linkedin_profile
from Agents.linkedIn_lookup_agent import lookup
from outputparser import summary_parser

def ice_break_with(name:str):

    url = lookup(name)
    linkedin_data = scrape_linkedin_profile(url)

    summary_template = """
         given the information about a person from linkedin {information} I want you to create:
         1. a short summary
         2. two interesting facts about them
         \n{format_instructions}
     """

    summary_prompt_template = PromptTemplate(input_variables=['information'],template=summary_template,partial_variables={"format_instructions": summary_parser.get_format_instructions()})

    llm = ChatOpenAI(temperature=0, model='gpt-4o-mini')
    chain = summary_prompt_template | llm | summary_parser
 
    result= chain.invoke(input={'information': linkedin_data})
    return result, linkedin_data.get('photoUrl')

    


if __name__ == '__main__':
    load_dotenv()
    ice_break_with('Sunil Gorintla')
