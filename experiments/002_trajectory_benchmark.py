"""Experiment 002 — Snapshot vs Trajectory."""
from nexus_brain.benchmark import run_benchmark, summarize

def main():
    summary = summarize(run_benchmark(seeds=range(50), steps=5, noise=0.03))
    print("NEXUS EXPERIMENT 002 — SNAPSHOT VS TRAJECTORY")
    print("-" * 52)
    for key, value in summary.items():
        print(f"{key}: {value:.6f}")

if __name__ == "__main__":
    main()
