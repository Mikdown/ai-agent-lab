import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_core.tools import Tool
from datetime import datetime

def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression from a string input.
    Uses Python's eval() for demonstration purposes. Not safe for untrusted input in production.
    Returns the result as a string, or an error message if evaluation fails.
    """
    try:
        # Only allow basic math for demo; do NOT use eval on untrusted input in production!
        result = eval(expression, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error: {e}"
    
def get_current_time(_: str) -> str:
    """
    Returns the current date and time as a formatted string (YYYY-MM-DD HH:MM:SS).
    The input parameter is required by the Tool interface but is not used.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def reverse_string(s: str) -> str:
    """
    Reverses the input string and returns the result.
    """
    return s[::-1]
    
def main():
    load_dotenv()
    print("🚀 Starting LangChain AI Agent Application!")
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("❌ ERROR: GITHUB_TOKEN not found in environment variables.")
        print("\n🔑 Please create a GitHub personal access token and add it to your environment.")
        print("   1. Create a token at: https://github.com/settings/tokens\n   2. Add it to a .env file as: OPENAI_API_KEY=your_token_here\n   3. Restart the application.\n")
        return
    print("✅ GITHUB_TOKEN found! Continuing... 🟢")

    # Create ChatOpenAI instance for GitHub's openai/gpt-4o endpoint
    chat = ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        base_url="https://models.inference.ai.azure.com",
        api_key=os.getenv("GITHUB_TOKEN")
    )

    print("🤖 ChatOpenAI instance created!")

    # Define tools list with calculator tool
    tools = [
        Tool(
            name="Calculator",
            func=calculator,
            description=(
                "Use this tool to accurately solve mathematical expressions, including arithmetic, multiplication, division, addition, subtraction, and parentheses. "
                "Use it whenever you need to compute, evaluate, or check the result of a math problem, especially if the calculation is non-trivial or involves multiple steps. "
                "Do not use for non-mathematical queries."
            )
        ),
        Tool(
            name="get_current_time",
            func=get_current_time,
            description=(
                "Use this tool to get the current date and time. "
                "Call it whenever you need to know the present time or date, or answer questions about the current timestamp."
            )
        ),
        Tool(
            name="reverse_string",
            func=reverse_string,
            description=(
                "Use this tool to reverse a string. "
                "Call it whenever you need to reverse a string."
            )
        )
    ]

    # Create agent with LLM and tools
    try:
        agent_executor = create_agent(
            chat,
            tools,
            debug=True
        )
        query = "Reverse the string 'Hello World!'"
        print(f"🤖 Agent running query: {query}")
        result = agent_executor.invoke({"messages": [{"role": "user", "content": query}]})
        print("🟢 Agent Output:")
        # Try to print the final answer from the agent result
        if isinstance(result, dict):
            # LangChain agent usually returns a 'messages' list
            messages = result.get('messages')
            if messages and isinstance(messages, list):
                # Find the last message with 'content'
                for msg in reversed(messages):
                    if isinstance(msg, dict) and 'content' in msg:
                        print(msg['content'])
                        break
                    elif hasattr(msg, 'content'):
                        print(msg.content)
                        break
                else:
                    print(result)
            else:
                print(result)
        else:
            print(result)
    except Exception as e:
        print(f"❌ Agent error: {e}")

if __name__ == "__main__":
    main()
