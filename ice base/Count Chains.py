# https://py.checkio.org/en/mission/count-chains/

from typing import List, Tuple
import numpy as np
import math


def count_chains(circles: List):
    circles.sort(key = lambda x: x[0])

    def get_distances(c1, c2):
        p1 = np.array(c1[:2])
        p2 = np.array(c2[:2])
        p3 = p2 - p1
        p4 = math.hypot(p3[0], p3[1])
        R0 = abs(c1[-1] - c2[-1])
        R1 = c1[-1] +c2[-1]
        return True if R0 < p4 < R1 else False

    Ncircles = []
    for i in range(len(circles)-1):
        for j in range(i + 1,len(circles)):
            a, b = -1, -1
            for N in Ncircles:
                if circles[i] in N:
                    a = Ncircles.index(N)
            for N in Ncircles:
                if circles[j] in N:
                    b = Ncircles.index(N)

            if not get_distances(circles[i], circles[j]):
                if a == b == -1:
                    Ncircles.append([circles[i]])
                    Ncircles.append([circles[j]])
                elif a != -1 and b == -1:
                    Ncircles.append([circles[j]])
                elif a == -1 and b != -1:
                    Ncircles.append([circles[i]])

            if get_distances(circles[i], circles[j]):
                if a == b == -1:
                    Ncircles.append([circles[i],circles[j]])
                elif a != -1 and b == -1:
                    Ncircles[a].append(circles[j])
                elif a == -1 and b != -1:
                    Ncircles[b].append(circles[i])
                elif a != -1 and b != -1 and a != b:
                    Ncircles[a].extend(Ncircles.pop(b))

    return len(Ncircles)
