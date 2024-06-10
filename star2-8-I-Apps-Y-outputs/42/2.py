
def majority_vote(vote_list):
    votes = {}
    for vote in vote_list:
        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1

    max_votes = max(votes.values())
    if max_votes > len(vote_list) / 2:
        return max(votes, key=lambda k: votes[k])
    else:
        return "Runoff!"

def main():
    vote_list = []
    while True:
        vote = input()
        if vote == "***":
            break
        vote_list.append(vote)

    result = majority_vote(vote_list)
    print(result)

if __name__ == "__main__":
    main()

