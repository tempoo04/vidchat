# VidChat

VidChat is a small Streamlit app for asking questions about a YouTube video. It downloads/transcribes the video audio with OpenAI Whisper, stores transcript chunks in a FAISS vector index, and uses Gemini to answer from the retrieved transcript context.

## Features

- Import a YouTube video by URL.
- Transcribe video audio.
- Ask questions about the transcript.
- Show the transcript snippets used as references.

## Tech Stack

- Python
- Streamlit
- LangChain
- OpenAI Whisper and embeddings
- Google Gemini
- FAISS

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a local `.env` file from the example:

```bash
cp .env.example .env
```

3. Add your API keys:

```env
GOOGLE_KEY=your_google_api_key
OPENAI_KEY=your_openai_api_key
```

4. Run the app:

```bash
streamlit run app.py
```

## Notes

- Real `.env` files are ignored by Git.
- Downloaded audio files are saved in `audios/` and ignored by Git.
- The search tab is present in the UI, but the current app flow only handles direct YouTube URL import.

## Security

Do not commit API keys. This repository previously tracked `.env`; if real keys were committed, rotate those keys in the OpenAI and Google dashboards.
