#!/usr/bin/env bash
set -euo pipefail
python -m src.ingest --source ./data/demos/sample.mp4 --fps 6 --out ./data/raw/run1/
python -m src.pipeline --config ./configs/cam_example.json --input ./data/raw/run1/ --out ./out/run1/
uvicorn src.api:app --reload
