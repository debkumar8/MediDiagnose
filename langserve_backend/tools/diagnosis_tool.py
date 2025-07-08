from langchain.tools import tool
from utils.euri_client import euri_chat_completion

@tool
def ai_diagnos(symptom_description: str) -> str:
    """Use EURI AI model to diagnose based on symptoms."""
    messages = [
        {"role": "user", "content": f"A patient reports: {symptom_description}. What are the possible diagnoses and steps to take?"}
    ]
    return euri_chat_completion(messages) 

# It is returning "euri_chat_completion" , what is the input "euri_chat_completion" takes ?
# It is taking a message, whatever message i am going to pass , if i said i am not felling well, i have sever back pain
# So, it is taking message
# Then i am going to create message in LLM way
# content wise formated string

# Finally we convert the function as tool by using @tool, so my agent will able to discover
