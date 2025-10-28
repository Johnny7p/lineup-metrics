# Simple pipeline runner (stub)
import argparse, json, os
def run(config_path, input_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    cfg = json.load(open(config_path))
    # TODO: wire ingest outputs to detection, tracking, rides, metrics, export
    open(os.path.join(out_dir, 'summary.json'),'w').write('{}')
    print(f'Wrote summary.json to {out_dir}')
if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', required=True)
    ap.add_argument('--input', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    run(args.config, args.input, args.out)
