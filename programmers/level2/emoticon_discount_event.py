# https://school.programmers.co.kr/learn/courses/30/lessons/150368

# itertools의 product를 사용해 할인율로 만들 수 있는 모든 조합 고려
from itertools import product

def solution(users, emoticons):
    result = [0, 0]
    size = len(emoticons)
    discount_ratio = [10, 20, 30, 40]
    
    for case in product(discount_ratio, repeat = size):
        num_join = 0
        total_amount = 0
        
        for user in users:
            ratio, money = user
            amount = 0
            
            for i in range(size):
                # 사용자가 정한 비율보다 할인율이 큰 이모티콘 모두 구매
                if ratio <= case[i]:
                    amount += emoticons[i] * ((100 - case[i]) / 100)
                    
            # 조건에 맞는 이모티콘을 모두 구매한 금액이 사용자가 가진 돈보다 클 경우, 이모티콘 플러스 가입
            if amount >= money:
                num_join += 1
                
            # 그렇지 않을 경우, 이모티콘 매출액에 반영
            else:
                total_amount += amount
                
        # 가입자 수, 판매액이 최대로 되도록 갱신
        if result[0] < num_join or (result[0] == num_join and result[1] < total_amount):
            result = [num_join, int(total_amount)]
            
    return result