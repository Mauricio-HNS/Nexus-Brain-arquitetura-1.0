"""Experiment 001 — Adversarial Synthetic World."""

from nexus_brain.adversarial import run_adversarial, summarize_adversarial


def main() -> None:
    results = run_adversarial(
        seeds=range(100),
        steps=5,
        noise=0.08,
        missing_rate=0.15,
    )
    summary = summarize_adversarial(results)

    print("NEXUS EXPERIMENT 003 — ADVERSARIAL SYNTHETIC WORLD")
    print("-" * 58)
    for condition, metrics in summary.items():
        print(f"\n[{condition}]")
        for key, value in metrics.items():
            print(f"{key}: {value:.6f}")

    print("\nInterpretation:")
    print("- Ordered > shuffled is necessary evidence for temporal structure.")
    print("- Null-world gain should remain near zero.")
    print("- Noise and missingness should reduce performance rather than be hidden.")


if __name__ == "__main__":
    main()
