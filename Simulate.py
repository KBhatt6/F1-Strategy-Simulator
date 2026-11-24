import fastf1

def total_time(base, wear, numLaps):  # NOT NEEDED - first draft, no pit stops, superseded by race_time
                total = 0
                for laps in range(1, numLaps + 1):
                    total += base + wear * laps
                return total

        #print(total_time(90, 0.05, 10))

tyres = {  # NEEDED - real data used by race_time and best_one_stop_strategy
        "SOFT": {"base": 89, "wear": 0.10},
        "MEDIUM": {"base": 90, "wear": 0.05},
        "HARD": {"base": 91, "wear": 0.03},
        "INTERS": {"base": 88, "wear": 0.15},
        "WETS": {"base": 87, "wear": 0.20}
    }

def total_time_with_pitstops(base, wear, numLaps, pitLap, pitlossTime):  # NOT NEEDED - single-compound-only version, superseded by race_time
            total = 0
            tyreAge = 0
            for laps in range(1, numLaps+1):
                tyreAge += 1
                total += base + wear *tyreAge 
                if laps == pitLap:
                    total += pitlossTime
                    tyreAge = 0
            return total

results = []  # NOT NEEDED - exploration using the function above, never used afterward
for pit_lap in range(2, 10):
        t = total_time_with_pitstops(90, 0.05, 10, pit_lap, 5)
        results.append(t)
    #print(results)

    #print(total_time_with_pitstops(90, 0.05, 10, 3, 5))

def total_time_two_compounds(base1, wear1, laps1, base2, wear2, laps2, pitlossTime):  # NOT NEEDED - one-stop-only, two-compound version, superseded by race_time
            total = 0
            tyreAge = 0
            for laps in range(1, laps1 + 1):
                tyreAge += 1
                total += base1 + wear1 * tyreAge
            tyreAge = 0
            total += pitlossTime
            for laps in range(1, laps2 + 1):
                tyreAge += 1
                total += base2 + wear2 * tyreAge
            return total
        
results_with_two_compounds = []  # NOT NEEDED - exploration using the function above, never used afterward
for laps1 in range(1, 10):
        laps2 = 10 - laps1
        t = total_time_two_compounds(tyres["HARD"]["base"], tyres["HARD"]["wear"], laps1, tyres["MEDIUM"]["base"], tyres["MEDIUM"]["wear"], laps2, 5)
        results_with_two_compounds.append(t)
print(results_with_two_compounds)  # NOT NEEDED - prints exploration output above

stops = []  # NOT NEEDED RIGHT NOW - manual input flow; will matter again once the LLM/website layer replaces it, but blocks testing best_one_stop_strategy in the meantime
while True:
        compound = input("Enter your next compound (press X to finish): ")
        if compound.upper() == "X":
            break
        lap = int(input("Enter the lap number for this pit stop: "))
        stops.append((lap, compound))

def race_time(startCompound, stops, numLaps, pitlossTime):  # NEEDED - this is the real engine, used by best_one_stop_strategy
        total = 0 
        tyreAge = 0
        compound = startCompound
        stop_index = 0

        for lap in range(1, numLaps + 1):
            tyreAge += 1
            total += tyres[compound]["base"] + tyres[compound]["wear"] * tyreAge

            if stop_index < len(stops) and lap == stops[stop_index][0]:
                total += pitlossTime
                compound = stops[stop_index][1]
                tyreAge = 0
                stop_index += 1

        return total

print(race_time("MEDIUM", stops, 10, 5))  # NOT NEEDED - leftover manual test call, hardcoded numLaps=10 that conflicts with numLaps=7 below


numLaps = 7  # NEEDED - but will eventually come from real track data (Stage 1/2), not a hardcoded guess
pitLossTime = 20  # NEEDED - same as above
def best_one_stop_strategy(numLaps, pitlossTime):  # NEEDED - the actual search you're building toward
    dry_tyres = ["SOFT", "MEDIUM", "HARD"]
    best_time = None
    best_pit_lap = None
    best_start = None
    best_end = None

    for pitLap in range(2, numLaps):
        for start in dry_tyres:
            for end in dry_tyres:
                if start != end:
                    t = race_time(start, [(pitLap, end)], numLaps, pitlossTime)
                    if best_time is None or t < best_time:
                        best_time = t
                        best_pit_lap = pitLap
                        best_start = start
                        best_end = end

    return best_time, best_pit_lap, best_start, best_end


print(best_one_stop_strategy(numLaps, pitLossTime))  # NEEDED