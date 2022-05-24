
# def service_lane(width, cases):
#     result = []
#     for index in range(len(cases)):
#         element_case = cases[index]
#         i = element_case[0]
#         j = element_case[1]
#         slice_width = min(width[i:j + 1])
#         result.append(slice_width)

#     return result



# cases = [[0,3], [4,6], [6,7], [3,5], [0,7]]
# width = [2,3,1,2,3,2,3,3]

# answer = service_lane(width, cases)
# print(answer)

n,t = map(int,input().split())
width = list(map(int,input().split()))
for _ in range(t):
    i,j = map(int,input().split())
    print(min(width[i:j+1]))