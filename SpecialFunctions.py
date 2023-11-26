from collections import Counter

#Media
def mean(array):
    result = 0
    for i in range(len(array)):
        result += array[i]
    return result / len(array)

#Mediana
def median(array):
    sorted_array = sorted(array)
    length = len(sorted_array)

    if length % 2 == 0:
        mid1 = sorted_array[length // 2 - 1]
        mid2 = sorted_array[length // 2]
        return (mid1 + mid2) / 2
    else:
        return sorted_array[length // 2]

#Moda
def mode(array):
    counts = Counter(array)
    max_frequency = max(counts.values())
    moda = [k for k, v in counts.items() if v == max_frequency]
    return moda

#Varianza
def variance(array):
    n = len(array)
    mean_value = sum(array) / n
    squared_diff = [(x - mean_value) ** 2 for x in array]
    variance_result = sum(squared_diff) / n
    return variance_result

#Desviacion estandar
def standard_deviation(array):
    return math.sqrt(variance(array))

#Rango de un arreglo
def data_range(array):
    return max(array) - min(array)

#Suma de elementos de un arreglo
def sum_values(array):
    return sum(array)

#Producto de elementos de un arreglo
def product_values(array):
    result = 1
    for x in array:
        result *= x
    return result

#Coeficiente de correlacion
def correlation_coefficient(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator_x = math.sqrt(sum((xi - mean_x)**2 for xi in x))
    denominator_y = math.sqrt(sum((yi - mean_y)**2 for yi in y))
    return numerator / (denominator_x * denominator_y)
