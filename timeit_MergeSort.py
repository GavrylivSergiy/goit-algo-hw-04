import timeit
import random
import pandas as pd

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Функція для тестування та порівняння алгоритмів сортування
def test_sorting_algorithms():
    # Генерація тестових даних
    data_sizes = [10, 100, 1000, 10000]
    data_types = {
        'random': lambda n: random.sample(range(n * 10), n),
        'sorted': lambda n: list(range(n)),
        'reverse_sorted': lambda n: list(range(n, 0, -1)),
        'almost_sorted': lambda n: sorted(random.sample(range(n * 10), n)),
    }

    results = []

    for size in data_sizes:
        for data_type, data_gen in data_types.items():
            data = data_gen(size)

            # Час виконання Merge Sort
            merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)

            # Час виконання Insertion Sort
            insertion_time = None
            if size <= 1000:  # Обмеження для великих розмірів через високу складність
                insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)

            # Час виконання Bubble Sort
            bubble_time = None
            if size <= 1000:  # Обмеження для великих розмірів через високу складність
                bubble_time = timeit.timeit(lambda: bubble_sort(data.copy()), number=1)

            # Час виконання Timsort (Python's sorted)
            timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)

            results.append((size, data_type, merge_time, insertion_time, bubble_time, timsort_time))

    return results

if __name__ == "__main__":
    results = test_sorting_algorithms()

    # Перетворення результатів у DataFrame
    df = pd.DataFrame(results, columns=["Size", "Type", "Merge Sort", "Insertion Sort", "Bubble Sort", "Timsort"])

    # Додавання теоретичних складностей
    complexities = {
        'Merge Sort': {'Best': 'O(n log n)', 'Average': 'O(n log n)', 'Worst': 'O(n log n)', 'Space': 'O(n)'},
        'Insertion Sort': {'Best': 'O(n)', 'Average': 'O(n^2)', 'Worst': 'O(n^2)', 'Space': 'O(1)'},
        'Bubble Sort': {'Best': 'O(n)', 'Average': 'O(n^2)', 'Worst': 'O(n^2)', 'Space': 'O(1)'},
        'Timsort': {'Best': 'O(n)', 'Average': 'O(n log n)', 'Worst': 'O(n log n)', 'Space': 'O(n)'}
    }

    # Виведення пояснень і складностей
    descriptions = {
        'Merge Sort': "Сортування злиттям - це алгоритм розділяй і володарюй, який розділяє масив на частини, сортує їх окремо, а потім об'єднує їх назад у відсортований масив. Це стабільний алгоритм, який добре працює з великими наборами даних.",
        'Insertion Sort': "Сортування вставками - це простий алгоритм, який будує остаточний відсортований масив, додаючи один елемент за раз. Ефективний для малих наборів даних або майже відсортованих масивів, але неефективний для великих наборів даних.",
        'Bubble Sort': "Сортування бульбашкою - це простий алгоритм порівняння, який повторно проходить по списку, порівнює сусідні елементи та міняє їх місцями, якщо вони знаходяться в неправильному порядку. Не підходить для великих наборів даних.",
        'Timsort': "Timsort - це гібридний алгоритм сортування, заснований на сортуванні злиттям та сортуванні вставками. Це стандартний алгоритм сортування в Python завдяки його ефективності та стабільності."
    }

    for algo, comp in complexities.items():
        print(f"\n{algo}:\n{descriptions[algo]}")
        print(f"Найкраща складність: {comp['Best']}")
        print(f"Середня складність: {comp['Average']}")
        print(f"Найгірша складність: {comp['Worst']}")
        print(f"Просторова складність: {comp['Space']}\n")

    print("Результати продуктивності:")
    print(df.to_string(index=False))