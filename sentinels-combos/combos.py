# SPDX-License-Identifier: Apache-2.0

heroes = {
        "Absolute Zero": 4,
        "Bunker": 5,
        "Fanatic": 4,
        "Haka": 4,
        "Legacy": 4,
        "Ra": 3,
        "Tachyon": 4,
        "Tempest": 4,
        "Visionary": 3,
        "Wraith": 4,
        "Unity": 3,
        "Expatriette": 2,
        "Mister Fixer": 2,
        "Argent Adept": 4,
        "Nightmist": 2,
        "Scholar": 2,
        "Chrono-Ranger": 2,
        "Omnitron-X": 2,
        "Captain Cosmic": 4,
        "Sky-Scraper": 2,
        "Guise": 3,
        "K.N.Y.F.E.": 2,
        "Naturalist": 2,
        "Parse": 2,
        "Sentinels": 2,
        "Setback": 2,
        "Benchmark": 2,
        "Stuntman": 2,
        "Doctor Medico": 2,
        "Idealist": 2,
        "Mainstay": 2,
        "Writhe": 2,
        "Akash'thriya": 2,
        "La Comodora": 2,
        "Harpy": 2,
        "Lifeline": 2,
        "Luminary": 2,
    }

# smaller set for testing
#heroes = {
#        "Unity": 3,
#        "Mainstay": 2,
#        "Writhe": 2,
#        "Akash'thriya": 2,
#        "La Comodora": 2,
#        "Harpy": 2,
#        "Lifeline": 2,
#        "Luminary": 2,
#    }

def make_hero_variants():
    variants = []
    for hero, numvars in heroes.items():
        for i in range(0, numvars):
            v = (hero, i)
            variants.append(v)
    variants.sort(key=lambda tup: tup[0])
    return variants

def is_all_unique(team):
    heroes = set()
    for hero in team:
        heroes.add(hero[0])
    return len(heroes) == len(team)

def make_team_combos_size_3(variants):
    print("Counting teams of size 3...")
    num_teams = 0
    numvars = len(variants)
    for x in range(0, numvars-1):
        for y in range(x+1, numvars-1):
            for z in range(y+1, numvars-1):
                team = (variants[x], variants[y], variants[z])
                if is_all_unique(team):
                    num_teams += 1
    return num_teams

def make_team_combos_size_4(variants):
    print("Counting teams of size 4...")
    num_teams = 0
    numvars = len(variants)
    for x in range(0, numvars-1):
        for y in range(x+1, numvars-1):
            for z in range(y+1, numvars-1):
                for a in range(z+1, numvars-1):
                    team = (variants[x], variants[y], variants[z], variants[a])
                    if is_all_unique(team):
                        num_teams += 1
    return num_teams

def make_team_combos_size_5(variants):
    print("Counting teams of size 5...")
    num_teams = 0
    numvars = len(variants)
    for x in range(0, numvars-1):
        for y in range(x+1, numvars-1):
            for z in range(y+1, numvars-1):
                for a in range(z+1, numvars-1):
                    for b in range(a+1, numvars-1):
                        team = (variants[x], variants[y], variants[z], variants[a], variants[b])
                        if is_all_unique(team):
                            num_teams += 1
    return num_teams

if __name__ == "__main__":
    variants = make_hero_variants()
    numteams3 = make_team_combos_size_3(variants)
    numteams4 = make_team_combos_size_4(variants)
    numteams5 = make_team_combos_size_5(variants)
    print(f"# of teams size 3: {numteams3}")
    print(f"# of teams size 4: {numteams4}")
    print(f"# of teams size 5: {numteams5}")

