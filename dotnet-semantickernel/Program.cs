namespace SemanticKernelAgent;

using Microsoft.SemanticKernel;
using Microsoft.Extensions.Configuration;

// Main entry point using top-level statements
Console.WriteLine("Semantic Kernel AI Agent");
Console.WriteLine("=======================\n");

// Build configuration
var config = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
    .AddUserSecrets(System.Reflection.Assembly.GetExecutingAssembly())
    .AddEnvironmentVariables()
    .Build();

// Get API key from configuration
var apiKey = config["OpenAI:ApiKey"];
var modelId = config["OpenAI:ModelId"] ?? "gpt-4o-mini";

if (string.IsNullOrEmpty(apiKey))
{
    Console.WriteLine("Error: OpenAI API key is not configured.");
    Console.WriteLine("Please set it using: dotnet user-secrets set OpenAI:ApiKey <your-key>");
    return;
}

// Create and configure the kernel
var builder = Kernel.CreateBuilder();
builder.AddOpenAIChatCompletion(modelId, apiKey);
var kernel = builder.Build();

// Example: Get a simple response
try
{
    Console.WriteLine("Sending prompt to AI agent...\n");
    var result = await kernel.InvokePromptAsync("What is the capital of France?");
    Console.WriteLine($"AI Agent Response: {result}");
}
catch (Exception ex)
{
    Console.WriteLine($"Error: {ex.Message}");
}
