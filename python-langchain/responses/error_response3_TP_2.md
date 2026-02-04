
python app.py
C:\Users\mikdo\CodeYou\ai-agent-lab\venv\Lib\site-packages\langchain_core_api\deprecation.py:25: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
from pydantic.v1.fields import FieldInfo as FieldInfoV1
Traceback (most recent call last):
File "C:\Users\mikdo\CodeYou\ai-agent-lab\python-langchain\app.py", line 6, in <module>
from langchain.agents.agent import AgentExecutor
ModuleNotFoundError: No module named 'langchain.agents.agent'

Let me simplify this to use a working approach without AgentExecutor:

Edited
app.py+1-1
Edited
app.py+28-9
I've simplified the code to remove the problematic AgentExecutor import and instead use a direct chain approach with manual tool calling. The new approach:

Removes the incompatible AgentExecutor import
Uses llm.bind_tools() to enable tool calling on the LLM
Creates a simple chain: prompt | llm_with_tools
Manually processes tool calls from the LLM response
Includes better error handling with traceback
Try running the app again—this should work with your current LangChain version.