# Hobby Stock Tracker - Technical Solution Plan

## Stack & Architecture
- **Backend:** Python (FastAPI)
- **Frontend:** HTML templates (Jinja2 or similar), CSS (Tailwind via CDN), JavaScript (Vue.js via CDN), Leaflet (for any mapping needs, via CDN)
- **Containerization:** Single-container app (Docker)
- **Database:**
  - Use local files for simple key-value or single-object storage.
  - Use SQLite for multiple tables/objects or relational data.
- **Static Assets:**
  - Load Tailwind, Vue, and Leaflet from public CDNs by default.
  - Ask user before switching to in-repo or self-hosted delivery.

## Solution Structure
- **/app/**
  - main.py (FastAPI entrypoint)
  - models.py (Pydantic models, DB models)
  - database.py (SQLite/local file logic)
  - routes/
    - inventory.py
    - wishlist.py
    - ...
  - templates/
    - base.html
    - inventory.html
    - wishlist.html
  - static/
    - (empty, unless user requests self-hosted assets)
- **/Dockerfile** (single container)
- **/requirements.txt**

## Frontend
- Use Jinja2 for server-side rendering of HTML templates.
- Integrate Tailwind CSS via CDN in base.html.
- Integrate Vue.js via CDN for interactive UI components (e.g., quantity counters, search/filter, flagging items).
- Integrate Leaflet via CDN if mapping/location features are added.

## Database
- For basic inventory, use a local JSON or pickle file.
- For multiple entities (inventory, categories, wishlist), use SQLite with SQLAlchemy or encode directly via sqlite3.

## Key Principles
- Keep backend and frontend code separated.
- Use public CDNs for all major frontend libraries unless user requests otherwise.
- All data is persisted locally (no cloud sync).
- Responsive design for desktop/mobile.

---
This plan follows your preferences for Python, FastAPI, containerization, and CDN-first frontend delivery. Let me know if you want to adjust any technology choices or directory structure.