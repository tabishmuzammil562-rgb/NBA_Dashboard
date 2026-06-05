import matplotlib.pyplot as plt
import seaborn as sns

def create_charts(df):
    # Set style layout
    sns.set_theme(style="whitegrid")
    plots = {}

    # 1. Pie Chart - Game Results Distribution
    fig, ax = plt.subplots(figsize=(5, 4))
    df['game_result'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#2b5c8f', '#d95f02'], ax=ax, startangle=90)
    ax.set_title("Win/Loss Distribution")
    ax.set_ylabel("")
    plots['pie'] = fig

    # 2. Histogram - Points Scored Frequency
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df['pts'], bins=20, kde=True, color='#1f77b4', ax=ax)
    ax.set_title("Distribution of Team Points")
    ax.set_xlabel("Points")
    plots['hist'] = fig

    # 3. Line Chart - Average Elo Trend Over Years
    fig, ax = plt.subplots(figsize=(7, 4))
    trend = df.groupby('year_id')['elo_i'].mean().reset_index()
    sns.lineplot(data=trend, x='year_id', y='elo_i', color='#2ca02c', linewidth=2, ax=ax)
    ax.set_title("Average Team ELO Trend Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Initial ELO")
    plots['line'] = fig

    # 4. Bar Chart - Top 10 Scoring Franchises
    fig, ax = plt.subplots(figsize=(7, 4))
    top_teams = df.groupby('fran_id')['pts'].mean().sort_values(ascending=False).head(10).reset_index()
    sns.barplot(data=top_teams, x='pts', y='fran_id', palette="Blues_r", ax=ax)
    ax.set_title("Top 10 Highest Average Scoring Franchises")
    ax.set_xlabel("Avg Points")
    plots['bar'] = fig

    # 5. Scatter Plot - Points vs Opponent Points
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=df.sample(min(len(df), 1000)), x='pts', y='opp_pts', alpha=0.4, color='#9467bd', ax=ax)
    ax.set_title("Team Points vs Opponent Points (Sampleed)")
    ax.set_xlabel("Team Points")
    ax.set_ylabel("Opponent Points")
    plots['scatter'] = fig

    # 6. Box Plot - Point Spread by Game Location
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=df, x='game_location', y='pts', palette="Set2", ax=ax)
    ax.set_title("Points Spread by Location (Home/Away/Neutral)")
    ax.set_xlabel("Location")
    plots['box'] = fig

    # 7. Heatmap - Feature Correlations
    fig, ax = plt.subplots(figsize=(6, 4))
    corr = df[['pts', 'elo_i', 'elo_n', 'opp_pts', 'forecast']].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5, ax=ax)
    ax.set_title("Correlation Matrix")
    plots['heatmap'] = fig

    # 8. Area Chart - Cumulative Games Played over Years
    fig, ax = plt.subplots(figsize=(7, 4))
    games_per_year = df.groupby('year_id')['game_id'].count().cumsum()
    games_per_year.plot.area(color='#ff7f0e', alpha=0.6, ax=ax)
    ax.set_title("Cumulative Growth of Total NBA Games Recorded")
    ax.set_xlabel("Year")
    ax.set_ylabel("Cumulative Count")
    plots['area'] = fig

    # 9. Count Plot - Playoff vs Regular Season Games
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.countplot(data=df, x='is_playoffs', palette="Pastel1", ax=ax)
    ax.set_title("Game Type Frequency")
    ax.set_xticklabels(['Regular Season', 'Playoffs'])
    ax.set_xlabel("")
    plots['count'] = fig

    # 10. Violin Plot - Forecast Probability by Win/Loss Result
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.violinplot(data=df, x='game_result', y='forecast', palette="muted", ax=ax)
    ax.set_title("Win Probability Forecast Density")
    ax.set_xlabel("Result")
    ax.set_ylabel("Forecast Value")
    plots['violin'] = fig

    return plots