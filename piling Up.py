from collections import deque

def check_piling(cubes):
    pile_1 = deque()
    pile_2 = deque()

    while cubes:
        # Choose the larger side from the front or back of the remaining cubes
        if cubes[0] >= cubes[-1]:
            side = cubes.popleft()
        else:
            side = cubes.pop()

        # Check if the current side can be added to either pile
        if pile_1 and side > pile_1[-1]:
            return "No"
        elif pile_2 and side > pile_2[-1]:
            return "No"

        # Add the current side to the appropriate pile
        if not pile_1 or side <= pile_1[-1]:
            pile_1.append(side)
        elif not pile_2 or side <= pile_2[-1]:
            pile_2.append(side)

    # If all cubes are successfully added to the piles, return "Yes"
    return "Yes"

for i in range(int(input())):
    length = int(input())
    cubes = deque(map(int, input().split()))
    result = check_piling(cubes)
    print(result)