Render deployment notes
======================

This file lists exact steps to make Render run this Django project correctly.

1) Repo changes (already applied)
- `Procfile` at the repo root: `web: gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT`
- `render.yaml` at the repo root with `startCommand: ./start.sh` (we removed `name:`)
- `start.sh` at the repo root which runs `collectstatic` and starts gunicorn

2) Required environment variables (set these in Render dashboard > Environment)
- `DJANGO_SECRET_KEY` : set to a secure random value
- `DJANGO_DEBUG` : `False`
- Optional: `DATABASE_URL` : if you use Render Postgres

3) Dashboard steps (the critical part)
- Open Render Dashboard → Services → select your web service for this repository.
- Confirm the service is linked to `johannmarqueta/Finals` and branch `main`.
- IMPORTANT: Remove any explicit **Start Command** value from the service settings. If a Start Command is present it overrides `render.yaml` and `Procfile`.
  - If you prefer to set it explicitly, set the Start Command to exactly one of the following:
    - `./start.sh`
    - `gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT`

4) Trigger a redeploy
- Either push a commit, or in the Deploys tab click **Manual Deploy** → **Deploy latest commit**.

5) Verify deploy logs
- After the build completes, look for the runtime line showing the command Render executed, e.g.:
  - `==> Running './start.sh'`
  or
  - `==> Running 'gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT'`
- If you still see `==> Running 'gunicorn app:app'`, the dashboard Start Command override is still present on the service — remove it.

6) Render CLI (optional)
- If you prefer to update the service from the terminal, install the Render CLI and run it locally. The dashboard UI is easiest for changing the Start Command.

Notes
- Gunicorn will fail on Windows due to the `fcntl` module; use `python manage.py runserver` locally for development, or test Gunicorn in WSL/Docker/Render.
- We added WhiteNoise and `STATICFILES_STORAGE` to `settings.py`, and added a `collectstatic` step in `start.sh`.

If you want, I can:
- walk you through the dashboard settings step-by-step while you have the dashboard open, or
- provide Render CLI commands if you prefer to run them locally (you must authenticate with Render CLI).
