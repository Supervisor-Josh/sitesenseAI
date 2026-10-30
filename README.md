# SiteSense Backend

Minimal, free-to-run MVP backend for SiteSense. It uses FastAPI, SQLite, and
Gemma through the Google AI Studio Gemini API. No paid hosting or PostgreSQL
account is required for the demo.

## Fastest setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Create a free API key in [Google AI Studio](https://aistudio.google.com/apikey)
and put it in `.env`:

```env
GEMINI_API_KEY=your-key-here
GEMMA_MODEL=gemma-3-27b-it
```

The configured model is sent to the Gemini API as `models/{GEMMA_MODEL}`.
Change it if Google AI Studio shows a different Gemma model available to your
key. Never commit `.env` or the API key.

Start the API:

```bash
uvicorn main:app --reload
```

The default database is the local `sitesense.db` SQLite file. PostgreSQL is
still supported by setting `DATABASE_URL`, but it is not needed for this MVP.

## MVP flow

- `GET /health` — API health
- `POST /analyses` — sends submitted text to Gemma and stores the result
- `GET /analyses` — returns local analysis history

Example request:

```bash
curl -X POST http://localhost:8000/analyses \
  -H 'Content-Type: application/json' \
  -d '{"input_text":"A clinic website is hard to use on mobile."}'
```

## Frontend

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`. Set `VITE_API_URL` only when the API is not
running at `http://localhost:8000`.

## Deliberate MVP limits

This time-boxed demo has no user accounts, hosted database, payment-based
hosting, or production authentication. History is local to the machine
running the backend. These can be added after the core Gemma workflow is
demonstrated.
