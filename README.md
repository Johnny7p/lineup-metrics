# lineup-metrics (scaffold)

Lean camera-only metrics: surfers-in-water, ride time/length, ride direction (L/R), top turns. Designed so tube-time can be added later by plugging in a barrel mask.

## Quickstart
1) Create a virtual env and install deps:
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
2) Add third-party repos as submodules (run from repo root):
```bash
git submodule add https://github.com/craigmulligan/crowdfactor third_party/crowdfactor
git submodule add https://github.com/PaoloPiacenti/AI-wave-tracker third_party/ai-wave-tracker
git submodule add https://github.com/theAIGuysCode/yolov4-deepsort third_party/yolo_deepsort
```
(You may swap in ByteTrack if preferred.)

3) Put an MP4/HLS URL in `configs/cam_example.json` and run:
```bash
python -m src.ingest --source ./data/demos/sample.mp4 --fps 6 --out ./data/raw/run1/
python -m src.pipeline --config ./configs/cam_example.json --input ./data/raw/run1/ --out ./out/run1/
uvicorn src.api:app --reload
```

## Notes
- All modules are stubbed with TODOs so you can fill in real logic quickly.
- `tube_time` is not in v0; add it later by introducing a barrel zone mask and overlap logic in `rides.py` / a new `tube.py`.
