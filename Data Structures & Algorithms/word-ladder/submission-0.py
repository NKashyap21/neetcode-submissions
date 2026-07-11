class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        D = defaultdict(list)
        
        def differs_by_one(w1, w2):
            if len(w1) != len(w2):
                return False
            diff = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                if differs_by_one(wordList[i],wordList[j]):
                    D[wordList[i]].append(wordList[j])
                    D[wordList[j]].append(wordList[i])

        seen = set()
        q = deque()
        seen.add(beginWord)
        q.append((beginWord,0))
        while q:
            for _ in range(len(q)):
                word , level = q.popleft()
                for ne in D[word]:
                    if ne in seen:
                        continue
                    if ne == endWord:
                        return level +2
                    seen.add(ne)
                    q.append((ne,level+1))
        
        return 0
