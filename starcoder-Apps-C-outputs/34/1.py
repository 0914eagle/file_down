
import numpy as np

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            books = []
            for _ in range(n):
                books.append(list(map(int,input().split())))
            books = np.array(books)
            best = np.prod(books[:,1])
            for i in range(1,2**n):
                bins = [[] for _ in range(3)]
                for j in range(n):
                    if i & 1<<j:
                        bins[0].append(j)
                    else:
                        bins[1].append(j)
                if len(bins[0])==0 or len(bins[1])==0:
                    continue
                bins[2] = list(set(range(n))-set(bins[0])-set(bins[1]))
                if len(bins[2])==0:
                    continue
                best = min(best,np.prod((np.max(books[bins[0],0]),np.max(books[bins[1],0]),np.max(books[bins[2],0]))),
                            np.prod((np.max(books[bins[0],0]),np.max(books[bins[1],0]),np.max(books[bins[2],0]))))
            print(best)
        except:
            break
