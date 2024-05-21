import heapq

def merge_k_lists(lists):
    # Мін-купа для зберігання елементів
    min_heap = []
    
    # Додаємо перші елементи з кожного списку до купи
    for i, lst in enumerate(lists):
        if lst:  # Перевіряємо, що список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента в списку)
    
    merged_list = []
    
    # Поки купа не порожня
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)
        
        # Якщо є ще елементи в цьому списку, додаємо наступний до купи
        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1], list_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)