import os
from src.workflow.graph import Graph

graph = Graph()

class ImageGraph:
    
    @staticmethod
    def generate_workflow_image():
        graph_image = graph.builder_workflow().get_graph().draw_mermaid_png()
        image_path = os.path.join("workflow_graph.png")
        with open(image_path, "wb") as f:
            f.write(graph_image)
            
if __name__ == "__main__":
    ImageGraph.generate_workflow_image()