import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

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
    
    # Test basic query without tools
    test_query = "What is 25 * 4 + 10?"
    print(f"📝 Query: {test_query}")
    
    response = llm.invoke([HumanMessage(content=test_query)])
    print(f"✅ Response: {response.content}\n")

if __name__ == "__main__":
    main()
