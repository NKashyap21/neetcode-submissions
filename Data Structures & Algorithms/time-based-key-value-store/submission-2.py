class TimeMap:

    def __init__(self):
        self.myHash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.myHash:
            self.myHash[key][0].append(value) #value
            self.myHash[key][1].append(timestamp) #timestamp
        else:
            self.myHash[key] = [[value],[timestamp]]
    
    def get(self, key: str, timestamp: int) -> str:
        values,timestamps = self.myHash.get(key,[[],[]])
        if len(timestamps) == 0:
            return ""
        l,r = 0,len(timestamps)-1
        while l <= r:
            m = (l+r)//2
            if timestamps[m] == timestamp:
                return values[m]
            elif timestamps[m] < timestamp:
                l = m+1
            else:
                r = m-1
        return values[r] if r >= 0 else ""
        

        
