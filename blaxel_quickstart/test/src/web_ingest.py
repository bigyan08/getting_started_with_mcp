import trafilatura
import requests
from memory import summarize, add_note


def ingest_url(url:str):
    download = trafilatura.fetch_url(url)
    if not download:
        return "Could not fetch"
    article = trafilatura.extract(download)
    if not article:
        return "Content not found."
    
    if len(article.strip()) > 1000:
        article = article[:1000]
    summary = summarize(article)
    add_note(summary)
    return summary

