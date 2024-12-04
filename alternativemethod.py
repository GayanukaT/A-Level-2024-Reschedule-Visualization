import pandas as pd
import numpy as np
import plotly.graph_objects as go

data = [
    {"Subject": "Combined Mathematics", "Part": "I", "Original Date": "2024-11-25", "Rescheduled Date": "2024-11-25"},
    {"Subject": "Combined Mathematics", "Part": "II", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-04"},
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
    {"Subject": "Logic & Scientific Method", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Logic & Scientific Method", "Part": "II", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-06"},
    {"Subject": "Art", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Art", "Part": "II", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-06"},
    {"Subject": "Art", "Part": "III", "Original Date": "2024-12-02", "Rescheduled Date": "2024-12-09"},
    {"Subject": "Dancing (Indigenous)", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Dancing (Indigenous)", "Part": "II", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Dancing (Bharatha)", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Dancing (Bharatha)", "Part": "II", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Oriental Music", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Oriental Music", "Part": "II", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Carnatic Music", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Carnatic Music", "Part": "II", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Western Music", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Western Music", "Part": "II", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Engineering Technology", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Engineering Technology", "Part": "II", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-06"},
    {"Subject": "Bio Systems Technology", "Part": "I", "Original Date": "2024-11-27", "Rescheduled Date": "2024-12-04"},
    {"Subject": "Bio Systems Technology", "Part": "II", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-06"},
    {"Subject": "Agricultural Science", "Part": "I", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Agricultural Science", "Part": "II", "Original Date": "2024-11-30", "Rescheduled Date": "2024-12-07"},
    {"Subject": "Business Studies", "Part": "I", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-05"},
    {"Subject": "Business Studies", "Part": "II", "Original Date": "2024-12-02", "Rescheduled Date": "2024-12-09"},
    {"Subject": "German", "Part": "I", "Original Date": "2024-11-28", "Rescheduled Date": "2024-12-05"},
    {"Subject": "German", "Part": "II", "Original Date": "2024-11-30", "Rescheduled Date": "2024-12-07"},
    {"Subject": "Physics", "Part": "I", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-06"},
    {"Subject": "Physics", "Part": "II", "Original Date": "2024-12-02", "Rescheduled Date": "2024-12-09"},
    {"Subject": "Pali", "Part": "I", "Original Date": "2024-11-29", "Rescheduled Date": "2024-12-06"},
    {"Subject": "Pali", "Part": "II", "Original Date": "2024-12-02", "Rescheduled Date": "2024-12-09"},
    {"Subject": "Sinhala", "Part": "I", "Original Date": "2024-11-30", "Rescheduled Date": "2024-12-07"},
    {"Subject": "Sinhala", "Part": "II", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Tamil", "Part": "I", "Original Date": "2024-11-30", "Rescheduled Date": "2024-12-07"},
    {"Subject": "Tamil", "Part": "II", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Civil Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Civil Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Mechanical Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Mechanical Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Electrical, Electronic and Information Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Electrical, Electronic and Information Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Food Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Food Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Agro Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Agro Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Bio Resource Technology", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Bio Resource Technology", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Business Statistics", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Business Statistics", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Sanskrit", "Part": "I", "Original Date": "2024-12-03", "Rescheduled Date": "2024-12-10"},
    {"Subject": "Sanskrit", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Chemistry", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-11"},
    {"Subject": "Chemistry", "Part": "II", "Original Date": "2024-12-06", "Rescheduled Date": "2024-12-13"},
    {"Subject": "Science for Technology", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-11"},
    {"Subject": "Science for Technology", "Part": "II", "Original Date": "2024-12-06", "Rescheduled Date": "2024-12-13"},
    {"Subject": "Drama & Theatre (Sinhala)", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-11"},
    {"Subject": "Drama & Theatre (Sinhala)", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Drama & Theatre (Tamil)", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-11"},
    {"Subject": "Drama & Theatre (Tamil)", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Drama & Theatre (English)", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-11"},
    {"Subject": "Drama & Theatre (English)", "Part": "II", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "Political Science", "Part": "I", "Original Date": "2024-12-04", "Rescheduled Date": "2024-12-11"},
    {"Subject": "Political Science", "Part": "II", "Original Date": "2024-12-06", "Rescheduled Date": "2024-12-13"},
    {"Subject": "French", "Part": "I", "Original Date": "2024-12-05", "Rescheduled Date": "2024-12-12"},
    {"Subject": "French", "Part": "II", "Original Date": "2024-12-06", "Rescheduled Date": "2024-12-13"},
    {"Subject": "Common General Test", "Part": "", "Original Date": "2024-12-07", "Rescheduled Date": "2024-12-16"},
    {"Subject": "English", "Part": "I", "Original Date": "2024-12-07", "Rescheduled Date": "2024-12-16"},
    {"Subject": "English", "Part": "II", "Original Date": "2024-12-10", "Rescheduled Date": "2024-12-18"},
    {"Subject": "General English", "Part": "II", "Original Date": "2024-12-09", "Rescheduled Date": "2024-12-17"},
    {"Subject": "General English", "Part": "I", "Original Date": "2024-12-09", "Rescheduled Date": "2024-12-17"},
    {"Subject": "Home Economics", "Part": "I", "Original Date": "2024-12-10", "Rescheduled Date": "2024-12-18"},
    {"Subject": "Home Economics", "Part": "II", "Original Date": "2024-12-12", "Rescheduled Date": "2024-12-20"},
    {"Subject": "Accounting", "Part": "I", "Original Date": "2024-12-10", "Rescheduled Date": "2024-12-18"},
    {"Subject": "Accounting", "Part": "II", "Original Date": "2024-12-13", "Rescheduled Date": "2024-12-21"},
    {"Subject": "History", "Part": "II", "Original Date": "2024-12-11", "Rescheduled Date": "2024-12-19"},
    {"Subject": "History", "Part": "I", "Original Date": "2024-12-13", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Arabic", "Part": "I", "Original Date": "2024-12-11", "Rescheduled Date": "2024-12-19"},
    {"Subject": "Arabic", "Part": "II", "Original Date": "2024-12-13", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Malay", "Part": "I", "Original Date": "2024-12-11", "Rescheduled Date": "2024-12-19"},
    {"Subject": "Malay", "Part": "II", "Original Date": "2024-12-13", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Chinese", "Part": "I", "Original Date": "2024-12-11", "Rescheduled Date": "2024-12-19"},
    {"Subject": "Chinese", "Part": "II", "Original Date": "2024-12-13", "Rescheduled Date": "2024-12-21"},
    {"Subject": "Information & Communication Technology", "Part": "I", "Original Date": "2024-12-12", "Rescheduled Date": "2024-12-20"},
    {"Subject": "Information & Communication Technology", "Part": "II", "Original Date": "2024-12-16", "Rescheduled Date": "2024-12-23"},
    {"Subject": "Hindi", "Part": "I", "Original Date": "2024-12-16", "Rescheduled Date": "2024-12-23"},
    {"Subject": "Hindi", "Part": "II", "Original Date": "2024-12-19", "Rescheduled Date": "2024-12-30"},
    {"Subject": "Korean", "Part": "I", "Original Date": "2024-12-16", "Rescheduled Date": "2024-12-23"},
    {"Subject": "Korean", "Part": "II", "Original Date": "2024-12-19", "Rescheduled Date": "2024-12-30"},
    {"Subject": "Mathematics", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Mathematics", "Part": "II", "Original Date": "2024-12-18", "Rescheduled Date": "2024-12-28"},
    {"Subject": "Higher Mathematics", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Higher Mathematics", "Part": "II", "Original Date": "2024-12-20", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Geography", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Geography", "Part": "II", "Original Date": "2024-12-18", "Rescheduled Date": "2024-12-28"},
    {"Subject": "Greek and Roman Civilization", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Greek and Roman Civilization", "Part": "II", "Original Date": "2024-12-20", "Rescheduled Date": "2024-12-31"},
    {"Subject": "Russian", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Russian", "Part": "II", "Original Date": "2024-12-18", "Rescheduled Date": "2024-12-28"},
    {"Subject": "Japanese", "Part": "I", "Original Date": "2024-12-17", "Rescheduled Date": "2024-12-27"},
    {"Subject": "Japanese", "Part": "II", "Original Date": "2024-12-18", "Rescheduled Date": "2024-12-28"},
    {"Subject": "Communication & Media Studies", "Part": "I", "Original Date": "2024-12-19", "Rescheduled Date": "2024-12-30"},
    {"Subject": "Communication & Media Studies", "Part": "II", "Original Date": "2024-12-20", "Rescheduled Date": "2024-12-31"}
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

    fig.add_trace(go.Scatter(
        x=subject_data["Rescheduled Date"],
        y=[subject] * len(subject_data),
        mode="lines+markers",
        line=dict(color="blue"),
        marker=dict(size=8, symbol="square", color="blue"),
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
    title='An Alternative Rescheduling Method: A Collective One-Week Postponement',
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