import argparse
import numpy as np
import os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=1_000_000)
    ap.add_argument("--seed", type=int, default=12345)
    ap.add_argument("--out", type=str, default="data/dataset.npz")
    args = ap.parse_args()

    os.makedirs("data", exist_ok=True)
    rng = np.random.default_rng(args.seed)
    n = args.n

    data = {}

    # 5 float
    inc_f = np.linspace(-1e6, 1e6, n, dtype=np.float64)
    data["float_inc"] = inc_f
    data["float_dec"] = inc_f[::-1].copy()
    for i in range(3):
        data[f"float_rand_{i+1}"] = rng.uniform(-1e6, 1e6, n).astype(np.float64)

    # 5 int
    inc_i = rng.integers(-10_000_000, 10_000_000, size=n, dtype=np.int64)
    inc_i.sort()
    data["int_inc"] = inc_i
    data["int_dec"] = inc_i[::-1].copy()
    for i in range(3):
        data[f"int_rand_{i+1}"] = rng.integers(-10_000_000, 10_000_000, size=n, dtype=np.int64)

    np.savez_compressed(args.out, **data)
    print("Saved:", args.out)
    print("Keys:", ", ".join(data.keys()))

if __name__ == "__main__":
    main()