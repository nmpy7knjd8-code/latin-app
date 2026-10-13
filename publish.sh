#!/usr/bin/env bash
# Rebuild phonetics, validate, commit and push the Latin app. Usage: ./publish.sh ["message"] [--strict]
set -euo pipefail
cd "$(dirname "$0")"
PY=/workspace/venv/bin/python; [ -x "$PY" ] || PY=python3
MSG="${1:-Sync content $(date '+%Y-%m-%d %H:%M')}"
STRICT=""; [[ " $* " == *" --strict "* ]] && STRICT=--strict
(cd content && $PY phonetics.py --build)
$PY tools_validate.py $STRICT
git add -A
if git diff --cached --quiet; then echo "nothing to commit"; else
  git -c user.name=nmpy7knjd8-code -c user.email=nmpy7knjd8-code@users.noreply.github.com commit -qm "$MSG"; fi
git pull -q --rebase
git push -q
echo "pushed $(git rev-parse --short HEAD) -> https://nmpy7knjd8-code.github.io/latin-app/"
