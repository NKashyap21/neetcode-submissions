class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPosSpd = [[position[i],speed[i]] for i in range(len(position))]
        carPosSpd.sort(key = lambda x: x[0])
        car_pos_spd = carPosSpd[::-1]

        stack = []
        for carStat in car_pos_spd:
            pos,spd = carStat[0],carStat[1]
            timeTarget = (target-pos)/spd

            if not stack or timeTarget > stack[-1]:
                stack.append(timeTarget)
        return len(stack)