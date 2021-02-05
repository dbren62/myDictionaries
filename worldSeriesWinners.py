start = 1903
titles = {}
yearWon = {}

input_file = open("WorldSeriesWinners.txt", "r")

winners = input_file.readlines()

list = [
    "Boston Americans",
    "New York Giants",
    "Chicago White Sox",
    "Chicago Cubs",
    "Chicago Cubs",
    "Pittsburgh Pirates",
    "Philadelphia Athletics",
    "Philadelphia Athletics",
    "Boston Red Sox",
    "Philadelphia Athletics",
    "Boston Braves",
    "Boston Red Sox",
    "Boston Red Sox",
    "Chicago White Sox",
    "Boston Red Sox",
    "Cincinnati Reds",
    "Cleveland Indians",
    "New York Giants",
    "New York Giants",
    "New York Yankees",
    "Washington Senators",
    "Pittsburgh Pirates",
    "St. Louis Cardinals",
    "New York Yankees",
    "New York Yankees",
    "Philadelphia Athletics",
    "Philadelphia Athletics",
    "St. Louis Cardinals",
    "New York Yankees",
    "New York Giants",
    "St. Louis Cardinals",
    "Detroit Tigers",
    "New York Yankees",
    "New York Yankees",
    "New York Yankees",
    "New York Yankees",
    "Cincinnati Reds",
    "New York Yankees",
    "St. Louis Cardinals",
    "New York Yankees",
    "St. Louis Cardinals",
    "Detroit Tigers",
    "St. Louis Cardinals",
    "New York Yankees",
    "Cleveland Indians",
    "New York Yankees",
    "New York Yankees",
    "New York Yankees",
    "New York Yankees",
    "New York Yankees",
    "New York Giants",
    "Brooklyn Dodgers",
    "New York Yankees",
    "Milwaukee Braves",
    "New York Yankees",
    "Los Angeles Dodgers",
    "Pittsburgh Pirates",
    "New York Yankees",
    "New York Yankees",
    "Los Angeles Dodgers",
    "St. Louis Cardinals",
    "Los Angeles Dodgers",
    "Baltimore Orioles",
    "St. Louis Cardinals",
    "Detroit Tigers",
    "New York Mets",
    "Baltimore Orioles",
    "Pittsburgh Pirates",
    "Oakland Athletics",
    "Oakland Athletics",
    "Oakland Athletics",
    "Cincinnati Reds",
    "Cincinnati Reds",
    "New York Yankees",
    "New York Yankees",
    "Pittsburgh Pirates",
    "Philadelphia Phillies",
    "Los Angeles Dodgers",
    "St. Louis Cardinals",
    "Baltimore Orioles",
    "Detroit Tigers",
    "Kansas City Royals",
    "New York Mets",
    "Minnesota Twins",
    "Los Angeles Dodgers",
    "Oakland Athletics",
    "Cincinnati Reds",
    "Minnesota Twins",
    "Toronto Blue Jays",
    "Toronto Blue Jays",
    "Atlanta Braves",
    "New York Yankees",
    "Florida Marlins",
    "New York Yankees",
    "New York Yankees",
    "New York Yankees",
    "Arizona Diamondbacks",
    "Anaheim Angels",
    "Florida Marlins",
    "Boston Red Sox",
    "Chicago White Sox",
    "St. Louis Cardinals",
    "Boston Red Sox",
    "Philadelphia Phillies",
]


for team in list:
    if team in titles:
        titles[team] += 1
    else:
        titles[team] = 1

print(f"TEAM           WINS")

for team, wins in sorted(titles.items()):
    print(f"{team}: {wins}")

for i in range(len(winners)):
    team = winners[i].rstrip("\n")
    year = start + i
    if year >= 1904:
        year += 1
    if year >= 1994:
        year += 1
    yearWon[str(year)] = team
    if team in titles:
        titles[team] += 1
    else:
        titles[team] = 1

while True:
    year = int(input("Enter year between 1903-2008 (excluding 1904 and 1994): "))
    if year == 1904:
        print("There was no World Series that year")
    elif year == 1994:
        print("There was no World Series that year")
    elif year < 1903 or year > 2008:
        print("The winner of that World Series if unknown")
    else:
        winner = yearWon[str(year)]
        wins = titles[str(winner)]
        print("The", winner, "won the World Series in", year)
        print("The", winner, "won the World Series", wins, "times")