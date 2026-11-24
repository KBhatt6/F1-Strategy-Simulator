import fastf1

print("it worked")


fastf1.Cache.enable_cache('cache')  # Enable caching to speed up data retrieval

session = fastf1.get_session(2023, 'Monaco', 'R')  # Get the session data for the 2023 Monaco Grand Prix qualifying
session.load()  # Load the session data

laps = session.laps  # Get the laps data from the session

#print(laps.columns)
#print(laps[['Driver', 'LapNumber', 'LapTime', 'Compound', 'TyreLife']])  # Print the driver, lap time, and compound used for each lap

ver_laps = laps[laps['Driver'] == 'HAM']
print(ver_laps[['LapNumber', 'LapTime', 'Compound', 'TyreLife']])