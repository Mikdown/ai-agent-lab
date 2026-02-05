User: Replace the single query with a list of test queries:
- "What time is it right now?"
- "What is 25 * 4 + 10?"
- "Reverse the string 'Hello World'"

Add a for loop that:
- Prints "Running example queries:" before the loop
- Iterates through each query
- Prints the query with formatting (📝 emoji and separator line)
- Calls agent_executor.invoke() for each query
- Prints the result with formatting (✅ emoji)
- Includes try-catch error handling for each query (❌ emoji for errors)

GitHub Copilot: Read [](file:///c%3A/Users/mikdo/CodeYou/ai-agent-lab/python-langchain/app.py#110-110), lines 110 to 156

Read [](file:///c%3A/Users/mikdo/CodeYou/ai-agent-lab/python-langchain/app.py#150-150), lines 150 to 161

Replacing 33 lines with 43 lines in [](file:///c%3A/Users/mikdo/CodeYou/ai-agent-lab/python-langchain/app.py)


```

```
Perfect! I've updated the app.py file to include:

✅ **List of three test queries**:
- "What time is it right now?"
- "What is 25 * 4 + 10?"
- "Reverse the string 'Hello World'"

✅ **For loop with**:
- "Running example queries:" printed before the loop
- Iteration through each query
- Formatted output with 📝 emoji and separator lines (─ * 50)
- agent_chain.invoke() called for each query
- Results printed with ✅ emoji
- Try-catch error handling with ❌ emoji for errors
- Proper spacing between queries

The agent will now test all three queries sequentially, demonstrating its ability to use different tools (Calculator, get_current_time, and reverse_string) as needed for each query.

Made changes.