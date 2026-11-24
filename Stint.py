import fastf1
import numpy as np
import pandas as pd

fastf1.Cache.enable_cache('cache')

session = fastf1.get_session(2023, 'Silverstone', 'R')
session.load(telemetry=False, weather=False, messages=False)

laps = session.laps
print("Total race laps:", laps['LapNumber'].max())

# keep only "clean" laps: not in/out laps, green flag only, within 107% of fastest
clean = laps.pick_wo_box()
clean = clean.pick_track_status('1', how='equals')
clean = clean.pick_quicklaps()

# lap time as plain seconds so we can do math on it later
clean = clean.copy()
clean['LapSeconds'] = clean['LapTime'].dt.total_seconds()

# one row per stint: who, which compound, how many clean laps, tyre age range
stints = clean.groupby(['Driver', 'Stint', 'Compound']).agg(
    cleanLaps=('LapNumber', 'count'),
    firstAge=('TyreLife', 'min'),
    lastAge=('TyreLife', 'max'),
    avgLap=('LapSeconds', 'mean'),
)
print(stints)

print()
print("Clean laps per compound:")
print(clean['Compound'].value_counts())

print(clean[['Driver', 'LapNumber', 'TyreLife', 'LapSeconds']].head(10))




print("-----------------------------------------------------------------------------------------------")
for KEY, PILE in clean.groupby(['Compound', 'TyreLife']):
    total = 0
    num = 0
    
    for t in PILE['LapSeconds']:
        total += t
        num += 1  
        
    print(KEY, total, num, total/num)
