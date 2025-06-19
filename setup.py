#!/usr/bin/env python3
"""
Setup script for the Document Q&A System
This script helps you get everything set up quickly
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and show the user what's happening"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        return False

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing Python dependencies...")
    return run_command(f"{sys.executable} -m pip install -r requirements.txt", "Installing dependencies")

def check_ollama():
    """Check if Ollama is installed and suggest models"""
    print("🤖 Checking Ollama installation...")
    if run_command("ollama --version", "Checking Ollama version"):
        print("✅ Ollama is installed!")
        print("\n💡 Recommended: Install a model for better performance:")
        print("   ollama pull gemma2:2b    # Good balance of speed and quality")
        print("   ollama pull phi3:mini    # Faster, smaller model")
        print("   ollama pull llama3.2:1b  # Very fast, compact model")
        return True
    else:
        print("❌ Ollama not found. Please install it from: https://ollama.ai/")
        return False

def create_directories():
    """Create necessary directories"""
    dirs = ["your_documents", "outputs"]
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
        print(f"✅ Created directory: {dir_name}")

def main():
    """Main setup function"""
    print("🚀 Setting up Document Q&A System...\n")
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies. Please check your internet connection and try again.")
        return False
    
    # Check Ollama
    ollama_ok = check_ollama()
    
    # Create directories
    create_directories()
    
    print("\n🎉 Setup complete!")
    print("\n📝 Next steps:")
    print("1. Start Jupyter: jupyter notebook Clean-Haystack-RAG.ipynb")
    if not ollama_ok:
        print("2. Install Ollama from: https://ollama.ai/")
        print("3. Pull a model: ollama pull gemma2:2b")
    print("4. Add your documents to the 'your_documents' folder")
    print("5. Run the notebook and start asking questions!")
    
    return True

if __name__ == "__main__":
    main()
