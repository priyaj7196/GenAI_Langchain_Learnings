from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
# definining input prompts
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']  
)
prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary of the report on \n {text}',
    input_variables=['text']  
)

# defining the model
model=ChatOpenAI()

# defining the output parser
parser= StrOutputParser()

chain= prompt1 | model | parser | prompt2 | model | parser
result=chain.invoke({'topic':'Education System in India'})

print(result)

chain.get_graph().print_ascii() #print the graph of the chain
