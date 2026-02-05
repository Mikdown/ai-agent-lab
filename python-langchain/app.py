import os
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
import json

def calculator(expression: str) -> str:
    """
    Evaluates mathematical expressions and returns the result.
    
    This function takes a mathematical expression as a string and evaluates it
    using Python's eval(). For demo purposes, it demonstrates basic tool
    functionality. In production, consider using safer alternatives like
    ast.literal_eval or a dedicated math parser library.
    
    Args:
        expression: A mathematical expression as a string (e.g., "25 * 4 + 10")
    
    Returns:
        The result of the expression as a string
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

def get_current_time(input: str) -> str:
    """
    Returns the current date and time in the format YYYY-MM-DD HH:MM:SS.
    
    This tool is useful for when the user asks for the current time or date.
    It provides the precise current date and time when called.
    
    Args:
        input: A string input parameter (required by Tool interface)
    
    Returns:
        The current date and time formatted as YYYY-MM-DD HH:MM:SS
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def reverse_string(input: str) -> str:
    """
    Reverses a string by returning it in reverse order.
    
    This function takes a string and returns it backwards using Python's
    slice notation [::-1], which is a concise and efficient way to reverse
    strings in Python.
    
    Args:
        input: A string to be reversed
    
    Returns:
        The input string reversed
    """
    return input[::-1]

def get_weather(date: str) -> str:
    """
    Returns the weather information for a given date.
    
    This function takes a date in YYYY-MM-DD format and returns weather
    information. If the date matches today's date, it returns sunny weather.
    For all other dates, it returns rainy weather.
    
    Args:
        date: A date string in format "YYYY-MM-DD"
    
    Returns:
        Weather information as a string (e.g., "Sunny, 72°F" or "Rainy, 55°F")
    
    Raises:
        ValueError: If the date string is not in the correct format
    """
    try:
        # Validate the date format
        from datetime import datetime as dt_class
        dt_class.strptime(date, "%Y-%m-%d")
        
        # Get today's date
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Compare input date with today's date
        if date == today:
            return "Sunny, 72°F"
        else:
            return "Rainy, 55°F"
    except ValueError as e:
        return f"Error: Invalid date format. Please use YYYY-MM-DD format. Details: {str(e)}"
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"

def main():
    """Main function to start the application."""
    print("🤖 Python LangChain Agent Starting...")
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Check if GITHUB_TOKEN exists
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("\n❌ Error: GITHUB_TOKEN not found in environment variables")
        print("\n📋 To fix this:")
        print("   1. Create a .env file in the project root directory")
        print("   2. Add your GitHub token: GITHUB_TOKEN=your_token_here")
        print("   3. Get a token from: https://github.com/settings/personal-access-tokens/new")
        print("   4. Make sure .env is in your .gitignore (don't commit it!)")
        return
    
    print("✅ GitHub token loaded successfully!\n")
    
    # Initialize the ChatOpenAI model
    llm = ChatOpenAI(
        model="openai/gpt-4o",
        temperature=0,
        base_url="https://models.github.ai/inference",
        api_key=github_token
    )
    
    # Create tools list with Calculator, Time, and String Reversal tools
    tools = [
        Tool(
            name="Calculator",
            func=calculator,
            description="Useful for performing mathematical calculations and evaluating mathematical expressions. "
                       "Use this tool when you need to compute arithmetic operations such as addition, subtraction, "
                       "multiplication, division, and more complex mathematical expressions. "
                       "Input should be a valid mathematical expression as a string (e.g., '25 * 4 + 10')."
        ),
        Tool(
            name="get_current_time",
            func=get_current_time,
            description="Returns the current date and time. Use this tool when the user asks what time it is, "
                       "what the current date is, or any question about the present moment. "
                       "The input parameter is not used but is required by the tool interface."
        ),
        Tool(
            name="reverse_string",
            func=reverse_string,
            description="Reverses a string. Input should be a single string."
        ),
        Tool(
            name="get_weather",
            func=get_weather,
            description="Returns weather information for a given date. Use this tool when the user asks about weather "
                       "for a specific date. Input should be a date string in YYYY-MM-DD format. "
                       "Returns sunny weather (72°F) for today's date and rainy weather (55°F) for other dates."
        )
    ]
    
    # Bind tools to the LLM for tool calling
    llm_with_tools = llm.bind_tools(tools)
    
    # Create a prompt template for the agent
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional and succinct AI assistant. Provide clear, concise responses without unnecessary elaboration. "
                   "You have access to four tools: Calculator (for math), get_current_time (for date/time), reverse_string (for string operations), and get_weather (for weather information). "
                   "Use the appropriate tool when needed to answer questions accurately. "
                   "Be professional in tone and efficient in your responses."),
        ("human", "{input}")
    ])
    
    # Create the agent chain
    agent_chain = prompt | llm_with_tools
    
    # Create a list of test queries
    test_queries = [
        "What time is it right now?",
        "What is 25 * 4 + 10?",
        "Reverse the string 'Hello World'",
        "What's the weather like today?"
    ]
    
    # Run multiple test queries
    print("Running example queries:\n")
    
    for query in test_queries:
        try:
            print(f"📝 Query: {query}")
            print("─" * 50)
            
            # Initialize messages with system message and user query
            from langchain_core.messages import HumanMessage, ToolMessage, SystemMessage
            messages = [
                SystemMessage(content="You are a professional and succinct AI assistant. Provide clear, concise responses without unnecessary elaboration. "
                                      "You have access to four tools: Calculator (for math), get_current_time (for date/time), reverse_string (for string operations), and get_weather (for weather information). "
                                      "Use the appropriate tool when needed to answer questions accurately. "
                                      "Be professional in tone and efficient in your responses."),
                HumanMessage(content=query)
            ]
            
            # Agent loop - continue until no more tool calls
            while True:
                # Invoke the LLM with tools using the current messages
                response = llm_with_tools.invoke(messages)
                
                # Check if the response contains tool calls
                if hasattr(response, 'tool_calls') and response.tool_calls:
                    print(f"Agent is calling tools...")
                    
                    # Add the assistant response to messages
                    messages.append(response)
                    
                    # Process each tool call
                    for tool_call in response.tool_calls:
                        tool_name = tool_call.get("name")
                        tool_input = tool_call.get("args", {})
                        tool_id = tool_call.get("id")
                        
                        print(f"  📌 Tool: {tool_name}")
                        print(f"  📌 Input: {tool_input}")
                        
                        # Execute the tool by getting the first (and usually only) argument
                        # LangChain passes single arguments as __arg1
                        first_arg = tool_input.get("__arg1", "") or tool_input.get("input", "") or tool_input.get("expression", "") or tool_input.get("date", "")
                        
                        if tool_name == "Calculator":
                            result = calculator(first_arg)
                        elif tool_name == "get_current_time":
                            result = get_current_time(first_arg)
                        elif tool_name == "reverse_string":
                            result = reverse_string(first_arg)
                        elif tool_name == "get_weather":
                            result = get_weather(first_arg)
                        else:
                            result = f"Unknown tool: {tool_name}"
                        
                        print(f"  📌 Result: {result}")
                        
                        # Add the tool result to messages
                        messages.append(ToolMessage(content=result, tool_call_id=tool_id))
                else:
                    # No more tool calls, print the final response
                    response_text = response.content if hasattr(response, 'content') else str(response)
                    print(f"✅ Result: {response_text}")
                    break
            
            print("\n")
        except Exception as e:
            print(f"❌ Error: {str(e)}\n")
            import traceback
            traceback.print_exc()
    
    print("🎉 Agent demo complete!")

if __name__ == "__main__":
    main()
