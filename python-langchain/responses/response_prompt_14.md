User: Add a Tool object to the tools list that:
- Has name="get_current_time"
- Uses the get_current_time function as func
- Has a description explaining when to use it
- Keep the Calculator tool in the list as well

GitHub Copilot: Read [](file:///c%3A/Users/mikdo/CodeYou/ai-agent-lab/python-langchain/app.py#1-1), lines 1 to 80

Read [](file:///c%3A/Users/mikdo/CodeYou/ai-agent-lab/python-langchain/app.py)

Replacing 33 lines with 55 lines in [](file:///c%3A/Users/mikdo/CodeYou/ai-agent-lab/python-langchain/app.py)


```

```


Read [](file:///c%3A/Users/mikdo/CodeYou/ai-agent-lab/python-langchain/app.py#1-1), lines 1 to 80

Perfect! I've successfully made the changes:

1. ✅ **Added `get_current_time()` function** - Takes a string input parameter and returns the current date/time using `datetime.now().strftime("%Y-%m-%d %H:%M:%S")`

2. ✅ **Updated tools list** - Now includes both:
   - **Calculator tool** - Uncommented and ready to use for math expressions
   - **get_current_time tool** - New tool that provides the current date and time with a clear description of when to use it

Both tools are now available in your agent's tools list, so the AI can call either one when appropriate for the user's query.

Made changes.