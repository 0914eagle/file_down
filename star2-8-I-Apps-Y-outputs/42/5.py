
def count_vote(candidate_dict, candidate_list, majority):
    for candidate in candidate_list:
        if candidate in candidate_dict:
            candidate_dict[candidate] += 1
        else:
            candidate_dict[candidate] = 1
    
    for candidate, votes in candidate_dict.items():
        if votes > majority:
            return candidate
    
    return "Runoff!"

candidate_list = []
while True:
    line = input()
    if line == "***":
        break
    candidate_list.append(line)

candidate_dict = {}
majority = len(candidate_list) // 2
result = count_vote(candidate_dict, candidate_list, majority)
print(result)

