from collections import defaultdict
def tally(rows):
    score = defaultdict(lambda: {
        "mp": 0,
        "w": 0,
        "l": 0,
        "d": 0,
        "p": 0
    })
    
    for row in rows:
        t1, t2, result = row.split(";")
        # a loss is the other teams win, switching reduces code
        if result == "loss": t1, t2, result = t2, t1, "win"

        score[t1]["mp"] += 1
        score[t2]["mp"] += 1

        if result == "win":
            score[t1]["w"] += 1
            score[t1]["p"] += 3
            score[t2]["l"] += 1

        if result == "draw":
            score[t1]["d"] += 1
            score[t2]["d"] += 1
            score[t1]["p"] += 1
            score[t2]["p"] += 1
    
    tbl = ["Team                           | MP |  W |  D |  L |  P"]
    # we make the score negitive, as to reverse the sort order of the score
    for team in sorted(score, key=lambda x: (0-score[x]['p'], x)):
        tbl.append(f"{team: <31}|  "
                   f"{score[team]['mp']} |  "
                   f"{score[team]['w']} |  "
                   f"{score[team]['d']} |  "
                   f"{score[team]['l']} |  "
                   f"{score[team]['p']}"
        )
    return tbl


