import os
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_core.tools import Tool

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
    
    # Create tools list with Calculator tool
    tools = [
        Tool(
            name="Calculator",
            func=calculator,
            description="Useful for performing mathematical calculations and evaluating mathematical expressions. "
                       "Use this tool when you need to compute arithmetic operations such as addition, subtraction, "
                       "multiplication, division, and more complex mathematical expressions. "
                       "Input should be a valid mathematical expression as a string (e.g., '25 * 4 + 10')."
        )
    ]
    
    # Create an agent with the tools
    agent_executor = create_agent(llm, tools, debug=True)
    
    # Test the agent with a query
    test_query = "What is 25 * 4 + 10?"
    
    try:
        print(f"📝 Query: {test_query}\n")
        result = agent_executor.invoke({"input": test_query})
        print(f"\n✅ Result: {result['output']}\n")
    except Exception as e:
        print(f"❌ Error: {str(e)}\n")

if __name__ == "__main__":
    main()
