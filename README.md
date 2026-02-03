# Sorting Algorithms

This repository is created for an **experimental study of sorting algorithms** in the **Data Structures and Algorithms (DSA)** course.  
The goal is to compare the **runtime performance** of several common sorting algorithms on large datasets.

---

## Sorting Algorithms

The following sorting algorithms are evaluated in this project:

- **QuickSort**  
  A divide-and-conquer algorithm, implemented in-place, with average time complexity `O(n log n)`.

- **HeapSort**  
  A comparison-based algorithm using a binary heap, with time complexity `O(n log n)` in all cases.

- **MergeSort**  
  A stable divide-and-conquer algorithm with time complexity `O(n log n)`, requiring additional memory.

- **NumPy Sort**  
  Uses `numpy.sort`, which is optimized at the C level and serves as a performance baseline.

---

## Installation
```bash
git clone https://github.com/ks2n/dsa-sorting.git
cd dsa-sorting
pip install -r requirements.txt
```

## Usage

Generate data
```bash
python generate.py --n 1000000 --seed 12345
```

Run
```bash
python benchmark.py --repeat 1
```

## File Structure

```
sorting-bench/
  requirements.txt
  generate.py
  sorts.py
  benchmark.py
  data/
    dataset.npz
  results/
    timings.csv
```
