from src.workflow.graph import Graph

graph = Graph()

state = graph.builder_workflow().invoke({})
print(state["combined_output"])