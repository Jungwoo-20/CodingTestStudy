from collections import deque


def solution(cacheSize, cities):
    answer = 0
    q = deque()
    for city in cities:
        city = city.lower()
        if cacheSize:
            if city not in q:
                if len(q) == cacheSize:
                    q.popleft()
                q.append(city)
                answer += 5
            else:
                q.remove(city)
                q.append(city)
                answer += 1
        else:
            return len(cities) * 5
    return answer


cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize,cities))