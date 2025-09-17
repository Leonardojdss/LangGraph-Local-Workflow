from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display
from ..workflow.nodes import State, Workflow
import os

builder = StateGraph(State)







graph = builder.compile()



graph_image = graph.get_graph().draw_mermaid_png()
image_path = os.path.join("workflow_graph.png")
with open(image_path, "wb") as f:
    f.write(graph_image)