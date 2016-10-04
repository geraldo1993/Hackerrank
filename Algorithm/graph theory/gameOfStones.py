

numberOfTestCases = int(raw_input())
op = []
for i in range(numberOfTestCases):
    availableStones = int(raw_input())
    result = [availableStones % 7 in [0, 1]]
    if result is None:
        pass
    elif result == [True]:
        op.append("Second")
    else:
        op.append("First")
for i in op:
    print i
