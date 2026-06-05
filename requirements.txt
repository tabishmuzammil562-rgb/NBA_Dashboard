import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    # Convert date to datetime object
    df['date_game'] = pd.to_datetime(df['date_game'])
    # Handle missing notes column
    df['notes'] = df['notes'].fillna('No Notes')
    return df

def apply_filters(df, selected_years, selected_frans, min_pts, max_pts, game_loc, search_term):
    # Year Filter
    filtered_df = df[(df['year_id'] >= selected_years[0]) & (df['year_id'] <= selected_years[1])]
    
    # Team/Franchise Filter
    if selected_frans:
        filtered_df = filtered_df[filtered_df['fran_id'].isin(selected_frans)]
        
    # Points Range Filter
    filtered_df = filtered_df[(filtered_df['pts'] >= min_pts) & (filtered_df['pts'] <= max_pts)]
    
    # Game Location Filter
    if game_loc != "All":
        loc_code = 'H' if game_loc == "Home" else ('A' if game_loc == "Away" else 'N')
        filtered_df = filtered_df[filtered_df['game_location'] == loc_code]
        
    # Search/Text Filter (Notes keyword lookup)
    if search_term:
        filtered_df = filtered_df[filtered_df['notes'].str.contains(search_term, case=False)]
        
    return filtered_df