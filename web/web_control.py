"""Website shortcuts and web searches."""
import webbrowser
from urllib.parse import quote_plus

WEBSITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "github": "https://github.com",
    "chatgpt": "https://chatgpt.com",
    "stackoverflow": "https://stackoverflow.com",
    "wikipedia": "https://www.wikipedia.org",
    "linkedin": "https://www.linkedin.com",
    "reddit": "https://www.reddit.com",
}


def open_website(name: str) -> str:
    name = name.lower().strip()
    url = WEBSITES.get(name)
    if not url:
        return "Website not found. Try Google, YouTube, Gmail, GitHub, ChatGPT, Wikipedia, LinkedIn, Reddit, or Stack Overflow."
    webbrowser.open(url)
    return f"Opening {name}."


def _search(query: str, url: str, label: str) -> str:
    query = query.strip()
    if not query:
        return "Please tell me what to search."
    webbrowser.open(url + quote_plus(query))
    return f"Searching {label} for {query}."


def google_search(query: str) -> str:
    return _search(query, "https://www.google.com/search?q=", "Google")


def youtube_search(query: str) -> str:
    return _search(query, "https://www.youtube.com/results?search_query=", "YouTube")


def github_search(query: str) -> str:
    return _search(query, "https://github.com/search?q=", "GitHub")


def wikipedia_search(query: str) -> str:
    return _search(query, "https://en.wikipedia.org/wiki/Special:Search?search=", "Wikipedia")
