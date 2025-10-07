from src.workflow.graph import Graph
from langfuse.langchain import CallbackHandler
 
langfuse_handler = CallbackHandler()
graph = Graph()

initial_state = {}

state = graph.builder_workflow().invoke(initial_state, config={"callbacks": [langfuse_handler]})
print(state["combined_output"])