# app.py
import os
import gradio as gr
from bs4 import BeautifulSoup
import numpy as np
import faiss
import langchain
from fastapi import FastAPI

def extract_text(html_or_plain: str) -> str:
    # simple fallback: if looks like HTML, parse with BeautifulSoup
    if "<" in html_or_plain and ">" in html_or_plain:
        soup = BeautifulSoup(html_or_plain, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
    else:
        text = html_or_plain
    return text[:4000]

def build_faiss_summary(text: str):
    # tiny deterministic "embedding" (demo only) -> demonstrates faiss usage
    # convert bytes to a fixed-length float32 vector (toy demo)
    b = text.encode("utf8")[:256].ljust(256, b"\0")
    v = np.frombuffer(b, dtype=np.uint8).astype("float32") / 255.0
    d = v.shape[0]
    index = faiss.IndexFlatL2(d)
    index.add(np.array([v], dtype="float32"))
    return f"FAISS index vectors: {index.ntotal} (dim={d})"

def summarize(text: str):
    # dummy summarizer — placeholder; swap for a real LLM later
    return "DUMMY SUMMARY: " + (text[:200] + ("…" if len(text)>200 else ""))

def pipeline(input_text: str):
    extracted = extract_text(input_text)
    summary = summarize(extracted)
    faiss_info = build_faiss_summary(extracted)
    return extracted, summary, faiss_info, f"langchain=={getattr(langchain,'__version__','unknown')}"

iface = gr.Interface(
    fn=pipeline,
    inputs=gr.Textbox(lines=8, placeholder="Paste HTML or plain text here..."),
    outputs=[
        gr.Textbox(label="Extracted text"),
        gr.Textbox(label="Summary"),
        gr.Textbox(label="FAISS status"),
        gr.Textbox(label="LangChain version")
    ],
    title="AIAgents — quickstart (demo)"
)

# Expose FastAPI app for Uvicorn (used in Docker CMD "uvicorn app:app ...")
app = FastAPI()
app = gr.mount_gradio_app(app, iface, path="/")

if __name__ == "__main__":
    # Local run convenience
    # Launch the Gradio interface locally
    iface.launch(server_name="0.0.0.0", server_port=int(os.environ.get("GRADIO_SERVER_PORT", 7860)))
