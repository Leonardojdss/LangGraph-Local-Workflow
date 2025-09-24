from langgraph.graph import StateGraph, START, END
from ..workflow.nodes import State, Workflow
import os

builder = StateGraph(State)
# Add nodes to the graph
builder.add_node("dolar", Workflow.dolar)

# Add edges
builder.add_edge(START, "dolar")
builder.add_edge("dolar", END)







graph = builder.compile()



