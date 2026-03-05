import os
from dotenv import load_dotenv

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

if __name__ == "__main__":
    main()
