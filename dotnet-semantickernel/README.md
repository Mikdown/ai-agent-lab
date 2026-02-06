# Semantic Kernel AI Agent (.NET)

A .NET 8.0+ console application using Microsoft.SemanticKernel for AI-powered tasks.

## Prerequisites

- .NET 8.0 or higher
- OpenAI API key (for ChatGPT models)

## Setup

### 1. Configure API Key

Store your OpenAI API key using User Secrets:

```bash
dotnet user-secrets init
dotnet user-secrets set OpenAI:ApiKey <your-api-key>
```

### 2. Build and Run

```bash
dotnet restore
dotnet build
dotnet run
```

## Project Structure

- **Program.cs** - Main entry point with Semantic Kernel initialization
- **dotnet-semantickernel.csproj** - Project configuration and NuGet dependencies
- **appsettings.json** - Configuration settings (API model info)

## Dependencies

- **Microsoft.SemanticKernel** - AI agent and plugin framework
- **Microsoft.Extensions.Configuration** - Configuration management
- **Microsoft.Extensions.Configuration.UserSecrets** - Secure credential storage
- **Microsoft.Extensions.Configuration.Json** - JSON configuration support
