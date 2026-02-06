# Semantic Kernel AI Agent (.NET)

A .NET 10.0+ console application using Microsoft.SemanticKernel for AI-powered tasks with GitHub Models.

## Prerequisites

- .NET 10.0 or higher
- GitHub Personal Access Token (with appropriate permissions for Models API)

## Setup

### 1. Configure GitHub Token

Store your GitHub token using User Secrets:

```bash
dotnet user-secrets init
dotnet user-secrets set GITHUB_TOKEN <your-github-token>
```

### 2. Configure API Endpoint (optional)

By default, the application uses GitHub Models endpoint. You can override via User Secrets:

```bash
dotnet user-secrets set ModelProvider github
dotnet user-secrets set ApiEndpoint https://api.models.github.com
dotnet user-secrets set ModelId gpt-4o
```

Or modify `appsettings.json`:

```json
{
  "ModelProvider": "github",
  "ApiEndpoint": "https://api.models.github.com",
  "ModelId": "gpt-4o"
}
```

### 3. Build and Run

```bash
dotnet restore
dotnet build
dotnet run --framework net10.0
```

## Endpoints Supported

- **GitHub Models**: `https://api.models.github.com` (requires GitHub token)
- **OpenAI**: `https://api.openai.com/v1` (use with OpenAI API key)
- **Azure OpenAI**: Custom Azure endpoint URL

## Project Structure

- **Program.cs** - Main entry point with Semantic Kernel initialization
- **dotnet-semantickernel.csproj** - Project configuration and NuGet dependencies
- **appsettings.json** - Configuration settings (endpoint, model info)

## Dependencies

- **Microsoft.SemanticKernel** - AI agent and plugin framework
- **Microsoft.Extensions.Configuration** - Configuration management
- **Microsoft.Extensions.Configuration.UserSecrets** - Secure credential storage
- **Microsoft.Extensions.Configuration.Json** - JSON configuration support
- **Microsoft.Extensions.Configuration.EnvironmentVariables** - Environment variable support
