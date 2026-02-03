Updated app.py with:

HumanMessage import from langchain_core.messages
Test query: "What is 25 * 4 + 10?"
llm.invoke() call with the query wrapped in a HumanMessage
Response output printing with emoji formatting
The AI will attempt to answer the math question without access to calculation tools.