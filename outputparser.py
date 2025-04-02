from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Summary(BaseModel):
    Summary: str = Field(description= 'concise summary of a person')
    facts: list[str] = Field(description='facts about person')
    headline: str = Field(description= 'profession of the person')


    def to_dict(self):
        return {'summary': self.Summary, 'facts': self.facts, 'headline': self.headline}
    
summary_parser = PydanticOutputParser(pydantic_object=Summary)