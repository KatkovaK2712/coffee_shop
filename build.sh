#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

mkdir -p staticfiles/media
cp -r media/* staticfiles/media/ 2>/dev/null || true
cp -r coffee_shop/media/* staticfiles/media/ 2>/dev/null || true
