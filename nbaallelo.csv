import streamlit as st
from filters import load_and_clean_data, apply_filters
from charts import create_charts

# Page Settings
st.set_page_config(page_title="NBA Analytics Dashboard", layout="wide")

st.title("🏀 NBA Historical Data Analytics Dashboard")
st.markdown("This dashboard leverages advanced visuals to explore over 126,000 historical NBA games, tracking trends, Elo metrics, and scoring outputs.")

# Load Data
try:
    df = load_and_clean_data("data/nbaallelo.csv")
except Exception as e:
    st.error(f"Error loading file. Make sure the dataset is placed inside the 'data/' directory. Details: {e}")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Interactive Dashboard Filters")

# Year Range Slider
min_year, max_year = int(df['year_id'].min()), int(df['year_id'].max())
selected_years = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Multi-select Franchises
all_frans = sorted(df['fran_id'].unique().tolist())
selected_frans = st.sidebar.multiselect("Select Teams/Franchises", all_frans)

# Numerical Range Slider for Points
min_p, max_p = int(df['pts'].min()), int(df['pts'].max())
selected_pts = st.sidebar.slider("Points Scored Range", min_p, max_p, (min_p, max_p))

# Dropdown Category Filter
game_loc = st.sidebar.selectbox("Game Location", ["All", "Home", "Away", "Neutral"])

# Text Search Filter
search_term = st.sidebar.text_input("Search Game Notes (Keyword)")

# Reset Logic Indicator
if st.sidebar.button("Reset All Filters"):
    st.rerun()

# Apply Filters
filtered_df = apply_filters(df, selected_years, selected_frans, selected_pts[0], selected_pts[1], game_loc, search_term)

# --- KPI CARDS ---
st.markdown("### 📊 Key Performance Indicators (KPIs)")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric(label="Total Records Filtered", value=f"{len(filtered_df):,}")
with kpi2:
    avg_pts = filtered_df['pts'].mean() if not filtered_df.empty else 0
    st.metric(label="Average Points Scored", value=f"{avg_pts:.2f}")
with kpi3:
    max_elo = filtered_df['elo_i'].max() if not filtered_df.empty else 0
    st.metric(label="Highest Initial ELO Rating", value=f"{max_elo:,.1f}")
with kpi4:
    win_pct = (filtered_df['game_result'] == 'W').sum() / len(filtered_df) * 100 if not filtered_df.empty else 0
    st.metric(label="Selected Match Win %", value=f"{win_pct:.1f}%")

st.markdown("---")

# --- DRAW VISUALIZATIONS ---
if filtered_df.empty:
    st.warning("No data found for the current filter settings. Try relaxing your sidebar filters.")
else:
    plots = create_charts(filtered_df)
    
    # Layout Sections
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(plots['pie'])
        st.pyplot(plots['line'])
        st.pyplot(plots['scatter'])
        st.pyplot(plots['heatmap'])
        st.pyplot(plots['count'])
    with col2:
        st.pyplot(plots['hist'])
        st.pyplot(plots['bar'])
        st.pyplot(plots['box'])
        st.pyplot(plots['area'])
        st.pyplot(plots['violin'])