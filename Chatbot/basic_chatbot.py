from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph,START,END
from langchain_core.messages import BaseMessage,HumanMessage,AIMessage
from typing import TypedDict,Annotated

from langgraph.graph.message import add_messages

load_dotenv() #load data
llm=ChatOpenAI() #create llm object

class Chatstate(TypedDict): #define state class
    
    messages:Annotated[list[BaseMessage], add_messages]

def Chat_node(state: Chatstate):

    # extract user query from message
    query = state['messages']

    # call llm
    response = llm.invoke(query)
    
    # update chatstate of message
    return {'messages': [response]}

# defining and compiling the graph
graph=StateGraph(Chatstate)

graph.add_node('Chat_node',Chat_node)

graph.add_edge(START, 'Chat_node')
graph.add_edge('Chat_node', END)

checkpoint = InMemorySaver()
workflow = graph.compile(checkpointer=checkpoint)

