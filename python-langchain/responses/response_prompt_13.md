User: In app.py Before the main() function, create a get_current_time function that:
- Takes a string input parameter (required by Tool interface)
- Has a docstring explaining it returns the current date and time
- Uses datetime.now().strftime("%Y-%m-%d %H:%M:%S")
- Returns the formatted string

GitHub Copilot: Read [](file:///c%3A/Users/mikdo/CodeYouAIClass2026Unit3/python-langchain/app.py)

Good news! The `get_current_time` function is already implemented in your app.py file. Here's what's there:

```python
def get_current_time(input: str) -> str:
    """Returns the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

This function meets all the requirements:
- ✅ Takes a string input parameter (required by Tool interface)
- ✅ Has a docstring explaining it returns the current date and time
- ✅ Uses `datetime.now().strftime("%Y-%m-%d %H:%M:%S")`
- ✅ Returns the formatted string

The function is correctly positioned before the `main()` function and the necessary `datetime` import is already included at the top of the file. It's ready to be used as a tool in your agent!