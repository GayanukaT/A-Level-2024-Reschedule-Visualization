import pandas as pd
import numpy as np
import plotly.graph_objects as go

data = [
    {"Subject": "Combined Mathematics", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Combined Mathematics", "Part": "II", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Buddhism", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Buddhism", "Part": "II", "Original Date": "2024-11-26", "Rescheduled Date": "2024-11-26"},
    {"Subject": "Hinduism", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Hinduism", "Part": "II", "Original Date": "2024-11-26", "Rescheduled Date": "2024-11-26"},
    {"Subject": "Christianity", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Christianity", "Part": "II", "Original Date": "2024-11-26", "Rescheduled Date": "2024-11-26"},
    {"Subject": "Islam", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Islam", "Part": "II", "Original Date": "2024-11-26", "Rescheduled Date": "2024-11-26"},
    {"Subject": "Buddhist Civilization", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Buddhist Civilization", "Part": "II", "Original Date": "2024-11-26", "Rescheduled Date": "2024-11-26"},
    {"Subject": "Hindu Civilization", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Hindu Civilization", "Part": "II", "Original Date": "2024-11-26", "Rescheduled Date": "2024-11-26"},
    {"Subject": "Islamic Civilization", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Islamic Civilization", "Part": "II", "Original Date": "2024-11-26", "Rescheduled Date": "2024-11-26"},
    {"Subject": "Christian Civilization", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Christian Civilization", "Part": "II", "Original Date": "2024-11-26", "Rescheduled Date": "2024-11-26"},
    {"Subject": "Biology", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Biology", "Part": "II", "Original Date": "2024-11-26", "Rescheduled Date": "2024-11-26"},
    {"Subject": "Economics", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Economics", "Part": "II", "Original Date": "2024-11-26", "Rescheduled Date": "2024-11-26"},
    {"Subject": "Logic & Scientific Method", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Logic & Scientific Method", "Part": "II", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Art", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Art", "Part": "II", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Art", "Part": "III", "Original Date": "2024-12-02", "Rescheduled Date": "2024-12-30"},
    {"Subject": "Dancing (Indigenous)", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Dancing (Indigenous)", "Part": "II", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-23"},
    {"Subject": "Dancing (Bharatha)", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Dancing (Bharatha)", "Part": "II", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-23"},
    {"Subject": "Oriental Music", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Oriental Music", "Part": "II", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-23"},
    {"Subject": "Carnatic Music", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Carnatic Music", "Part": "II", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-23"},
    {"Subject": "Western Music", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Western Music", "Part": "II", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-23"},
    {"Subject": "Engineering Technology", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Engineering Technology", "Part": "II", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Bio Systems Technology", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Bio Systems Technology", "Part": "II", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Agricultural Science", "Part": "I", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-23"},
    {"Subject": "Agricultural Science", "Part": "II", "Original Date": "2024-11-30", "Rescheduled Date": "2024-12-28"},
    {"Subject": "Business Studies", "Part": "I", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-23"},
    {"Subject": "Business Studies", "Part": "II", "Original Date": "2024-12-02", "Rescheduled Date": "2024-12-30"},
    {"Subject": "German", "Part": "I", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-23"},
    {"Subject": "German", "Part": "II", "Original Date": "2024-11-30", "Rescheduled Date": "2024-12-28"},
    {"Subject": "Physics", "Part": "I", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Physics", "Part": "II", "Original Date": "2024-12-02", "Rescheduled Date": "2024-12-30"},
    {"Subject": "Pali", "Part": "I", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Pali", "Part": "II", "Original Date": "2024-12-02", "Rescheduled Date": "2024-12-30"},
    {"Subject": "Sinhala", "Part": "I", "Original Date": "2024-11-30", "Rescheduled Date": "2024-12-28"},
    {"Subject": "Sinhala", "Part": "II", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Tamil", "Part": "I", "Original Date": "2024-11-30", "Rescheduled Date": "2024-12-28"},
    {"Subject": "Tamil", "Part": "II", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Civil Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Civil Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Mechanical Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Mechanical Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Electrical, Electronic and Information Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Electrical, Electronic and Information Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Food Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Food Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Agro Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Agro Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Bio Resource Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Bio Resource Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Business Statistics", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Business Statistics", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Sanskrit", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Sanskrit", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Chemistry", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Chemistry", "Part": "II", "Original Date": "2024-12-06", "Rescheduled Date": "2024-12-06"},
    {"Subject": "Science for Technology", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Science for Technology", "Part": "II", "Original Date": "2024-12-06", "Rescheduled Date": "2024-12-06"},
    {"Subject": "Drama & Theatre (Sinhala)", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Drama & Theatre (Sinhala)", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Drama & Theatre (Tamil)", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Drama & Theatre (Tamil)", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Drama & Theatre (English)", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Drama & Theatre (English)", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Political Science", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Political Science", "Part": "II", "Original Date": "2024-12-06", "Rescheduled Date": "2024-12-06"},
    {"Subject": "French", "Part": "I", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-05"},
    {"Subject": "French", "Part": "II", "Original Date": "2024-12-06", "Rescheduled Date": "2024-12-06"},
    {"Subject": "Common General Test", "Part": "", "Original Date": "2024-12-07", "Rescheduled Date": "2024-12-07"},
    {"Subject": "English", "Part": "I", "Original Date": "2024-12-07", "Rescheduled Date": "2024-12-07"},
    {"Subject": "English", "Part": "II", "Original Date": "2024-12-10", "Rescheduled Date": "2024-12-10"},
    {"Subject": "General English", "Part": "II", "Original Date": "2024-12-09", "Rescheduled Date": "2024-12-09"},
    {"Subject": "General English", "Part": "I", "Original Date": "2024-12-09", "Rescheduled Date": "2024-12-09"},
    {"Subject": "Home Economics", "Part": "I", "Original Date": "2024-12-10", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Home Economics", "Part": "II", "Original Date": "2024-12-12", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Accounting", "Part": "I", "Original Date": "2024-12-10", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Accounting", "Part": "II", "Original Date": "2024-12-13", "Rescheduled Date": "2024-12-13"},
    {"Subject": "History", "Part": "II", "Original Date": "2024-12-11", "Rescheduled Date": "2024-12-11"},
    {"Subject": "History", "Part": "I", "Original Date": "2024-12-13", "Rescheduled Date": "2024-12-13"},
    {"Subject": "Arabic", "Part": "I", "Original Date": "2024-12-11", "Rescheduled Date": "2024-12-11"},
    {"Subject": "Arabic", "Part": "II", "Original Date": "2024-12-13", "Rescheduled Date": "2024-12-13"},
    {"Subject": "Malay", "Part": "I", "Original Date": "2024-12-11", "Rescheduled Date": "2024-12-11"},
    {"Subject": "Malay", "Part": "II", "Original Date": "2024-12-13", "Rescheduled Date": "2024-12-13"},
    {"Subject": "Chinese", "Part": "I", "Original Date": "2024-12-11", "Rescheduled Date": "2024-12-11"},
    {"Subject": "Chinese", "Part": "II", "Original Date": "2024-12-13", "Rescheduled Date": "2024-12-13"},
    {"Subject": "Information & Communication Technology", "Part": "I", "Original Date": "2024-12-12", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Information & Communication Technology", "Part": "II", "Original Date": "2024-12-16", "Rescheduled Date": "2024-12-16"},
    {"Subject": "Hindi", "Part": "I", "Original Date": "2024-12-16", "Rescheduled Date": "2024-12-16"},
    {"Subject": "Hindi", "Part": "II", "Original Date": "2024-12-19", "Rescheduled Date": "2024-12-19"},
    {"Subject": "Korean", "Part": "I", "Original Date": "2024-12-16", "Rescheduled Date": "2024-12-16"},
    {"Subject": "Korean", "Part": "II", "Original Date": "2024-12-19", "Rescheduled Date": "2024-12-19"},
    {"Subject": "Mathematics", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-17"},
    {"Subject": "Mathematics", "Part": "II", "Original Date": "2024-12-18", "Rescheduled Date": "2024-12-18"},
    {"Subject": "Higher Mathematics", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-17"},
    {"Subject": "Higher Mathematics", "Part": "II", "Original Date": "2024-12-20", "Rescheduled Date": "2024-12-20"},
    {"Subject": "Geography", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-17"},
    {"Subject": "Geography", "Part": "II", "Original Date": "2024-12-18", "Rescheduled Date": "2024-12-18"},
    {"Subject": "Greek and Roman Civilization", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-17"},
    {"Subject": "Greek and Roman Civilization", "Part": "II", "Original Date": "2024-12-20", "Rescheduled Date": "2024-12-20"},
    {"Subject": "Russian", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-17"},
    {"Subject": "Russian", "Part": "II", "Original Date": "2024-12-18", "Rescheduled Date": "2024-12-18"},
    {"Subject": "Japanese", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-17"},
    {"Subject": "Japanese", "Part": "II", "Original Date": "2024-12-18", "Rescheduled Date": "2024-12-18"},
    {"Subject": "Communication & Media Studies", "Part": "I", "Original Date": "2024-12-19", "Rescheduled Date": "2024-12-19"},
    {"Subject": "Communication & Media Studies", "Part": "II", "Original Date": "2024-12-20", "Rescheduled Date": "2024-12-20"}
]

df = pd.DataFrame(data)
df["Original Date"] = pd.to_datetime(df["Original Date"])
df["Rescheduled Date"] = pd.to_datetime(df["Rescheduled Date"])

fig = go.Figure()

new_date_start = pd.Timestamp("2024-12-21")
new_date_end = pd.Timestamp("2024-12-31")

for subject in df["Subject"].unique():
    subject_data = df[df["Subject"] == subject]

    fig.add_trace(go.Scatter(
        x=subject_data["Original Date"],
        y=[subject] * len(subject_data),
        mode="lines+markers",
        name=f"{subject} - Original",
        line=dict(color="red"),
        marker=dict(size=8, symbol="square"),
        showlegend=False
    ))

    for _, row in subject_data.iterrows():
        is_new_date = new_date_start <= row["Rescheduled Date"] <= new_date_end
        color = "blue" if is_new_date else "green"

        fig.add_trace(go.Scatter(
            x=[row["Rescheduled Date"]],
            y=[row["Subject"]],
            mode="markers",
            marker=dict(size=8, symbol="square", color=color),
            showlegend=False
        ))

    for i in range(len(subject_data) - 1):
        part1 = subject_data.iloc[i]
        part2 = subject_data.iloc[i + 1]

        is_new_line = (
            new_date_start <= part1["Rescheduled Date"] <= new_date_end or
            new_date_start <= part2["Rescheduled Date"] <= new_date_end
        )
        line_color = "blue" if is_new_line else "green"

        fig.add_trace(go.Scatter(
            x=[part1["Rescheduled Date"], part2["Rescheduled Date"]],
            y=[subject, subject],
            mode="lines",
            line=dict(color=line_color),
            showlegend=False
        ))

highlight_days = [
    "2024-11-27", "2024-11-28", "2024-11-29", "2024-11-30", "2024-12-01",
    "2024-12-02", "2024-12-03", "2024-12-08", "2024-12-14", "2024-12-15",
    "2024-12-21", "2024-12-22", "2024-12-23", "2024-12-24", "2024-12-25",
    "2024-12-26", "2024-12-27", "2024-12-28", "2024-12-29", "2024-12-30",
    "2024-12-31",
]

highlight_colors = [
    "rgba(255, 0, 0, 0.8)", "rgba(255, 0, 0, 0.8)", "rgba(255, 0, 0, 0.8)", 
    "rgba(255, 0, 0, 0.8)", "rgba(255, 0, 0, 0.5)", "rgba(255, 0, 0, 0.8)", 
    "rgba(255, 0, 0, 0.8)", "rgba(0, 255, 0, 0.5)", "rgba(0, 255, 0, 0.5)", 
    "rgba(0, 255, 0, 0.5)", "rgba(0, 0, 255, 0.8)", "rgba(0, 0, 255, 0.5)",
    "rgba(0, 0, 255, 0.8)", "rgba(0, 0, 255, 0.5)", "rgba(0, 0, 255, 0.5)",
    "rgba(0, 0, 255, 0.5)", "rgba(0, 0, 255, 0.8)", "rgba(0, 0, 255, 0.8)",
    "rgba(0, 0, 255, 0.5)", "rgba(0, 0, 255, 0.8)", "rgba(0, 0, 255, 0.8)",
]

for i, day in enumerate(highlight_days):
    fig.add_shape(
        type="line",
        x0=day, x1=day,
        y0=0, y1=len(df["Subject"].unique()),
        line=dict(color=highlight_colors[i], width=2)
    )

fig.update_xaxes(
    showgrid=True,
    gridcolor='lightgrey',
    gridwidth=0.5
)

fig.update_yaxes(
    showgrid=True,
    gridcolor='lightgrey',
    gridwidth=0.5
)

fig.update_layout(
    template='ggplot2',
    plot_bgcolor='#ffe6f2',
    title='Visualizing How the A-Level 2024 Exam Was Postponed and Rescheduled',
    margin=dict(t=200),
    xaxis=dict(
        title="Dates",
        tickvals=pd.date_range("2024-11-25", "2024-12-31"),
        ticktext=[date.strftime('%m/%d') for date in pd.date_range("2024-11-25", "2024-12-31")],
        tickangle=270,
        tickfont=dict(size=14),
        side='top',
        range=["2024-11-24", "2025-01-01"],
    ),
    yaxis=dict(
        title="Subjects",
        tickvals=df["Subject"].unique(),
        ticktext=df["Subject"].unique(),
        tickangle=0,
        tickfont=dict(size=14),
        range=[len(df["Subject"].unique()), -1]
    ),
    height=1500,
    width=1200,
)

fig.show()