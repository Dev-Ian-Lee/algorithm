# https://www.acmicpc.net/problem/17779

# 걸린 시간: -
# 시간복잡도: ???

# x + d1 + d2 <= N 조건 고려 안 했더니 인덱스 에러 발생 -> 검색 통해 해결(문제의 모든 조건 고려하기)
# 경계선 구현 안 하고 문제 조건대로 1번 ~ 4번 구역만 고려하면 되는 줄 알았으나, 구현해야 함
# 배열 전체 합(total) 구한 뒤 1번 ~ 4번 구역 빼면 5번 구역 쉽게 구할 수 있음
# 2번, 4번 구역은 뒤에서부터 반복해야하는 걸 고려 못해서 시간 오래 걸림

N = int(input())

city = []
for _ in range(N):
    city.append(list(map(int, input().split())))
    
total = 0
for i in range(N):
    for j in range(N):
        total += city[i][j]
    
ans = int(1e9)
area = []

for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d1 in range(1, y):
            for d2 in range(1, N - y + 1):
                
                # 범위 조건
                if x + d1 + d2 > N:
                    continue
                
                # 경계선
                temp = [[0 for _ in range(N)] for _ in range(N)]
                for i in range(d1 + 1):
                    temp[x + i - 1][y - i - 1] = 5
                    
                for i in range(d2 + 1):
                    temp[x + i - 1][y + i - 1] = 5
                    
                for i in range(d2 + 1):
                    temp[x + d1 + i - 1][y - d1 + i - 1] = 5
                    
                for i in range(d1 + 1):
                    temp[x + d2 + i - 1][y + d2 - i - 1] = 5
                
                # 1번 ~ 4번 구역 계산
                # 각 행에서 경계선 만날 경우 break
                # 2번, 4번 구역의 경우 뒤에서부터 check
                one = 0
                for r in range(1, x + d1):
                    for c in range(1, y + 1):
                        if temp[r - 1][c - 1] == 5:
                            break
                        
                        one += city[r - 1][c - 1]
                
                two = 0
                for r in range(1, x + d2 + 1):
                    for c in range(N, y, -1):
                        if temp[r - 1][c - 1] == 5:
                            break
                        
                        two += city[r - 1][c - 1]
                        
                three = 0
                for r in range(x + d1, N + 1):
                    for c in range(1, y - d1 + d2):
                        if temp[r - 1][c - 1] == 5:
                            break
                        
                        three += city[r - 1][c - 1]
        
                four = 0
                for r in range(x + d2 + 1, N + 1):
                    for c in range(N, y - d1 + d2 - 1, -1):
                        if temp[r - 1][c - 1] == 5:
                            break
                        
                        four += city[r - 1][c - 1]
                
                area = [one, two, three, four]
                five = total - sum(area)
                area.append(five)
                
                val = max(area) - min(area)
                
                if val < ans:
                    ans = val
                    
print(ans)