class Cluster:
    def __init__(self, persons):
        self.cluster = []
        self.persons = persons

    def union(self, s1, s2):
        pass

    def get_level(self, s):
        pass


def main():
    n, m, q = [int(x) for x in input().split()]
    persons = {}
    for _ in range(n):
        s, v = input().split()
        persons[s] = int(v)

    sensates = set()
    cluster = Cluster(persons)
    for _ in range(m):
        s1, s2 = input().split()
        sensates.add(s1)
        sensates.add(s2)
        cluster.union(s1, s2)

    for _ in range(q):
        t = input()
        if t not in sensates or cluster.get_level(t) < 5 or persons[t] >= 5:
            print("S")
        else:
            print("N")


if __name__ == '__main__':
    main()