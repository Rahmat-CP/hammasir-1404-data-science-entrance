candidates = list(map(int, input().split()))
target = int(input())

candidates.sort()

results = []


def find_combination(start, remining, current_path):
    if remining == 0:
        results.append(list(current_path))
        return
    
    if remining < 0:
        return
    
    for i in range(start, len(candidates)):
        if start < i and candidates[i - 1] == candidates[i]:
            continue
        
        if candidates[i] > remining:
            break
        
        current_path.append(candidates[i])
        find_combination(i + 1, remining - candidates[i], current_path)
        current_path.pop()
        
find_combination(0, target, [])

if not results:
    print(0)
else:
    for combination in results:
        print(*combination)