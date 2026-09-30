# RowletAI — Indonesian Equity Market Intelligence

RowletAI is a research dashboard for exploring Indonesian equities with Sectors data. It combines market-wide screening with company-level evidence so users can compare signals, inspect peer context, and understand how the displayed metrics were formed.

## Problem statement

Retail investors in Indonesia need a clearer way to screen listed companies and understand their strengths, risks, and relative position; RowletAI turns Sectors market data into an explainable research workflow.

## What the app does

- Screens the company universe by composite and dimension signals.
- Shows company fundamentals, momentum, valuation, and risk evidence.
- Compares a selected company with its peer group.
- Provides a Company Journal with sourced context and methodology notes.
- Supports analysis only; it does not place trades or provide instructions to buy or sell securities.

## Run locally on Windows

The app entry point is `app/dashboard.py`.

1. Install Python 3.10 or newer.
2. From the repository folder, create and activate a virtual environment:

   ```powershell
   py -3 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Create a local environment file and add your Sectors API key:

   ```powershell
   Copy-Item .env.example .env
   ```

   Edit `.env` and set `SECTORS_API_KEY`. Keep `.env` private; it is excluded from Git.

5. Start the app:

   ```powershell
   streamlit run app/dashboard.py
   ```

## Data and API configuration

The dashboard expects these Sectors-derived snapshots in `data/`:

- `bagger_scores.json`
- `fundamentals.json`
- `momentum_scores.json`
- `risk_metrics.json`
- `company_profiles.json`

The app uses the Sectors REST API v2 for live company and daily-market context. Set `SECTORS_API_KEY` in `.env` for local use or in Streamlit secrets for deployment. The app can create local runtime caches such as `daily_cache.json`, `journal_report_cache.json`, and `company_enrichment.json`; these are excluded from Git.

Photo-provider keys are optional. Add `UNSPLASH_ACCESS_KEY`, `PEXELS_API_KEY`, or `PIXABAY_API_KEY` only if you want the corresponding image providers. The app's bundled visual assets do not require those keys.

Do not commit `.env`, `.streamlit/secrets.toml`, or any API credentials. Use `.env.example` as the names-only template.

## Curated peer comparisons

The optional `data/local_peer_groups.json` file contains explicitly curated peer groups used by Compare Insight when a local demonstration group is configured. The current AADI.JK group is an illustrative coal-producer peer set; it is not official index membership, a Sectors-provided classification, or investment advice.

For a configured group, the app uses the local peer symbols and classification before making a sector/company-report lookup for that comparison. Other peer rules use available Sectors membership or local classifications; constrained comparisons are not silently replaced with unrelated companies.

Review the group metadata, source references, and `updated_at` date when maintaining this file.

## Stack

Python, Streamlit, pandas, NumPy, Plotly, and the Sectors REST API v2.

## Sectors Hackathon submission checklist

The official rules require a public repository, a one-minute teaser, a judging walkthrough of up to three minutes, a one-sentence problem statement, track and team details, and a public social post. See the [official rules](https://hackathon.sectors.app/rules) before submission.

Suggested track: **Market Intelligence**.
