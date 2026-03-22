import json
from pathlib import Path
from datetime import datetime


def load_articles(directory):
    """Load all JSON articles from `directory`.

    Each file should be a valid JSON object. The function returns a list of
    dicts sorted by the `date` field (ISO format) descending when available.
    Files are given a `slug` derived from the filename if not present.
    """
    p = Path(directory)
    if not p.exists() or not p.is_dir():
        return []

    articles = []
    for file in sorted(p.glob("*.json")):
        try:
            raw = file.read_text(encoding="utf-8")
            data = json.loads(raw)
        except Exception:
            # skip files we can't read/parse
            continue

        if not isinstance(data, dict):
            continue

        # use filename as slug if not provided
        data.setdefault("slug", file.stem)

        # parse optional ISO date for sorting
        date_val = data.get("date")
        if isinstance(date_val, str):
            try:
                data["_date_obj"] = datetime.fromisoformat(date_val)
            except Exception:
                data["_date_obj"] = None
        else:
            data["_date_obj"] = None

        articles.append(data)

    # sort newest first by parsed date (missing dates go last)
    articles.sort(key=lambda a: a.get("_date_obj") or datetime.min, reverse=True)

    # clean helper keys and normalize date back to ISO string when possible
    for a in articles:
        if a.get("_date_obj"):
            a["date"] = a["_date_obj"].isoformat()
        a.pop("_date_obj", None)

    return articles
