class TimeMap:

    def __init__(self):
        self.my_hash = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.my_hash:
            self.my_hash[key][0].append(value)
            self.my_hash[key][1].append(timestamp)
        else:
            self.my_hash[key] = [[value],[timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        values,timestamps = self.my_hash.get(key,[[],[]])
        if values == []:
            return ""
        
        l,r = 0,len(timestamps)-1
        while l<=r:
            m = (l+r)//2
            if timestamps[m] == timestamp:
                return values[m]
            elif timestamps[m] < timestamp:
                l = m+1
            else:
                r = m-1
        return values[r] if r>=0 else ""

