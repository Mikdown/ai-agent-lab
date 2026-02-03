In app.py, add code to:

Import and load environment variables using dotenv
Check if GITHUB_TOKEN exists in environment variables
Display an error message with helpful instructions if the token is not found
Return early if no token is found
Include helpful user feedback with emoji

Updated app.py with:

Environment variable loading inside main()
GITHUB_TOKEN validation with early return if missing
Helpful error message with emoji (❌, 📋, ✅) and instructions for setting up the token
Success message when token is found