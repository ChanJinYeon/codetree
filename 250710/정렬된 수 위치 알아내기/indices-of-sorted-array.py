n = int(input())
sequence = list(map(int, input().split()))

mapping = [ (idx, num) for idx, num in enumerate(sequence, start=1) ]
mapping.sort(key=lambda x: x[1])
new_mapping = [ (tup, idx) for idx, tup in enumerate(mapping, start=1)]
new_mapping.sort(key=lambda x: x[0][0])

for num in new_mapping:
    print(num[1], end=' ')