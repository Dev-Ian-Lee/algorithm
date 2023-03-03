# https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    # 캐시 사이즈가 0일 경우, 모든 도시가 캐시 미스
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = []
    runtime = 0
    
    # 대소문자를 구분하지 않으므로 모든 도시를 소문자로 변환
    cities = [ele.lower() for ele in cities]
    
    i = 0
    while True:
        # 캐시가 가득 찼을 경우 종료
        if len(cache) == cacheSize:
            break
    
        # 캐시에 없는 도시는 맨 뒤에 추가
        if cities[i] not in cache:
            cache.append(cities[i])
            runtime += 5
            
        # 캐시에 있는 도시는 해당 위치에서 추출한 뒤 맨 뒤에 추가
        else:
            popped = cache.pop(cache.index(cities[i]))
            cache.append(popped)
            runtime += 1
            
        i += 1
    
    # 앞에서 고려한 도시들 이후로부터 반복
    for city in cities[i:]:

        # 캐시에 없는 도시일 경우
        if city not in cache:
            cache.pop(0)
            cache.append(city)
            runtime += 5
            continue
        
        # 캐시에 있는 도시일 경우
        for i in range(cacheSize):
            if cache[i] == city:
                popped = cache.pop(i)
                cache.append(popped)
                runtime += 1
                break
            
    return runtime