"""
Creates a simulated improvement scenario for interview demonstration.
IMPORTANT: "After" values are scenario estimates, not real client results.
"""
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / "process_data.csv")

before = {
    "Productivity %": df["Productivity_%"].mean(),
    "Defect Rate %": df["Defect_Rate_%"].mean(),
    "Cycle Time (min)": df["Cycle_Time_Min"].mean(),
    "Waiting Time (min)": df["Waiting_Time_Min"].mean(),
    "Downtime (min)": df["Downtime_Min"].mean()
}

# Scenario assumptions based on process-improvement actions
after = {
    "Productivity %": min(before["Productivity %"] * 1.10, 100),
    "Defect Rate %": before["Defect Rate %"] * 0.75,
    "Cycle Time (min)": before["Cycle Time (min)"] * 0.90,
    "Waiting Time (min)": before["Waiting Time (min)"] * 0.70,
    "Downtime (min)": before["Downtime (min)"] * 0.80
}

comparison = pd.DataFrame({"Before": before, "After (Scenario)": after})
comparison["Change %"] = ((comparison["After (Scenario)"]-comparison["Before"])/comparison["Before"]*100).round(2)

print("\n=== BEFORE vs AFTER SCENARIO ===")
print(comparison.round(2))
comparison.to_csv(BASE / "outputs" / "before_after_scenario.csv")
