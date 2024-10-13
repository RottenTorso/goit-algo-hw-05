import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i = i + m - min(k, j + 1)
            k = m - 1
    return -1

# Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    
    if m > n:
        return -1
    
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Тексти для тестування
text1 = """..."""  # Вставте текст статті 1
text2 = """..."""  # Вставте текст статті 2

# Підрядки для тестування
existing_substring = "алгоритм"
non_existing_substring = "неіснуючий"

# Вимірювання часу виконання
def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1000)

# Вимірювання для статті 1
time_boyer_moore_text1_exist = measure_time(boyer_moore, text1, existing_substring)
time_kmp_text1_exist = measure_time(kmp_search, text1, existing_substring)
time_rabin_karp_text1_exist = measure_time(rabin_karp, text1, existing_substring)

time_boyer_moore_text1_non_exist = measure_time(boyer_moore, text1, non_existing_substring)
time_kmp_text1_non_exist = measure_time(kmp_search, text1, non_existing_substring)
time_rabin_karp_text1_non_exist = measure_time(rabin_karp, text1, non_existing_substring)

# Вимірювання для статті 2
time_boyer_moore_text2_exist = measure_time(boyer_moore, text2, existing_substring)
time_kmp_text2_exist = measure_time(kmp_search, text2, existing_substring)
time_rabin_karp_text2_exist = measure_time(rabin_karp, text2, existing_substring)

time_boyer_moore_text2_non_exist = measure_time(boyer_moore, text2, non_existing_substring)
time_kmp_text2_non_exist = measure_time(kmp_search, text2, non_existing_substring)
time_rabin_karp_text2_non_exist = measure_time(rabin_karp, text2, non_existing_substring)

# Висновки
results = {
    "text1": {
        "existing": {
            "Boyer-Moore": time_boyer_moore_text1_exist,
            "KMP": time_kmp_text1_exist,
            "Rabin-Karp": time_rabin_karp_text1_exist
        },
        "non_existing": {
            "Boyer-Moore": time_boyer_moore_text1_non_exist,
            "KMP": time_kmp_text1_non_exist,
            "Rabin-Karp": time_rabin_karp_text1_non_exist
        }
    },
    "text2": {
        "existing": {
            "Boyer-Moore": time_boyer_moore_text2_exist,
            "KMP": time_kmp_text2_exist,
            "Rabin-Karp": time_rabin_karp_text2_exist
        },
        "non_existing": {
            "Boyer-Moore": time_boyer_moore_text2_non_exist,
            "KMP": time_kmp_text2_non_exist,
            "Rabin-Karp": time_rabin_karp_text2_non_exist
        }
    }
}

# Вивід результатів
for text, data in results.items():
    print(f"Results for {text}:")
    for pattern_type, times in data.items():
        print(f"  {pattern_type}:")
        for algorithm, time in times.items():
            print(f"    {algorithm}: {time:.6f} seconds")
