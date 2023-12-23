# https://www.acmicpc.net/problem/9465

# 걸린 시간: -
# 시간복잡도: O()

# DP로 풀어야겠다는 생각은 했는데 구현하는 방법이 생각나지 않아서 검색해서 해결
# 행이 2로 고정이기 때문에 DP 테이블을 이중 리스트로 사용
# DP의 경우 선택지를 반영할지 여부를 이지선다가 아닌 삼지선다로도 선택 가능

# 각 열에서의 최대값을 계산하는 방식으로 접근

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    dp = [[0 for _ in range(n)] for _ in range(2)]
    
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().rstrip().split())))
            
    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        
    elif n == 2:
        print(max(stickers[0][0] + stickers[1][1], stickers[0][1] + stickers[1][0]))
        
    else:
            
        # dp는 각 열의 최대값을 의미
        # stickers의 0번 인덱스까지만을 고려할 때, 각 열의 첫 번째 항목이 0열에서의 최대값
        dp[0][0] = stickers[0][0]
        dp[1][0] = stickers[1][0]
        
        # 1열에서의 최대값의 경우, 0열에서 위(아래) 칸을 뗐을 경우 그 대각선인 아래(위) 칸을 더한 값
        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] = dp[0][0] + stickers[1][1]
        
        # 2열부터의 최대값은 이전 열까지의 대각선값, 0행의 전전 열까지의 핪, 1행의 전전 열까지의 합 중 가장 큰 값에 현재 스티커 값을 더한 값
        # 이전 열에서 아무것도 선택하지 않고 현재 스티커를 뗐을 때 최대값일 수도 있기 때문에, 전전 열까지 고려
        for i in range(2, n):
            dp[0][i] = stickers[0][i] + max(dp[1][i - 1], dp[0][i - 2], dp[1][i - 2])
            dp[1][i] = stickers[1][i] + max(dp[0][i - 1], dp[0][i - 2], dp[1][i - 2])
            
        print(max(dp[0][n - 1], dp[1][n - 1]))