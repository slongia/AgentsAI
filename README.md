---
title: AgentsAI
emoji: 🐠
colorFrom: blue
colorTo: yellow
sdk: docker
pinned: false
short_description: Introduction to AI agents with LangChain and FAISS
---

# 🤖 AgentsAI

An AI agents quickstart demo showcasing text extraction, summarization, and vector search capabilities using modern AI/ML frameworks.

## 🌟 Features

- **Text Extraction**: Parse HTML or plain text input using BeautifulSoup
- **Summarization**: Placeholder for LLM-based text summarization (ready for integration)
- **Vector Search**: FAISS-based vector indexing for semantic search
- **LangChain Integration**: Built with LangChain framework for agent orchestration
- **Web Interface**: Interactive Gradio UI for easy testing and demonstration
- **FastAPI Backend**: RESTful API support via FastAPI/Uvicorn

## 🚀 Tech Stack

- **Python 3.11**
- **Gradio 3.44** - Interactive web interface
- **LangChain 0.2.15** - Agent framework
- **FAISS** - Vector similarity search
- **FastAPI** - Web framework
- **BeautifulSoup4** - HTML parsing
- **Transformers** - HuggingFace models support
- **OpenAI API** - Ready for LLM integration

## 📦 Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/slongia/AgentsAI.git
cd AgentsAI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
# Using Uvicorn
uvicorn src.app:app --host 0.0.0.0 --port 7860

# Or run directly
python src/app.py
```

### Docker Deployment

```bash
docker build -t agentsai .
docker run -p 7860:7860 agentsai
```

### Dev Container

This project includes a VS Code dev container configuration for consistent development environments:

```bash
# Open in VS Code and use "Reopen in Container"
```

## 🎯 Usage

1. Open your browser to `http://localhost:7860`
2. Paste HTML or plain text into the input box
3. View the extracted text, summary, and FAISS indexing status
4. Check the LangChain version information

## 📁 Project Structure

```
AgentsAI/
├── .devcontainer/
│   └── devcontainer.json    # VS Code dev container config
├── src/
│   └── app.py               # Main application
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🛠️ Development

### Prerequisites

- Python 3.11+
- Git
- Docker (optional)

### Environment Setup

The project uses environment variables for configuration. You can set:

- `GRADIO_SERVER_PORT`: Custom port (default: 7860)
- Additional API keys for OpenAI, etc.

## 🔗 Links

- **Hugging Face Space**: [slongia/AgentsAI](https://huggingface.co/spaces/slongia/AgentsAI)
- **GitHub Repository**: [slongia/AgentsAI](https://github.com/slongia/AgentsAI)
- **Hugging Face Spaces Config**: [Documentation](https://huggingface.co/docs/hub/spaces-config-reference)

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

## 🎓 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [FAISS Documentation](https://faiss.ai/)
- [Gradio Documentation](https://gradio.app/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## ⚠️ Note

This is a demonstration project. The summarization feature currently uses a placeholder implementation and should be replaced with a proper LLM (e.g., OpenAI GPT, Anthropic Claude, or open-source models) for production use.

---

Built by [Surinder Longia](https://github.com/slongia)
