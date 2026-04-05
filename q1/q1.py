import time
import sys
sys.path.append('../src')
from HVLCS import hvlcs, backtrack

times, lengths, results = [], [], []

for i in range(1, 11):
    lines = open(f"input{i}.in").read().split('\n')
    k = int(lines[0])
    val = {lines[j+1].split()[0]: int(lines[j+1].split()[1]) for j in range(k)}
    A, B = lines[k+1], lines[k+2]

    runs = []
    for _ in range(3):
        start = time.time()
        M = hvlcs(A, B, val)
        seq = backtrack(M, A, B)
        runs.append(time.time() - start)
    elapsed = sum(runs) / 3

    size = len(A) * len(B)
    results.append(f"File {i}: |A|={len(A)} |B|={len(B)} size={size}, value={M[len(A)][len(B)]}, seq={seq}, time={elapsed:.6f}s")
    print(results[-1])

with open("results.txt", 'w') as f:
    f.write("\n".join(results))