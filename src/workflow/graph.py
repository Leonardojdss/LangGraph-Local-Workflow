from langgraph.graph import StateGraph, START, END
from ..workflow.nodes import State, Nodes

class Graph:
    """
    Class to build the workflow graph with LangGraph and LLM Local (Ollama).
    """
    @staticmethod
    def builder_workflow():
        """
        Build the workflow graph with LangGraph.
        """
        agents = Nodes
        graph_parallel_builder = StateGraph(State)

        graph_parallel_builder.add_node("agent_dollar", agents.dolar)
        graph_parallel_builder.add_node("agent_yahoo_finance", agents.yahoo_finance)
        graph_parallel_builder.add_node("agent_trend_topic_previous_day", agents.notices)
        graph_parallel_builder.add_node("aggregator", agents.aggregator)
        graph_parallel_builder.add_edge(START, "agent_dollar")
        graph_parallel_builder.add_edge(START, "agent_yahoo_finance")
        graph_parallel_builder.add_edge(START, "agent_trend_topic_previous_day")
        graph_parallel_builder.add_edge("agent_dollar", "aggregator")
        graph_parallel_builder.add_edge("agent_yahoo_finance", "aggregator")
        graph_parallel_builder.add_edge("agent_trend_topic_previous_day", "aggregator")
        graph_parallel_builder.add_edge("aggregator", END)
        graph_workflow = graph_parallel_builder.compile()
        return graph_workflow

