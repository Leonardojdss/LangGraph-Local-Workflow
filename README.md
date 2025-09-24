# LangGraph-Local-Workflow

A LangGraph-based workflow system for financial data queries using Ollama LLM with tools for dollar exchange rates and stock prices.

![Workflow Graph](image.png)

## Features

- **Dollar Exchange Rate Tool**: Fetches USD/BRL exchange rates from the Central Bank of Brazil API
- **Yahoo Finance Tool**: Retrieves stock prices for US companies
- **LangGraph Workflow**: Structured workflow using LangGraph with state management
- **Ollama Integration**: Uses local Ollama LLM (qwen2.5:0.5b model)

## Prerequisites

1. **Python 3.8+**
2. **Ollama** installed and running locally
3. **Ollama model**: `qwen2.5:0.5b` (or modify the model in `src/infrastructure/connection_ollama.py`)

### Installing Ollama

Visit [Ollama's website](https://ollama.ai/) and follow the installation instructions for your platform.

After installing Ollama, pull the required model:
```bash
ollama pull qwen2.5:0.5b
```

## Installation

1. **Clone the repository**:
```bash
git clone https://github.com/Leonardojdss/LangGraph-Local-Workflow.git
cd LangGraph-Local-Workflow
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

Run the main demonstration:
```bash
python -m src.main
```

This will show available tools and workflow status.

### Using the Workflow

```python
from src.workflow.graph import graph
from src.workflow.nodes import State

# Initialize state
initial_state = State(
    dolar="",
    notices="", 
    yahoo_finance="",
    combined_output=""
)

# Run the workflow (requires Ollama running)
result = graph.invoke(initial_state)
print(result)
```

### Available Tools

1. **previous_dollar**: Gets the previous business day's USD/BRL exchange rate
2. **dollar**: Gets USD/BRL exchange rate for a specific date (MM-DD-YYYY format)
3. **search_yahoo_finance**: Gets stock prices for US companies

### Example Tool Usage

```python
from src.workflow.tools import Tools

tools = Tools()

# Get previous day's dollar rate (requires external API access)
# result = tools.previous_dollar.invoke({})

# Get stock prices (requires external API access)  
# result = tools.yahoo_finance.invoke({"companies": ["MSFT", "AAPL", "GOOG"]})
```

## Project Structure

```
src/
├── infrastructure/
│   └── connection_ollama.py    # Ollama LLM connection
├── workflow/
│   ├── agents.py              # LangGraph agents
│   ├── graph.py               # Workflow graph definition
│   ├── nodes.py               # Workflow nodes and state
│   └── tools.py               # LangChain tools for external APIs
├── utils/
│   └── image_graph.py         # Graph visualization utility
└── main.py                    # Main entry point
```

## Architecture

The workflow uses:

- **LangGraph**: For workflow orchestration and state management
- **LangChain Tools**: For external API integrations (BCB API, Yahoo Finance)
- **Ollama**: As the local LLM provider
- **Structured State**: TypedDict-based state management

## Configuration

### Changing the LLM Model

Edit `src/infrastructure/connection_ollama.py`:

```python
def __init__(self, model: str = "your-model-name", temperature: int = 0):
```

### Adding New Tools

1. Add tool methods to `src/workflow/tools.py` with `@tool` decorator
2. Update agents in `src/workflow/agents.py` to include new tools
3. Modify workflow nodes in `src/workflow/nodes.py` as needed

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Make sure you're running commands from the project root
2. **Ollama Connection Error**: Ensure Ollama is running and the model is available
3. **API Connection Issues**: External APIs (BCB, Yahoo Finance) require internet access

### Testing

Run the structure test to verify everything is set up correctly:
```bash
python /tmp/test_workflow.py  # (if test file is available)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source. Please check the license file for details.