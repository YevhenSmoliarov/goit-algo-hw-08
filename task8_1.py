import heapq

def min_cost_to_connect_cables(cables):
    # Перетворення списку кабелів на мін-купу
    heapq.heapify(cables)
    
    total_cost = 0
    
    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягування двох найкоротших кабелів
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Обчислення вартості їх з'єднання
        cost = first + second
        total_cost += cost
        
        # Поміщення нового кабеля назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні загальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))