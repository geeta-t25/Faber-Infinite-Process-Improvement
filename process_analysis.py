"""
Faber Infinite - Process Improvement & Operational Efficiency
Run: python process_analysis.py
"""
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / "process_data.csv", parse_dates=["Date"])

# Overall KPIs
overall = {
    "Records": len(df),
    "Total Target Units": int(df["Target_Units"].sum()),
    "Total Actual Units": int(df["Actual_Units"].sum()),
    "Average Productivity %": round(df["Productivity_%"].mean(), 2),
    "Average Defect Rate %": round(df["Defect_Rate_%"].mean(), 2),
    "Average Cycle Time (min)": round(df["Cycle_Time_Min"].mean(), 2),
    "Average Waiting Time (min)": round(df["Waiting_Time_Min"].mean(), 2),
    "Average Downtime (min)": round(df["Downtime_Min"].mean(), 2),
}
print("\n=== OVERALL KPIs ===")
for k, v in overall.items():
    print(f"{k}: {v}")

# Process comparison
process_summary = df.groupby("Process").agg(
    Records=("Process","size"),
    Productivity_pct=("Productivity_%","mean"),
    Defect_Rate_pct=("Defect_Rate_%","mean"),
    Cycle_Time_Min=("Cycle_Time_Min","mean"),
    Waiting_Time_Min=("Waiting_Time_Min","mean"),
    Downtime_Min=("Downtime_Min","mean"),
    Actual_Units=("Actual_Units","sum"),
).round(2).sort_values("Productivity_pct")

print("\n=== PROCESS SUMMARY ===")
print(process_summary)

# Shift comparison
shift_summary = df.groupby("Shift").agg(
    Productivity_pct=("Productivity_%","mean"),
    Defect_Rate_pct=("Defect_Rate_%","mean"),
    Waiting_Time_Min=("Waiting_Time_Min","mean"),
    Downtime_Min=("Downtime_Min","mean")
).round(2)

# Pareto of defects by process
pareto = df.groupby("Process")["Defects"].sum().sort_values(ascending=False).to_frame("Defects")
pareto["Cumulative_%"] = (pareto["Defects"].cumsum()/pareto["Defects"].sum()*100).round(2)

# Simple prioritization rule
process_summary["Priority"] = "Monitor"
process_summary.loc[
    (process_summary["Productivity_pct"] < df["Productivity_%"].mean()) |
    (process_summary["Defect_Rate_pct"] > df["Defect_Rate_%"].mean()),
    "Priority"
] = "Improve"

# Export analysis
out = BASE / "outputs"
out.mkdir(exist_ok=True)
process_summary.to_csv(out / "process_summary.csv")
shift_summary.to_csv(out / "shift_summary.csv")
pareto.to_csv(out / "defect_pareto.csv")

print("\n=== PRIORITY PROCESSES ===")
print(process_summary[process_summary["Priority"]=="Improve"][[
    "Productivity_pct","Defect_Rate_pct","Waiting_Time_Min","Downtime_Min","Priority"
]])

print("\n=== LEAN INTERPRETATION ===")
print("- High waiting time -> investigate Waiting waste.")
print("- High defects/rework -> investigate Defects and root causes.")
print("- High cycle time -> investigate Overprocessing / bottlenecks.")
print("- High downtime -> investigate equipment/process availability.")
print("\nFiles written to outputs/")
