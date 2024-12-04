# A-Level 2024 Exam Reschedule Visualization

This repository contains Python code to visualize the **postponement and rescheduling** of the **2024 GCE Advanced Level (A-Level)** examination in Sri Lanka. The visualizations represent how the exam dates were affected by extreme weather conditions and the two methods of rescheduling. The project uses **Plotly** to create interactive plots for better analysis.

## Overview

The Sri Lankan A-Level exams in 2024 faced delays due to extreme weather conditions, leading to a rescheduling of certain subjects. This repository includes visualizations that compare two possible ways the exams could have been rescheduled:

- **Actual Rescheduling**: Shows how the exams were rescheduled after the disruption, with dates marked in different colors.
- **Alternative Rescheduling**: Proposes an alternative way of rescheduling, where all exams are postponed collectively within a week.

## Visualizations

### 1. **Scatter Plot for Affected and New Exam Dates**:
- **Green**: Original exam dates (unchanged).
- **Red**: Affected (postponed) exam dates.
- **Blue**: New rescheduled dates.

### 2. **Line Graphs**:
Shows the relationship between the original and rescheduled dates for each subject. It clearly indicates the gaps between different parts of the exams.

### 3. **Gap Analysis**:
Shows the differences between the original and new gaps between parts of each subject.

### 4. **Postponed Days Graph**:
Visualizes the number of days each part of the subjects was postponed for both the actual and alternative methods.

## Requirements

To run this code, you'll need the following Python libraries:

- **pandas**: For data manipulation.
- **numpy**: For numerical operations.
- **plotly**: For creating interactive plots.

You can install the required dependencies using `pip`:

```bash
pip install pandas numpy plotly
