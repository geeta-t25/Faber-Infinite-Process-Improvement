# Operational Process Improvement & Efficiency Analytics

A data-driven operational analytics project that analyzes process performance using productivity, quality, cycle time, waiting time, and downtime metrics.

## Overview

The project analyzes operational process data to identify performance gaps between different process stages.

The analysis focuses on five key performance indicators:

- Productivity
- Defect Rate
- Cycle Time
- Waiting Time
- Downtime

Python and Pandas are used for data processing and KPI analysis, while Excel is used to present the results through a management dashboard.

## Project Workflow

Raw Operational Data
        ↓
Data Processing
        ↓
KPI Calculation
        ↓
Process & Shift Comparison
        ↓
Performance Gap Identification
        ↓
Improvement Analysis
        ↓
Dashboard

## Technologies Used

- Python
- Pandas
- NumPy
- Microsoft Excel
- Git & GitHub

## Dataset

The project uses a synthetic operational dataset containing process-level information such as:

- Date
- Process
- Product
- Shift
- Team
- Target Units
- Actual Units
- Cycle Time
- Waiting Time
- Downtime
- Defects
- Rework

The dataset is synthetic and is intended to demonstrate the analysis methodology.

## Key Performance Indicators

### Productivity

Productivity is calculated by comparing actual output with the target output.

`Productivity = Actual Units / Target Units × 100`

### Defect Rate

`Defect Rate = Defects / Actual Units × 100`

### Cycle Time

Average time required to complete a process.

### Waiting Time

Time spent waiting between process activities.

### Downtime

Time during which the process or equipment is unavailable.

## Analysis

The Python analysis aggregates the operational data by process and shift.

The process-level analysis showed that Assembly had comparatively lower productivity and higher defect rate, waiting time, cycle time, and downtime than the other process stages.

This made Assembly the first area selected for further investigation.

The analysis identifies a priority area; it does not by itself establish the underlying root cause. Root-cause investigation would require additional process observations and detailed cause-level data.

## Dashboard

The Excel dashboard provides a management-level view of:

- Overall productivity
- Overall defect rate
- Average cycle time
- Average waiting time
- Average downtime
- Productivity comparison across processes

## Process Improvement Approach

The project connects operational analysis with process-improvement concepts including:

- Lean waste identification
- Kaizen
- 5S
- Pareto analysis
- 5 Why
- Fishbone analysis
- DMAIC

These methods provide a framework for investigating and prioritizing improvement opportunities.

## Running the Project

Install the required Python packages:

```bash
pip install pandas numpy openpyxl