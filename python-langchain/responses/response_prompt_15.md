User: Replace the query with: "Reverse the string 'Hello World'"
Comment out both the Calculator and Time tools
Run the application and observe that the AI attempts to reverse the string but may not be reliable

GitHub Copilot: Read [](file:///c%3A/Users/mikdo/CodeYou/ai-agent-lab/python-langchain/app.py#70-70), lines 70 to 140

Replacing 20 lines with 20 lines in [](file:///c%3A/Users/mikdo/CodeYou/ai-agent-lab/python-langchain/app.py)


```

```


Ran terminal command: C:/Users/mikdo/CodeYou/ai-agent-lab/venv/Scripts/python.exe python-langchain/app.py

Perfect! The changes have been completed and the application ran successfully. Here's what we can observe:

## Changes Made:
1. ✅ **Replaced the query** with: `"Reverse the string 'Hello World'"`
2. ✅ **Commented out both tools** - Calculator and get_current_time are now disabled

## Execution Result:
```
📝 Query: Reverse the string 'Hello World'

Response content: The reverse of the string "Hello World" is:

**"dlroW olleH"**

✅ Agent completed successfully
```

## Observation:
The AI attempted to reverse the string **without any dedicated tool** and produced the correct result: `"dlroW olleH"`. However, this demonstrates an important point:

- **Without a tool**: The AI relies on its training data and knowledge to attempt the task. While it succeeded here, this approach can be:
  - Less reliable for edge cases
  - Not guaranteed for all inputs
  - Slower as it must reason through the problem
  
- **With a tool**: A dedicated `reverse_string()` tool would guarantee accuracy and consistency for this operation

This is exactly the lesson of this exercise—tools provide reliable, deterministic execution of specific tasks, which is more dependable than asking the AI to handle everything through reasoning alone.

Made changes.