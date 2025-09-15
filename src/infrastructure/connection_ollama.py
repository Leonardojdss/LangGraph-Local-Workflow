from langchain_ollama import ChatOllama

class OllamaConnection:
    """
    Class to connect to Ollama LLM model.
    model default is "gemma3:1b"
    temperature default is 0
    """
    def __init__(self, model: str = "gemma3:1b", temperature: int = 0):
        self.model = model
        self.temperature = temperature

    def connect(self):
        llm = ChatOllama(model=self.model, temperature=self.temperature)
        return llm
    
# if __name__ == "__main__":
#     llm = OllamaConnection().connect()
#     messages = [
#     (
#         "system",
#         "voce é um assistente útil que ajuda os usuários a aprender programação.",
#     ),
#     ("human", "Eu amo programação."),
# ]
#     ai_msg = llm.invoke(messages)
#     print(ai_msg)