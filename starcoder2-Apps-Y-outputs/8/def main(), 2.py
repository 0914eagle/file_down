
import sys

def main():
    # Read in the input
    R, C = map(int, sys.stdin.readline().split())
    crossword = []
    for i in range(R):
        crossword.append(sys.stdin.readline().strip())

    # Find the smallest word
    smallest = ""
    for i in range(R):
        for j in range(C):
            # Check for horizontal words
            if j + 1 < C and crossword[i][j] != "#" and crossword[i][j + 1] != "#":
                word = crossword[i][j] + crossword[i][j + 1]
                if smallest == "" or word < smallest:
                    smallest = word
            # Check for vertical words
            if i + 1 < R and crossword[i][j] != "#" and crossword[i + 1][j] != "#":
                word = crossword[i][j] + crossword[i + 1][j]
                if smallest == "" or word < smallest:
                    smallest = word

    # Print the smallest word
    print(smallest)

if __name__ == "__main__":
    main()

