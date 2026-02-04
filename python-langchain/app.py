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
    
    # Bind tools to the LLM for tool calling
    llm_with_tools = llm.bind_tools(tools)
    
    # Create a prompt template for the agent
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. You have access to a Calculator tool. "
                   "When you need to perform calculations, use the Calculator tool by calling it with the mathematical expression. "
                   "Always use the tool for math questions rather than trying to calculate yourself."),
        ("human", "{input}")
    ])
    
    # Create the agent chain
    agent_chain = prompt | llm_with_tools
    
    # Test the agent with a query
    test_query = "What is 25 * 4 + 10?"
    
    try:
        print(f"📝 Query: {test_query}\n")
        
        # Invoke the agent
        response = agent_chain.invoke({"input": test_query})
        
        # Check if the response contains tool calls
        if hasattr(response, 'tool_calls') and response.tool_calls:
            print(f"Agent is calling tools...")
            for tool_call in response.tool_calls:
                tool_name = tool_call.get("name")
                tool_input = tool_call.get("args", {})
                print(f"  📌 Tool: {tool_name}")
                print(f"  📌 Input: {tool_input}")
                
                # Execute the tool
                if tool_name == "Calculator":
                    result = calculator(tool_input.get("expression", ""))
                    print(f"  📌 Result: {result}")
        else:
            print(f"Response content: {response.content if hasattr(response, 'content') else response}")
        
        print(f"\n✅ Agent completed successfully\n")
    except Exception as e:
        print(f"❌ Error: {str(e)}\n")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
