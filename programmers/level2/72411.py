# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter

# 걸린 시간: -
# 시간복잡도: ???

# 가능한 조합을 구하는 방법이 생각이 안 나서 검색
# 문자열 정렬은 sort 대신 sorted 사용
# combinations로 메뉴 개수 별 가능한 조합 계산 후, Counter 사용해 조합별 빈도 계산
# 딕셔너리에 메뉴 개수 별 최대 빈도 수 저장
# answer 리스트에 딕셔너리에 저장된 최대 빈도 수와 같은 빈도 수의 메뉴 조합 추가

def solution(orders, course) :
    answer = []
    combs = []

    for order in orders :
        # 문자열 정렬
        order = sorted(order)
        
        # 가능한 메뉴 조합
        for c in course :
            combs += combinations(order, c)

    # 조합별 빈도 계산
    value = Counter(combs).most_common()
    
    dict = {}
    for menu, frequency in value :
        # 딕셔너리에 해당 메뉴 개수로 저장된 값이 없거나, 해당 메뉴 개수로 된 조합의 빈도가 같은 경우 코스에 추가
        if len(menu) not in dict.keys() or dict[len(menu)] == frequency :
            
            # 1명 이하로 주문한 코스는 고려 X
            if frequency <= 1 :
                break
            
            answer.append(''.join(menu))
            
            # 메뉴 개수의 최대 빈도 수를 딕셔너리에 저장
            dict[len(menu)] = frequency

    answer.sort()
    return answer