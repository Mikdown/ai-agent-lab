using OpenAI;
using OpenAI.Chat;
using System.ClientModel;
using Microsoft.Extensions.Configuration;

// Build configuration
var config = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
    .AddEnvironmentVariables()
    .AddUserSecrets(System.Reflection.Assembly.GetExecutingAssembly())
    .Build();

// Main entry point
Console.WriteLine("Semantic Kernel AI Agent");
Console.WriteLine("=======================\n");

// Get GitHub token from configuration
var githubToken = config["GITHUB_TOKEN"];

if (string.IsNullOrEmpty(githubToken))
{
    Console.WriteLine("❌ Error: GITHUB_TOKEN is not configured.");
    Console.WriteLine("\n📝 To set your GitHub token, use User Secrets:");
    Console.WriteLine("   $ dotnet user-secrets init");
    Console.WriteLine("   $ dotnet user-secrets set GITHUB_TOKEN <your-github-token>\n");
    Console.WriteLine("🔗 Get your token at: https://github.com/settings/tokens");
    return;
}

Console.WriteLine("✅ Configuration loaded successfully!");
Console.WriteLine($"🔑 GitHub Token: {'*' * Math.Max(githubToken.Length - 4, 1)}{githubToken.Substring(Math.Max(githubToken.Length - 4, 0))}");
Console.WriteLine("\n🚀 Semantic Kernel AI Agent is ready!\n");

// Configure GitHub Models endpoint
var endpoint = "https://models.github.ai/inference";
var credential = new ApiKeyCredential(githubToken);
var model = "openai/gpt-4o";

var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(endpoint)
};

var client = new ChatClient(model, credential, openAIOptions);

Console.WriteLine($"📦 Model Provider: github");
Console.WriteLine($"🔗 Endpoint: {endpoint}");
Console.WriteLine($"🤖 Model: {model}\n");
Console.WriteLine("✨ Chat client configured and ready!\n");

// Create chat messages
List<ChatMessage> messages = new List<ChatMessage>()
{
    new SystemChatMessage("You are a helpful assistant."),
    new UserChatMessage("What is 25 * 4 + 10?"),
};

Console.WriteLine("👤 User: What is 25 * 4 + 10?");

try
{
    var requestOptions = new ChatCompletionOptions()
    {
        Temperature = 1.0f,
        TopP = 1.0f,
        MaxOutputTokenCount = 1000
    };

    var response = client.CompleteChat(messages, requestOptions);
    
    if (response.Value.Content.Count > 0)
    {
        Console.WriteLine($"🤖 AI: {response.Value.Content[0].Text}\n");
        Console.WriteLine("✅ Agent completed successfully!");
    }
}
catch (Exception ex)
{
    Console.WriteLine($"❌ Error: {ex.Message}");
    Console.WriteLine("\n💡 Troubleshooting Tips:");
    Console.WriteLine("   - Verify your GitHub token has access to GitHub Models");
    Console.WriteLine("   - Check that the endpoint is correct: https://models.github.ai/inference");
    Console.WriteLine("   - Ensure the model ID is available: openai/gpt-4o");
}
