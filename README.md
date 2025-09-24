# LangGraph-Local-Workflow

Um workflow local baseado em LangGraph que utiliza modelos LLM locais (Ollama) para consultas de dados financeiros em tempo real.

![Workflow Diagram](image.png)

## 📋 Visão Geral

Este projeto implementa um sistema de agentes inteligentes usando LangGraph para consultar dados financeiros, incluindo:

- **Cotação do Dólar**: Consulta da taxa de câmbio USD/BRL através da API do Banco Central do Brasil
- **Preços de Ações**: Consulta de preços de ações americanas através do Yahoo Finance
- **Processamento Local**: Utiliza modelos Ollama para processamento de linguagem natural local

## 🏗️ Arquitetura

O projeto está estruturado em camadas:

```
src/
├── infrastructure/          # Conexões e configurações
│   └── connection_ollama.py # Conexão com modelo Ollama
├── workflow/               # Lógica do workflow
│   ├── agents.py          # Definição dos agentes
│   ├── tools.py           # Ferramentas de consulta de dados
│   ├── nodes.py           # Nós do workflow
│   └── graph.py           # Configuração do grafo
└── utils/                 # Utilitários
    └── image_graph.py     # Geração de diagramas
```

### Componentes Principais

#### 1. **Infrastructure Layer**
- `OllamaConnection`: Gerencia conexão com modelos Ollama locais
- Modelo padrão: `qwen2.5:0.5b`
- Temperatura configurável (padrão: 0)

#### 2. **Tools Layer**
- `dollar()`: Consulta cotação do dólar em data específica
- `previous_dollar()`: Consulta cotação do dia útil anterior
- `yahoo_finance()`: Consulta preços de ações americanas

#### 3. **Agents Layer**
- `agent_dollar()`: Agente especializado em cotações de dólar
- `agent_yahoo_finance()`: Agente para consultas de ações

#### 4. **Workflow Layer**
- `State`: Definição do estado do workflow
- `Workflow`: Nós de processamento
- `StateGraph`: Configuração do fluxo de execução

## 🚀 Instalação

### Pré-requisitos

1. **Python 3.8+**
2. **Ollama instalado localmente**
   ```bash
   # Instalar Ollama
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Baixar modelo recomendado
   ollama pull qwen2.5:0.5b
   ```

### Dependências

```bash
# Clone o repositório
git clone https://github.com/Leonardojdss/LangGraph-Local-Workflow.git
cd LangGraph-Local-Workflow

# Instalar dependências Python
pip install -r requirements.txt

# Ou instalar manualmente
pip install langgraph langchain-ollama langchain-core yfinance requests typing-extensions
```

## 💻 Uso

### Exemplo Básico - Cotação do Dólar

```python
from src.workflow.nodes import Workflow

# Consultar cotação atual do dólar
state = {"dolar": "", "notices": "", "yahoo_finance": "", "combined_output": ""}
result = Workflow.dolar(state)
print(result["dolar"])
```

### Exemplo - Consulta de Ações

```python
from src.workflow.tools import Tools

# Consultar preços de ações
companies = ["AAPL", "MSFT", "GOOGL"]
prices = Tools.yahoo_finance(companies)
print(prices)
```

### Exemplo - Conexão Ollama Personalizada

```python
from src.infrastructure.connection_ollama import OllamaConnection

# Usar modelo diferente
llm = OllamaConnection(model="llama2:7b", temperature=0.1).connect()

# Fazer consulta
messages = [
    ("system", "Você é um assistente financeiro especializado."),
    ("human", "Qual a cotação atual do dólar?")
]
response = llm.invoke(messages)
print(response)
```

## 🔧 Configuração

### Modelos Ollama Suportados

O projeto é compatível com qualquer modelo Ollama. Modelos recomendados:

- `qwen2.5:0.5b` (padrão - rápido e eficiente)
- `llama2:7b` (mais capaz, mais lento)
- `mistral:7b` (boa performance geral)

### Configuração da Conexão

```python
# Configuração personalizada
ollama_config = {
    "model": "qwen2.5:0.5b",
    "temperature": 0,
    "base_url": "http://localhost:11434"  # URL padrão do Ollama
}
```

## 📊 APIs Utilizadas

### 1. Banco Central do Brasil - PTAX
- **Endpoint**: `https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/`
- **Função**: Cotações oficiais USD/BRL
- **Atualização**: Dias úteis
- **Formato**: JSON

### 2. Yahoo Finance
- **Biblioteca**: `yfinance`
- **Função**: Preços de ações em tempo real
- **Mercados**: Principalmente ações americanas (NYSE, NASDAQ)
- **Dados**: Preço atual, histórico, informações da empresa

## 🔄 Workflow States

O sistema utiliza o seguinte estado:

```python
class State(TypedDict):
    dolar: str           # Resultado da consulta de dólar
    notices: str         # Notícias ou avisos
    yahoo_finance: str   # Resultados do Yahoo Finance
    combined_output: str # Saída combinada
```

## 🧪 Testando o Sistema

### Teste da Conexão Ollama

```python
python -c "
from src.infrastructure.connection_ollama import OllamaConnection
llm = OllamaConnection().connect()
print('✅ Ollama conectado com sucesso')
"
```

### Teste das APIs Financeiras

```python
python -c "
from src.workflow.tools import Tools
from datetime import datetime

# Teste API Banco Central
date = datetime.now().strftime('%m-%d-%Y')
result = Tools.dollar(date)
print('💰 Dólar:', result)

# Teste Yahoo Finance
stocks = Tools.yahoo_finance(['AAPL'])
print('📈 Ações:', stocks)
"
```

## 🚨 Solução de Problemas

### Erro de Conexão Ollama
```bash
# Verificar se Ollama está rodando
ollama list

# Iniciar serviço se necessário
ollama serve
```

### Erro de Modelo Não Encontrado
```bash
# Baixar modelo padrão
ollama pull qwen2.5:0.5b
```

### Erro de Dependências
```bash
# Reinstalar dependências
pip install --upgrade langgraph langchain-ollama yfinance requests
```

## 📈 Roadmap

- [ ] Implementação completa do StateGraph
- [ ] Interface web para interação
- [ ] Suporte a mais mercados financeiros
- [ ] Análise técnica de ações
- [ ] Notificações automáticas
- [ ] Cache de consultas
- [ ] API REST

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/Leonardojdss/LangGraph-Local-Workflow/issues)
- **Documentação**: Este README
- **Ollama**: [Documentação Oficial](https://ollama.ai/docs)

---

**Desenvolvido com ❤️ usando LangGraph e Ollama**