def combination(candidates, target):
    candidates.sort()
    results = []

    def backtrack(start, current_comb, remains):
        if remains == 0:
            results.append(current_comb)
            return
        if remains < 0:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            backtrack(i + 1, current_comb + [candidates[i]], remains - candidates[i])

    backtrack(0, [], target)
    return results

candidates = [2, 5, 2, 1, 2]
target = 5
print(combination(candidates, target))
