class Solution:
    def findWinners(self, matches):

        group1 = []
        group2 = []
        matchDict = {}

        for players in matches:
            matchDict[players[0]] = 0
            matchDict[players[1]] = 0
        for players in matches:
            matchDict[players[1]] += 1
        for losses in matchDict:
            if matchDict[losses] == 0:
                group1.append(losses)
            elif matchDict[losses] == 1:
                group2.append(losses)
        return([sorted(group1), sorted(group2)])

