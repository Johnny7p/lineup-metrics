import cv2, os, argparse
def grab_frames(source, fps, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open source: {source}")
    frame_interval = max(1, int(round(cap.get(cv2.CAP_PROP_FPS) / max(1, fps))))
    i = 0; saved = 0
    while True:
        ret, frame = cap.read()
        if not ret: break
        if i % frame_interval == 0:
            path = os.path.join(out_dir, f"frame_{i:06d}.jpg")
            cv2.imwrite(path, frame); saved += 1
        i += 1
    cap.release()
    print(f"Saved {saved} frames to {out_dir}")
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--fps", type=int, default=6)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    grab_frames(args.source, args.fps, args.out)
