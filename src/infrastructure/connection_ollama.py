from langchain_ollama import ChatOllama

class OllamaConnection:
    """
    Class to connect to Ollama LLM model.
    model default is "qwen2.5:0.5b"
    temperature default is 0
    """
    def __init__(self, model: str = "qwen2.5:0.5b", temperature: int = 0):
        self.model = model
        self.temperature = temperature

    def connect(self):
        llm = ChatOllama(model=self.model, temperature=self.temperature)
        return llm