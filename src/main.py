#!/usr/bin/env python3
"""
Main entry point for the LangGraph Local Workflow.
This demonstrates how to use the workflow system.
"""

from .workflow.tools import Tools
from .workflow.agents import Agents
from .workflow.nodes import State, Workflow
from .workflow.graph import graph

def main():
    """
    Main function to demonstrate the workflow.
    """
    print("LangGraph Local Workflow")
    print("=" * 40)
    
    # Initialize the state
    initial_state = State(
        dolar="",
        notices="",
        yahoo_finance="",
        combined_output=""
    )
    
    print("Available tools:")
    tools = Tools()
    print(f"- {tools.previous_dollar.name}: {tools.previous_dollar.description}")
    print(f"- {tools.yahoo_finance.name}: {tools.yahoo_finance.description}")
    print(f"- {tools.dollar.name}: {tools.dollar.description}")
    
    print("\nWorkflow graph is ready!")
    print("To use the workflow with Ollama running:")
    print("1. Make sure Ollama is installed and running")
    print("2. Ensure the model 'qwen2.5:0.5b' is available")
    print("3. Run: result = graph.invoke(initial_state)")
    
    # Uncomment the following lines when Ollama is available:
    # try:
    #     result = graph.invoke(initial_state)
    #     print("Workflow result:", result)
    # except Exception as e:
    #     print(f"Error running workflow (likely Ollama not available): {e}")

if __name__ == "__main__":
    main()
