class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        party = list(senate)
        n = len(party)
        bans = [1]*n    # 1- notBan, 0- Ban
        d_count = 0
        r_count = 0
        for r in party:
            if r == "R":
                r_count += 1
            else:
                d_count += 1
        curr = 0
        nxt = 1
        while d_count != 0 and r_count != 0:
            if bans[curr] == 0:
                curr += 1
                if curr >= n:
                    curr = curr %n
            if party[nxt] == party[curr] or bans[nxt] == 0:
                nxt += 1
                if nxt >= n:
                    nxt = nxt % n
            else:
                bans[nxt] = 0
                if party[nxt] == "R":
                    r_count -= 1
                else:
                    d_count -= 1
                curr += 1
                nxt = curr + 1
                if curr >= n:
                    curr = curr % n
                if nxt >= n:
                    nxt = nxt % n
        if d_count == 0:
            return "Radiant"
        else:
            return "Dire"
            
