from IPython.display import Image, display
import os
from ..workflow.graph import graph

graph_image = graph.get_graph().draw_mermaid_png()
image_path = os.path.join("workflow_graph.png")
with open(image_path, "wb") as f:
    f.write(graph_image)