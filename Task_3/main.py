from core.file_operations import read_file
from core.search_algorithms import boyer_moore_search, kmp_search, rabin_karp_search
from core.performance_measurement import time_algorithm
from tabulate import tabulate
import os

def main():
    current_directory = os.path.dirname(__file__)
    text_folder = "text"
    file_name1 = "article_1.txt"
    file_name2 = "article_2.txt"
    
    text1 = read_file(os.path.join(current_directory, text_folder, file_name1))
    text2 = read_file(os.path.join(current_directory, text_folder, file_name2))

    existing_substring_text1 = "алгоритми"
    nonexisting_substring_text1 = "мила маму раму але так і не домила"  
    existing_substring_text2 = "рекомендаційні системи"  
    nonexisting_substring_text2 = "абабагаламага"


    algorithm_names = {
    'boyer_moore_search': 'Боєр-Мур',
    'kmp_search': 'Кнут-Морріс-Пратт',
    'rabin_karp_search': 'Рабін-Карп'}
    
    headers = ["Алгоритм", "Існуючий підрядок (Текст 1)", "Неіснуючий підрядок (Текст 1)", "Існуючий підрядок (Текст 2)", "Неіснуючий підрядок (Текст 2)", "Загальний час"]
    data = []
    
    for algo in ['boyer_moore_search', 'kmp_search', 'rabin_karp_search']:
        time_exist_text1 = time_algorithm(algo, text1, existing_substring_text1, globals())
        time_nonexist_text1 = time_algorithm(algo, text1, nonexisting_substring_text1, globals())
        time_exist_text2 = time_algorithm(algo, text2, existing_substring_text2, globals())
        time_nonexist_text2 = time_algorithm(algo, text2, nonexisting_substring_text2, globals())
        total_time = time_exist_text1 + time_nonexist_text1 + time_exist_text2 + time_nonexist_text2
        
        data.append([algorithm_names[algo], time_exist_text1, time_nonexist_text1, time_exist_text2, time_nonexist_text2, total_time])
    
    print(tabulate(data, headers=headers, tablefmt="github", floatfmt=">.6f", numalign="center"))

if __name__ == "__main__":
    main()