import pandas as pd
file_path = 'D:/VAISH/MCA notes and materials/shadowfox/task3/ipl.xlsx'
data = pd.read_excel(file_path)
print("Column Names:", data.columns)  # Check column names
# Remove leading/trailing spaces in column names if necessary
data.columns = [col.strip() for col in data.columns]
# Check if necessary columns exist
required_columns = ['Pick', 'Clean Pick', 'Fumble', 'Catch', 'Dropped Catch',
                    'Stumping', 'Run Out', 'Missed Stumping', 'Missed Run Out', 'Direct Hit', 'Runs']
missing_columns = [col for col in required_columns if col not in data.columns]
if missing_columns:
    raise ValueError(f"Missing columns: {', '.join(missing_columns)}")
# Convert relevant columns to numeric, handling errors
numeric_columns = ['Clean Pick', 'Fumble', 'Catch', 'Dropped Catch', 'Stumping',
                   'Run Out', 'Missed Stumping', 'Missed Run Out', 'Direct Hit', 'Runs']
for col in numeric_columns:
    data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)
# Determine the fielding action
data['Pick'] = data[['Clean Pick', 'Fumble', 'Catch', 'Dropped Catch']].apply(
    lambda row: row.idxmax() if row.max() > 0 else 'None', axis=1)
data['Throw'] = data[['Run Out', 'Missed Stumping', 'Missed Run Out', 'Direct Hit']].apply(
    lambda row: row.idxmax() if row.max() > 0 else 'None', axis=1)
# Filter data for players of interest
players_of_interest = ['Player1', 'Player2', 'Player3']  # Replace with actual player names
filtered_data = data[data['Player Name'].isin(players_of_interest)]
# Define weights for the performance calculation
weights = {
    'Clean Pick': 1,
    'Good Throw': 1,
    'Catch': 2,
    'Dropped Catch': -2,
    'Stumping': 1,
    'Run Out': 3,
    'Missed Run Out': -1,
    'Direct Hit': 2,
    'Runs': 1,  # Positive for runs saved, negative for runs conceded
}
# Calculate performance score for each player
def calculate_performance_score(df):
    performance_scores = {}
    for player, group in df.groupby('Player Name'):
        counts = {action: 0 for action in weights.keys()}   
        for _, row in group.iterrows():
            pick = row['Pick']
            throw = row['Throw']
            runs = row['Runs']
            if pick in counts:
                counts[pick] += 1
            if throw in counts:
                counts[throw] += 1
            counts['Runs'] += runs
        performance_score = sum(counts[action] * weights[action] for action in weights)
        performance_scores[player] = performance_score
    return performance_scores
performance_scores = calculate_performance_score(filtered_data)
performance_df = pd.DataFrame(list(performance_scores.items()), columns=['Player Name', 'Performance Score'])
performance_df.to_csv('fielding_performance_scores.csv', index=False)
print(performance_df)
