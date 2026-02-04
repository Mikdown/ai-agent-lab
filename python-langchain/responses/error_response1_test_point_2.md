Error code: 400 - {'error': {'message': "Invalid 'messages': empty array. Expected an array with minimum length 1, but got an empty array instead.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'empty_array'}}

Read Python source code file
The issue is that create_agent needs a proper prompt template. Let me fix this by using create_tool_calling_agent instead, which is the modern approach for LangChain:

Edited
app.py+2-1
Edited
app.py+9-1
I've fixed the error by updating the agent creation to use  create_tool_calling_agent with a proper ChatPromptTemplate. The issue was that the original create_agent function requires a prompt template to avoid sending empty messages to the API.

The changes include:

Updated imports to use create_tool_calling_agent and AgentExecutor
Added ChatPromptTemplate import
Created a proper prompt template with system and human message roles
Used create_tool_calling_agent() to build the agent with the prompt
Used AgentExecutor to run the agent with verbose output
Try running the app again—it should now properly invoke the calculator tool for the math query.

>python app.py
C:\Users\mikdo\CodeYou\ai-agent-lab\venv\Lib\site-packages\langchain_core\_api\deprecation.py:25: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
  from pydantic.v1.fields import FieldInfo as FieldInfoV1  
Traceback (most recent call last):
  File "C:\Users\mikdo\CodeYou\ai-agent-lab\python-langchain\app.py", line 6, in <module>
    from langchain.agents import create_tool_calling_agent, AgentExecutor
ImportError: cannot import name 'create_tool_calling_agent' from 'langchain.agents' (C:\Users\mikdo\CodeYou\ai-agent-lab\venv\Lib\site-packages\langchain\agents\__init__.py)    

