class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1st car-> pos 1->3mi/hr, 2nd car->pos 4-> 2mi/hr
        pair =[[p,s] for p,s in zip(position, speed)]
        stack =[]
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<= stack[-2]:
                stack.pop()
        return len(stack)



        