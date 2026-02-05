(venv) C:\Users\mikdo\CodeYou\ai-agent-lab\python-langchain>python app.py
C:\Users\mikdo\CodeYou\ai-agent-lab\venv\Lib\site-packages\langchain_core\_api\deprecation.py:25: UserWarning: Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.
  from pydantic.v1.fields import FieldInfo as FieldInfoV1
🤖 Python LangChain Agent Starting...
✅ GitHub token loaded successfully!

Running example queries:

📝 Query: What time is it right now?
──────────────────────────────────────────────────
Agent is calling tools...
  📌 Tool: get_current_time
  📌 Input: {'__arg1': ''}
  📌 Result: 2026-02-05 10:07:17


📝 Query: What is 25 * 4 + 10?
──────────────────────────────────────────────────
Agent is calling tools...
  📌 Tool: Calculator
  📌 Input: {'__arg1': '25 * 4 + 10'}
  📌 Result: 110


📝 Query: Reverse the string 'Hello World'
──────────────────────────────────────────────────
Agent is calling tools...
  📌 Tool: reverse_string
  📌 Input: {'__arg1': 'Hello World'}
  📌 Result: dlroW olleH


🎉 Agent demo complete!