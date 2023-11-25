# statistik.py

def mean(data):
    # Menghitung rata-rata dari data
    return sum(data) / len(data)

def median(data):
    # Menghitung median dari data
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_data[n // 2]

def variance(data):
    # Menghitung varians dari data
    n = len(data)
    mean_val = mean(data)
    return sum((x - mean_val) ** 2 for x in data) / n

def standard_deviation(data):
    # Menghitung deviasi standar dari data
    return variance(data) ** 0.5
