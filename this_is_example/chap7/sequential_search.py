# <이것이 취업을 위한 코딩 테스트다> 예제 7-1

def sequential_search(N, target, array):
    for i in range(N):
        if array[i] == target:
            return i + 1
        
array = ['Aa', 'Bb', 'Cc']
print(sequential_search(len(array), 'Bb', array))