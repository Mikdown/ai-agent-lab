>python app.py
C:\Users\mikdo\CodeYou\ai-agent-lab\venv\Lib\site-packages\langchain_core\_api\deprecation.py:25: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
  from pydantic.v1.fields import FieldInfo as FieldInfoV1  
Traceback (most recent call last):
  File "C:\Users\mikdo\CodeYou\ai-agent-lab\python-langchain\app.py", line 6, in <module>
    from langchain.agents import AgentExecutor
ImportError: cannot import name 'AgentExecutor' from 'langchain.agents' (C:\Users\mikdo\CodeYou\ai-agent-lab\venv\Lib\site-packages\langchain\agents\__init__.py)

Fixed the import - I've changed from langchain.agents import AgentExecutor to from langchain.agents.agent import AgentExecutor. Try running the app again.