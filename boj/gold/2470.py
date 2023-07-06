# https://www.acmicpc.net/problem/2470

import sys

n = int(sys.stdin.readline())
fluid = list(map(int, sys.stdin.readline().split()))

fluid.sort()

start = 0
end = len(fluid) - 1

# 가장 왼쪽(알칼리성)의 용액과 가장 오른쪽(산성)의 용액을 초기값으로 사용
optimum = fluid[start] + fluid[end]
optimum_fluids = [fluid[start], fluid[end]]
while True:

    # 서로 다른 두 용액을 혼합해야하므로 두 값이 같아질 때도 break
    if start >= end:
        break

    mixed = fluid[start] + fluid[end]

    # 현재 두 용액을 혼합한 것의 절대값(0과의 차이)이 최적값의 절대값보다 작을 경우, 최적값 갱신
    if abs(mixed) < abs(optimum):
        optimum = mixed
        optimum_fluids = [fluid[start], fluid[end]]

    # 특성값이 0이 됐을 경우 종료
    if mixed == 0:
        break

    # 0보다 작을 경우 특성값을 키우기 위해 start를 오른쪽으로 한 칸 이동
    elif mixed < 0:
        start += 1

    # 0보다 클 경우 특성값을 줄이기 위해 end를 왼쪽으로 한 칸 이동
    else:
        end -= 1

print(optimum_fluids[0], optimum_fluids[1])