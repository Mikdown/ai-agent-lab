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
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_core.tools import Tool
from datetime import datetime

def main():
    load_dotenv()
    print("🚀 Starting LangChain AI Agent Application!")
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("❌ ERROR: OPENAI_API_KEY not found in environment variables.")
        print("\n🔑 Please create a GitHub personal access token and add it to your environment.")
        print("   1. Create a token at: https://github.com/settings/tokens\n   2. Add it to a .env file as: OPENAI_API_KEY=your_token_here\n   3. Restart the application.\n")
        return
    print("✅ OPENAI_API_KEY found! Continuing... 🟢")

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
        )
    ]

    # Create agent with LLM and tools
    try:
        agent_executor = create_agent(
            chat,
            tools,
            debug=True
        )
        query = "What is 25 * 4 + 10?"
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
