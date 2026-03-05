import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

def main():
    load_dotenv()
    print("🚀 Starting LangChain AI Agent Application!")
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("❌ ERROR: GITHUB_TOKEN not found in environment variables.")
        print("\n🔑 Please create a GitHub personal access token and add it to your environment.")
        print("   1. Create a token at: https://github.com/settings/tokens\n   2. Add it to a .env file as: GITHUB_TOKEN=your_token_here\n   3. Restart the application.\n")
        return
    print("✅ GITHUB_TOKEN found! Continuing... 🟢")

    # Create ChatOpenAI instance
    chat = ChatOpenAI(
        model="openai/gpt-4o",
        temperature=0,
        base_url="https://models.github.ai/inference",
        api_key=github_token
    )
    print("🤖 ChatOpenAI instance created!")

    # Test query
    query = "What is 25 * 4 + 10?"
    print(f"📝 Sending test query: {query}")
    response = chat.invoke([HumanMessage(content=query)])
    print("💬 AI Response:")
    print(response.content)

if __name__ == "__main__":
    main()
