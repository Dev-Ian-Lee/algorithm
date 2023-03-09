# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):

    # 할인 목록 중에 없는 제품이 하나라도 있을 경우, 0 반환
    for ele in want:
        if ele not in discount:
            return 0
    
    cnt = 0
    
    # 원하는 제품을 원하는 개수만큼 쇼핑 목록에 저장 후 정렬
    shop = []
    for idx in range(len(want)):
        for _ in range(number[idx]):
            shop.append(want[idx])
            
    shop.sort()
    
    i = 0
    while True:
        if i > len(discount) - 10:
            break
            
        # 할인 목록에서 10일 치를 잘라 판매 목록으로 만든 뒤 정렬
        sale = discount[i:i + 10]
        sale.sort()
        
        # 판매 목록과 쇼핑 목록이 같은 경우, 카운트 증가
        if sale == shop:
            cnt += 1
            
        i += 1
        
    return cnt