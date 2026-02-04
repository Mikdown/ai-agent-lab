After initializing the LLM in main(), create a tools list with:

A Tool object for the calculator
Use name="Calculator"
Use the calculator function as func
Include a detailed description explaining when to use it
INSTRUCTIONS.md
:166-170
Read lines 30 to 65 of file
Now I'll add the tools list after the LLM initialization:

Edited
app.py+12-0
Done! I've added a tools list after the LLM initialization in app.py with:

A Tool object named "Calculator"
The calculator function as the tool's function

A detailed description explaining when and how to use the tool for mathematical calculations