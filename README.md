# 📚 Local Document Q&A System with Haystack & Ollama

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg)](https://jupyter.org/)
[![Haystack](https://img.shields.io/badge/haystack-ai-green.svg)](https://haystack.deepset.ai/)
[![Ollama](https://img.shields.io/badge/ollama-local--ai-purple.svg)](https://ollama.ai/)

A simple, powerful system that reads your documents and answers questions about them using **100% local** AI models. No cloud APIs, no data sharing, complete privacy!

## 🌟 Features

- **Document Processing**: Supports PDF, Word documents (.docx), and text files
- **Local AI Integration**: Uses Ollama models (gemma3:1b, llama3.2, etc.) for generating answers
- **No Complex Dependencies**: Uses BM25 keyword search (no embeddings required)
- **Smart Text Processing**: Automatically cleans and chunks documents for better retrieval
- **User-Friendly Interface**: Simple functions for adding documents and asking questions

## 🛠️ Prerequisites

### Required Software
- **Python 3.8+**
- **Ollama** installed and running locally
  - Download from: https://ollama.ai/
  - Install a model like: `ollama pull gemma3:1b`

### Python Packages
The notebook will automatically install these packages:
- `haystack-ai` - Main RAG framework
- `ollama-haystack` - Ollama integration
- `PyPDF2` - PDF file processing
- `python-docx` - Word document processing

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/document-qa-system.git
cd document-qa-system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install and Setup Ollama
1. Download and install Ollama from: https://ollama.ai/
2. Pull a model (recommended):
   ```bash
   ollama pull gemma2:2b
   # or for faster processing on lower-end hardware:
   ollama pull phi3:mini
   ```
3. Start Ollama (it usually starts automatically)

### 4. Run the Notebook
```bash
jupyter notebook Clean-Haystack-RAG.ipynb
```

### 5. Try It Out
Run all cells in order, then use the simple interface:
```python
# Add your documents
add_document_to_system("sample_documents/sample_document.txt")

# Ask questions
ask_about_documents("What are the key features of this system?")
```

### 4. Ask Questions
```python
# Ask questions about your documents
ask_about_documents("What is the main topic of these documents?")
ask_about_documents("Can you summarize the key findings?")
ask_about_documents("What methodology was used?")
```

## 📖 How It Works

### Document Processing Pipeline
1. **File Reading**: Extracts text from PDF, DOCX, or TXT files
2. **Text Cleaning**: Removes formatting artifacts and normalizes text
3. **Document Chunking**: Breaks large documents into smaller, searchable pieces
4. **Storage**: Stores chunks in an in-memory document store

### Question Answering Pipeline
1. **Search**: Uses BM25 algorithm to find relevant document chunks
2. **Context Building**: Assembles relevant chunks into context
3. **Answer Generation**: Uses your local Ollama model to generate answers
4. **Response**: Returns human-readable answers based on your documents

## 🎯 Key Functions

### Main Interface Functions
- `add_document_to_system(file_path)` - Add a document to your knowledge base
- `ask_about_documents(question)` - Ask questions about your documents
- `check_knowledge_base()` - See what documents are loaded

### Direct System Access
- `qa_system.add_document_file(path)` - Add documents directly
- `qa_system.answer_question(question)` - Get answers directly
- `qa_system.show_knowledge_base_info()` - Get system statistics

## 📁 Project Structure

```
document-qa-system/
├── Clean-Haystack-RAG.ipynb      # 🎯 Main notebook - start here!
├── README.md                     # 📖 This documentation
├── requirements.txt              # 📦 Python dependencies
├── .gitignore                   # 🚫 Files to ignore in git
├── sample_documents/            # 📄 Sample files for testing
│   └── sample_document.txt      # Example document
└── your_documents/              # 📂 Put your files here (gitignored)
```

## 🔧 System Architecture

### Core Components
- **DocumentQASystem**: Main class that orchestrates everything
- **InMemoryDocumentStore**: Stores document chunks
- **InMemoryBM25Retriever**: Finds relevant documents using keyword search
- **OllamaGenerator**: Generates answers using your local AI model
- **Pipeline**: Orchestrates the document processing and question answering

### Text Processing
- **Cleaning**: Removes PDF artifacts and normalizes whitespace
- **Chunking**: Splits documents into 500-word overlapping pieces
- **Metadata**: Tracks source files and chunk information

## ⚡ Performance Tips

### For Better Results
1. **Use descriptive questions** - Be specific about what you want to know
2. **Add multiple related documents** - More context = better answers
3. **Use appropriate AI models** - Larger models give better answers but are slower

### Troubleshooting
- **Ollama not responding**: Ensure Ollama is running (`ollama serve`)
- **Poor answers**: Try adding more relevant documents
- **Memory issues**: Restart the notebook kernel if processing many large files

## 🎨 Customization

### Change AI Model
```python
qa_system = DocumentQASystem(ai_model_name="llama3.2")  # or any Ollama model
```

### Adjust Chunk Size
Modify the `piece_size` parameter in `_break_into_smaller_pieces()` method

### Custom File Types
Extend the `add_document_file()` method to support additional file formats

## 📊 Example Usage

```python
# 1. Add your research papers or documents
add_document_to_system("sample_documents/sample_document.txt")
add_document_to_system("your_documents/research_paper.pdf")
add_document_to_system("your_documents/meeting_notes.docx")

# 2. Check what's loaded
check_knowledge_base()  # Shows: "Knowledge base contains X document pieces"

# 3. Ask questions about your documents
ask_about_documents("What are the main topics covered?")
ask_about_documents("What are the key findings?")
ask_about_documents("Can you summarize the methodology?")
ask_about_documents("Are there any important conclusions?")
```

## 🎥 Demo

![Demo GIF](https://via.placeholder.com/600x300.png?text=Demo+GIF+Coming+Soon)

*Add a GIF or screenshot of your system in action*

## 🐛 Common Issues

### Import Errors
- Ensure all packages are installed: run cells 1-2 first
- Restart kernel if you encounter module conflicts

### Document Processing Issues
- **PDFs**: Some PDFs may have poor text extraction - try converting to text first
- **Large files**: Very large documents may take time to process
- **Encoding**: Non-English documents may need encoding adjustments

### AI Model Issues
- **Model not found**: Install the model first: `ollama pull gemma3:1b`
- **Slow responses**: Larger models take more time, consider using smaller models for testing

## 🔄 Updates and Maintenance

### Clearing the Knowledge Base
Restart the notebook kernel to start fresh with new documents.

### Adding New Features
The modular design makes it easy to extend:
- Add new file format support in `_extract_text_from_*` methods
- Customize the answer template in `_setup_workflows()`
- Add preprocessing steps in `_clean_messy_text()`

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add some amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contributions
- Support for more file formats (Excel, PowerPoint, etc.)
- Better text preprocessing for specific document types
- Integration with more local AI models
- Performance optimizations
- UI improvements
- Better error handling

## ⭐ Show Your Support

If you find this project useful, please consider:
- Giving it a ⭐ on GitHub
- Sharing it with others who might benefit
- Contributing improvements or bug fixes
- Reporting issues or suggesting features

## 📧 Contact

- GitHub: [@yourusername](https://github.com/yourusername)
- Issues: [Project Issues](https://github.com/yourusername/document-qa-system/issues)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Haystack](https://haystack.deepset.ai/) - The amazing RAG framework
- [Ollama](https://ollama.ai/) - Local AI model runtime
- The open-source community for inspiration and tools

---

**Happy Document Q&A! 🎉**

For questions or issues, check the troubleshooting section above or review the code comments in the notebook.
