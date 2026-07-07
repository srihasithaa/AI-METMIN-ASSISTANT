# AI Meeting Minutes Assistant

## Overview

An AI-powered assistant that answers questions about meeting minutes using LangChain and Ollama.

## Features

- Load meeting minutes from a text file
- Answer questions based only on the meeting content
- Maintains conversation history
- Uses local Gemma models through Ollama

## Technologies

- Python
- LangChain
- Ollama
- Gemma 4B
- RunnableWithMessageHistory

## Project Structure

AI-MEETING-MINUTES-ASSISTANT/
│
├── app.py
├── prompts.py
├── loaders.py
├── chains.py
├── memory.py
├── documents/
│   └── meeting.txt
├── requirements.txt
└── README.md

## How to Run

1. Clone repository
2. Install requirements
3. Install Ollama
4. Pull Gemma model
5. Run app.py
