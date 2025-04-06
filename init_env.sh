#!/bin/bash
rm -rf .venv
poetry env use python3.11
source .venv/bin/activate
poetry install --no-root -vvvv
