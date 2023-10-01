# https://www.acmicpc.net/problem/1253

# 걸린 시간: -
# 시간복잡도: O(N^2)

# 처음엔 combinations로 가능한 합의 조합을 구한 뒤 set에 저장하고, for문으로 각각의 수가 set에 있는지 검사하는 방식으로 구현
# 이 경우, 다른 두 수의 합으로 구한 값인지 자기 자신을 포함한 값인지 구분하지 못해 0이 포함된 경우 틀린 답 반환

# for문을 한 번 더 사용해 매 반복마다 자기 자신을 제외한 조합을 구해 set에 저장할 경우, 답은 맞는데 시간 초과 발생
# 해결할 방법이 생각이 안 나서 검색

N = int(input())
nums = list(map(int, input().split()))

nums.sort()

cnt = 0
for i in range(N):
    
    # 음수도 존재할 수 있기 때문에 현재 값을 제외한 모든 수를 고려
    tmp = nums[:i] + nums[i + 1:]
    start, end = 0, len(tmp) - 1
    
    # 투포인터를 이분 탐색과 비슷한 형태로 구현
    while True:
        if start >= end:
            break
        
        val = tmp[start] + tmp[end]
        
        if val < nums[i]:
            start += 1
            
        elif val > nums[i]:
            end -= 1
            
        else:
            cnt += 1
            break
        
print(cnt)