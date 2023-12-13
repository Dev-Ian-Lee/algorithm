# https://www.acmicpc.net/problem/16926

# 걸린 시간: 120min
# 시간복잡도: O(N * M * R)

# 초기에는 new_arr을 매 반복(R)마다 새로 생성하는 것 대신, 처음에만 생성해 반복이 끝날 때마다 arr 에 deepcopy함
# 이 경우, deepcopy의 시간복잡도가 O(N)이기 때문에 시간 초과 발생

# 해당 코드도 Python3로 제출 시 시간 초과, PyPy3로 제출 시 통과

import sys

N, M, R = map(int, sys.stdin.readline().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

direction = 0

for _ in range(R):
    i = 0
    j = 0
    layer_cnt = 0

    # 매 반복마다 새로운 배열 생성
    new_arr = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(N * M):
        # 하
        if direction == 0:
            # 각 단계의 첫 번째 항목은 direction == 3일 때 계산하기 위해 pass
            if i == j:
                i += 1

            new_arr[i][j] = arr[i - 1][j]

            i += 1
            # 해당 방향의 칸을 모두 고려했을 경우, 방향 전환
            # 각 레이어(단계)마다 계산할 칸 수 감소
            if i >= N - layer_cnt:
                i -= 1
                j += 1
                direction += 1

        # 우
        elif direction == 1:
            new_arr[i][j] = arr[i][j - 1]

            j += 1
            if j >= M - layer_cnt:
                i -= 1
                j -= 1
                direction += 1

        # 상
        elif direction == 2:
            new_arr[i][j] = arr[i + 1][j]

            i -= 1
            if i < layer_cnt:
                i += 1
                j -= 1
                direction += 1

        # 좌
        elif direction == 3:
            new_arr[i][j] = arr[i][j + 1]

            j -= 1

            # 해당 레이어 계산이 끝났을 경우(첫 번째 항목으로 돌아온 경우), 다음 레이어로 이동
            if i == j + 1:
                new_arr[i][j + 1] = arr[i][j + 2]

                i += 1
                j += 2
                layer_cnt += 1
                direction = 0

    # 배열에 회전한 결과인 새로운 배열을 덮어씌움
    arr = new_arr

for line in new_arr:
    for ele in line:
        print(ele, end=" ")

    print()
