#!/bin/bash
set -exu

poetry install --no-ansi
poetry run pip-audit
poetry run pytest