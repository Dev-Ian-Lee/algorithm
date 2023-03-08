# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    arr1 = make_array(str1)
    arr2 = make_array(str2)
    
    # 둘 다 공집합일 경우, 자카드 유사도가 1
    if len(arr1) == 0 and len(arr2) == 0:
        return 65536
    
    set1 = set(arr1)
    set2 = set(arr2)
    
    union = []
    intersection = []
    
    for ele in set1:

        # set1과 set2에 모두 있는 원소의 경우
        if ele in set2:
            cnt1 = arr1.count(ele)
            cnt2 = arr2.count(ele)
            
            # 합집합에는 최대 개수만큼 추가
            for i in range(max(cnt1, cnt2)):
                union.append(ele)
            
            # 교집합에는 최소 개수만큼 추가
            for i in range(min(cnt1, cnt2)):
                intersection.append(ele)
            
        # set1에만 있는 원소의 경우, arr1에 있는 개수만큼 합집합에 추가
        else:
            cnt = arr1.count(ele)
            
            for i in range(cnt):
                union.append(ele)
            
    # 차집합을 사용해 set2에만 있는 경우 처리
    # set2에만 있는 원소의 경우, arr2에 있는 개수만큼 합집합에 추가
    diff = set2 - set1
    for ele in diff:
        cnt = arr2.count(ele)
            
        for i in range(cnt):
            union.append(ele)
    
    return int((len(intersection) / len(union)) * 65536)
                
# 문자열에서 알파벳으로만 이루어진 두 글자 문자열 리스트 반환
def make_array(s):
    arr = []
    size = len(s)
    
    for i in range(size - 1):
        cur = s[i].lower()
        nex = s[i + 1].lower()
        
        if ord('a') <= ord(cur) <= ord('z'):
            if ord('a') <= ord(nex) <= ord('z'):
                arr.append(cur + nex)
                
    return arr