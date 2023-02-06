import os
path = os.chdir("../AI/COG_ICT/data")

# # ===== 두 문서의 유사도 분석 =====

# # == 내가 짠 코드 ==
# import os
# path = os.chdir("../AI/COG_ICT/data")

# files = []
# for idx in range(2):
#     filename = input(f"파일{idx}의 이름을 입력하시오: ").strip()
#     files.append(open(filename + ".txt", "r"))

# f_list = [[] for _ in range(2)]
# for file in files:
#     num = 0
#     for line in file:
#         for word in line.split():
#             f_list[num].append(word)
#     num += 1

# cnt = 0
# group_word = []
# for f in f_list:
#     for word in range(0, len(f)-4):
#         group = []
#         for idx in range(5):
#             group.append(f[idx])    
#         group_word.append(set(group))

# # print(group_word)
# # print(group_word[0] & group_word[1])
# print(group_word[0] | group_word[1])

# similarity = (len(group_word[0] & group_word[1])) / len((group_word[0] | group_word[1]))
# print(similarity)
# # ==

# # == 교수님 코드 ==

# def make_shingle_set(fname, k):
#     file = open(fname, "r")
#     wlist = file.read().split()
#     shingle_set = set()



# fname1, fname2 = input("두 개의 파일 이름: ").split()
# k = int(input("Shingle의 크기? "))

# set1 = make_shingle_set(fname1, k)
# set2 = make_shingle_set(fname2, k)
# print(f"유사도 = {len(set1 & set2) / len(set1 | set2)}")

# # ==


# # ===== 장바구니 분석 =====

# # == 내 코드 == 
# import os
# path = os.chdir("../AI/COG_ICT/data")

# # filename, reliability, choice = input("파일 이름, 신뢰도, 지지도를 입력하세요: ").split()

# # def make_list(fname):
# #     file = open(fname + ".txt", "r")

# #     L = []
# #     for line in file:
# #         input = line.split()
# #         input_list = [int(input[x+2]) for x in range(0, int(input[1]))]
# #         L.append({int(input[0]) : input_list})
# #     return L

# # print(make_list(filename))

# # ==

# # == 교수님 코드 ==
# # 지지도 = (a,b를 같이 산 바구니의 수) / (전체 바구니의 수)
# # 신뢰도 = (a,b를 같이 산 바구니의 수) / (a를 산 바구니의 수)

# from collections import Counter

# # filename, reliability, choice = input("파일 이름, 신뢰도, 지지도를 입력하세요: ").split()

# def counter(fname):
#     file = open(fname + ".txt", "r")
#     single = {}
#     freq = {}
#     N = 0 # 바구니 수

#     for line in file:
#         N += 1
#         words = [int(x) for x in line.split()]
#         items = sorted(set(words[2:]))
#         for x in range(len(items)):
#             single[x] = single.get(x, 0) + 1
#             for y in range(x+1, len(items)):
#                 freq[(items[x], items[y])] = freq.get((items[x], items[y]), 0) + 1

#     c = Counter(freq)
#     return c.most_common(5), N, single

# print(counter("small"))


# # ===== PageRank 구하기 =====

# import os
# path = os.chdir("../AI/COG_ICT/data")

# fname = input("파일 이름: ")

# def make_graph(fname):
#     file = open(fname+".txt", "r")
#     graph = {}
#     nset = set()

#     for line in file:
#         src, dest = [int(x) for x in line.split()]
#         if src in graph:
#             graph[src].add(dest)
#         else:
#             graph[src] = {dest}
#         nset.add(src)
#         nset.add(dest)
    
#     if nset > set(graph.keys()): # 걸리면 Spyder가 존재
#         dangling = nset - set(graph.keys())
#         for node in dangling:
#             graph[node] = nset # Spyder는 모든 노드에 rank를 flooding

#     return graph, {x:1/len(nset) for x in nset}

# def calc_rank(graph, old_rank):
#     N = len(graph)
#     rank = {x:0 for x in graph.keys()}
    
#     for x in graph:
#         delta = old_rank[x] / len(graph[x])
#         for dest in graph[x]:
#             rank[dest] += delta
#     return rank

# graph, rank_init = make_graph(fname)
# rank_after = calc_rank(graph, rank_init)
# print(rank_after)

# rank_init, rank_after = rank_after, rank_init
# rank_after = calc_rank(graph, rank_init)
# print(rank_after)

# rank_init, rank_after = rank_after, rank_init
# rank_after = calc_rank(graph, rank_init)
# print(rank_after)

# rank_init, rank_after = rank_after, rank_init
# rank_after = calc_rank(graph, rank_init)
# print(rank_after)

# rank_init, rank_after = rank_after, rank_init
# rank_after = calc_rank(graph, rank_init)
# print(rank_after)


# ===== 콘텐츠 구매 기록 생성 =====

from collections import Counter

class View():
    def __init__(self, vlist):
        self.data = set(vlist)

    def distance(self, other):
        return 1 - len(self.data & other.data) / len(self.data | other.data)

    def __sub__(self, other):
        return self.data - other.data

    def __repr__(self):
        return f"{self.data}"

fname = input("파일 이름: ").strip()
file = open(fname + ".txt", "r")

user_view = {}
for line in file:
    words = line.split()
    user_view[words[0]] = View([int(x) for x in words[1:]])

while True:
    user = input("추천할 사람은? ")
    if user == 'q': break

    target = user_view[user]
    slist = sorted(user_view.items(), key=lambda x:x[1].distance(target))
    
    for x in range(len(slist)):
        if user == slist[x][0]:
            slist.pop(x)
            break
    print(slist)

    rlist = []
    for x in range(3):
        rlist.extend(slist[x][1] - target)
    print(rlist)

    c = Counter(rlist)
    print(c.most_common(2))






