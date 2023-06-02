competitions = [
    ["A","B"],
    ["B","C"],
    ["C","A"]
]
results = [0,0,1]

def tournamentWin(competitions,results):
    currentBestTeam = ""
    scores = {currentBestTeam:0}
    for idx,team in enumerate(competitions):
        result = results[idx]
        tA,tB = team
        winningTeam = tA if result==1 else tB
        setScore(winningTeam,3,scores)
        if scores[winningTeam]>scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam

def setScore(team,points,score):
    if team not in score:
        score[team] = 0
    score[team] += points

print(tournamentWin(competitions,results))