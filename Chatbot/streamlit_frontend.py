# adding a streamlit frontend to the basic chatbot
import streamlit as st
from basic_chatbot import workflow
from langchain_core.messages import HumanMessage

# st.session_state -> dict ->

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

# message_history=[] --> if it is initialized like this for every run this list gets empty
# first load conversation history and display till then's data
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# take user input
user_input=st.chat_input('Type Here')

# append 
if user_input:
    #  frist add the msg to msseage_history
    st.session_state['message_history'].append({'role': 'user' , 'content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    
    config = {'configurable': {'thread_id': '1'}}
    response = workflow.invoke({'messages': [HumanMessage(content=user_input)]}, config=config)
    ai_message=response['messages'][-1].content

    # add the msg to message_history
    st.session_state['message_history'].append({'role': 'assistant' , 'content':ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)