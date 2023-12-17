import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('MacOSX')


# Расчет коэффициента корреляции Пирсона
def calculate_pearson_correlation(x, y):
    # Среднее значение
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Стандартное отклонение
    std_x = np.std(x)
    std_y = np.std(y)

    # Ковариацию между переменными x и y
    cov_xy = np.mean(x * y) - mean_x * mean_y

    return cov_xy / (std_x * std_y)


def plot_data_and_regression_line(x, y, slope, intercept):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Данные')

    # Линия регрессии
    plt.plot(x, intercept + slope * x, color='red', label='Линия регрессии')

    plt.xlabel('Процентное содержание компонента (X)')
    plt.ylabel('Твёрдость по шкале Роквелла (Y)')
    plt.title('Корреляционное поле и линия регрессии')
    plt.legend()
    plt.grid(True)

    plt.show()


data_x = np.array([3.9, 6.5, 3.7, 4.5, 5.0, 5.8, 3.3, 6.2, 3.6, 3.9, 5.1, 6.4,
                   4.2, 4.9, 6.0, 5.4, 4.4, 3.8, 6.7, 4.6, 4.3, 6.3, 5.2, 6.4,
                   6.2, 5.5, 2.7, 2.8, 5.4, 5.8, 6.6, 5.3, 4.2, 4.3, 4.0, 5.4])
data_y = np.array([56, 55, 43, 55, 46, 54, 42, 63, 48, 45, 50, 58,
                   50, 54, 52, 50, 60, 53, 63, 51, 45, 60, 48, 61,
                   56, 46, 41, 43, 58, 60, 61, 55, 46, 53, 51, 56])

# Коэффициента корреляции Пирсона
pearson_correlation_coefficient = calculate_pearson_correlation(data_x, data_y)
print("Коэффициент корреляции Пирсона:", pearson_correlation_coefficient)

# Параметры линейной регрессии
mean_x = np.mean(data_x)
mean_y = np.mean(data_y)
std_x = np.std(data_x, ddof=1)
std_y = np.std(data_y, ddof=1)
cov_xy = np.mean(data_x * data_y) - mean_x * mean_y
slope = cov_xy / (std_x ** 2)
intercept = mean_y - slope * mean_x

# Коэффициент детерминации R^2
r_squared = pearson_correlation_coefficient ** 2

print("Уравнение линейной регрессии: Y =", slope, "* X +", intercept)
print("Коэффициент детерминации (R^2):", r_squared)

plot_data_and_regression_line(data_x, data_y, slope, intercept)
