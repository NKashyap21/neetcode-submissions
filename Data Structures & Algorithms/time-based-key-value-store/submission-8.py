class TimeMap:

    def __init__(self):
        self.store = {} #key -> [[val],[time]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            val,time = self.store[key]
            val.append(value)
            time.append(timestamp)
        else:
            self.store[key] = [[value],[timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        
        val,time = self.store.get(key,[[],[]])
        if not val:
            return ""
        
        l,r = 0,len(time)-1
        while l <= r:
            m = (l+r)//2
            if time[m] == timestamp:
                return val[m]
            elif time[m] > timestamp:
                r = m - 1
            else:
                l = m+1
        return val[r] if r >= 0 else ""