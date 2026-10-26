"""Phase 2 starter: generate fake support tickets, then explore them with pandas.

Run:  python phase-2-data-libraries/explore_tickets.py
Read every line. Then do the "YOUR TURN" tasks at the bottom.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # draw to files, no window needed
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT_DIR = Path(__file__).parent / "output"
OUT_DIR.mkdir(exist_ok=True)


def make_tickets(n: int = 1000, seed: int = 42) -> pd.DataFrame:
    """Create a fake ticket dataset with some deliberate messiness."""
    rng = np.random.default_rng(seed)
    categories = ["billing", "login", "device", "sync", "other"]
    priorities = ["low", "medium", "high"]

    created = pd.Timestamp("2026-09-01") + pd.to_timedelta(
        rng.integers(0, 60 * 24 * 30, n), unit="m"
    )
    category = rng.choice(categories, n, p=[0.2, 0.25, 0.25, 0.2, 0.1])
    priority = rng.choice(priorities, n, p=[0.5, 0.35, 0.15])

    base_hours = {"billing": 12, "login": 4, "device": 20, "sync": 10, "other": 8}
    hours = np.array([rng.exponential(base_hours[c]) for c in category])
    resolved = created + pd.to_timedelta(hours, unit="h")

    df = pd.DataFrame(
        {
            "ticket_id": np.arange(1, n + 1),
            "created_at": created,
            "resolved_at": resolved,
            "category": category,
            "priority": priority,
            "csat": rng.integers(1, 6, n).astype(float),
        }
    )
    # Messiness: some missing satisfaction scores and unresolved tickets
    df.loc[rng.choice(n, 120, replace=False), "csat"] = np.nan
    df.loc[rng.choice(n, 40, replace=False), "resolved_at"] = pd.NaT
    return df


def main() -> None:
    df = make_tickets()

    print("--- First rows ---")
    print(df.head())
    print("\n--- Info ---")
    df.info()
    print("\n--- Missing values ---")
    print(df.isna().sum())

    # New column: hours to resolve
    df["resolution_hours"] = (df["resolved_at"] - df["created_at"]).dt.total_seconds() / 3600

    print("\n--- Tickets by category ---")
    by_cat = df.groupby("category").agg(
        tickets=("ticket_id", "count"),
        median_hours=("resolution_hours", "median"),
        avg_csat=("csat", "mean"),
    )
    print(by_cat.sort_values("tickets", ascending=False).round(2))

    # Chart 1: median resolution time by category
    ax = by_cat["median_hours"].sort_values().plot(kind="barh")
    ax.set_xlabel("Median resolution time (hours)")
    ax.set_title("Resolution time by category")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "resolution_by_category.png")
    plt.close()

    # Chart 2: tickets per day
    daily = df.set_index("created_at").resample("D")["ticket_id"].count()
    ax = daily.plot()
    ax.set_ylabel("Tickets created")
    ax.set_title("Daily ticket volume")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "daily_volume.png")
    plt.close()

    print(f"\nCharts saved to {OUT_DIR}")

    # ------------------------------------------------------------------
    # YOUR TURN (write your code below, one task at a time, commit each):
    # 1. What share of tickets are still unresolved? By category?
    # 2. For resolved tickets, what % took longer than 24 hours, by priority?
    # 3. Does average csat differ by category? Handle the missing values and explain
    #    your choice (drop rows? fill? ignore in the mean?).
    # 4. Add a weekday column (df["created_at"].dt.day_name()) and chart tickets by weekday.
    # 5. Save df to SQLite with df.to_sql(...), then answer task 2 with a SQL query
    #    using pandas.read_sql. Do the two answers match?
    # ------------------------------------------------------------------


if __name__ == "__main__":
    main()
