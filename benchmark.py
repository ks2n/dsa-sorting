import argparse
import os
import time
import gc
import numpy as np
import pandas as pd

from sorts import quicksort, heapsort, mergesort

def is_sorted_list(a):
    return all(a[i] <= a[i + 1] for i in range(len(a) - 1))

def is_sorted_np(a):
    return bool(np.all(a[:-1] <= a[1:]))

def bench_one(algo_name, arr_np):
    """Return seconds, ok."""
    if algo_name == "NumPySort":
        x = arr_np.copy()
        t0 = time.perf_counter()
        y = np.sort(x)
        sec = time.perf_counter() - t0
        ok = is_sorted_np(y)
        return sec, ok

    # list-based algorithms
    a = arr_np.tolist()
    t0 = time.perf_counter()
    if algo_name == "QuickSort":
        quicksort(a)
    elif algo_name == "HeapSort":
        heapsort(a)
    elif algo_name == "MergeSort":
        mergesort(a)
    else:
        raise ValueError("Unknown algo")
    sec = time.perf_counter() - t0
    ok = is_sorted_list(a)
    return sec, ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=str, default="data/dataset.npz")
    ap.add_argument("--repeat", type=int, default=1)
    ap.add_argument("--out", type=str, default="results/timings.csv")
    ap.add_argument("--only", type=str, default="QuickSort,HeapSort,MergeSort,NumPySort")
    args = ap.parse_args()

    os.makedirs("results", exist_ok=True)
    ds = np.load(args.data)
    keys = list(ds.keys())

    algos = [x.strip() for x in args.only.split(",") if x.strip()]

    rows = []
    for key in keys:
        arr = ds[key]
        for algo in algos:
            for rep in range(1, args.repeat + 1):
                gc.collect()
                sec, ok = bench_one(algo, arr)
                if not ok:
                    raise RuntimeError(f"Sort failed: {algo} on {key}")
                rows.append({
                    "sequence": key,
                    "dtype": str(arr.dtype),
                    "n": int(arr.shape[0]),
                    "algorithm": algo,
                    "repeat": rep,
                    "seconds": sec
                })
                print(f"{key:12s} | {algo:8s} | rep {rep} | {sec:.3f}s")

    df = pd.DataFrame(rows)
    df.to_csv(args.out, index=False)
    print("Saved:", args.out)

if __name__ == "__main__":
    main()