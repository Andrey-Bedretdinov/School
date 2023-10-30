import matplotlib
import numpy as np

matplotlib.use('MacOSX')
import matplotlib.pyplot as plt


# функция, описывающая дифференциальное уравнение
def f(x, y):
    return x * np.exp(-x ** 2) - 2 * x * y  # вычисляем значение функции f(x, y)


# метод Эйлера
def euler_method(x0, y0, h, x_end):
    x_values = [round(x0, 15)]  # создаем список для значений x, начиная с x0, и округляем до 6 знаков после запятой
    y_values = [round(y0, 15)]  # создаем список для значений y, начиная с y0, и округляем до 6 знаков после запятой

    # выполняем итерации до тех пор, пока x меньше x_end
    while x0 < x_end:
        y0 = round(y0 + h * f(x0, y0), 15)  # вычисляем следующее значение y с использованием метода Эйлера и округляем
        x0 = round(x0 + h, 15)  # увеличиваем x на шаг h
        x_values.append(x0)  # добавляем новое значение x в список
        y_values.append(y0)  # добавляем новое значение y в список

    return x_values, y_values


# Рунге-Кутта 4 порядка
def runge_kutta_4th_order(x0, y0, h, x_end):
    x_values = [round(x0, 15)]
    y_values = [round(y0, 15)]

    # выполняем итерации до тех пор, пока x меньше x_end
    while x0 < x_end:
        # вычисляем коэффициенты
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + 0.5 * h, y0 + 0.5 * k1)
        k3 = h * f(x0 + 0.5 * h, y0 + 0.5 * k2)
        k4 = h * f(x0 + h, y0 + k3)

        y0 = round(y0 + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4), 15)  # вычисляем следующее значение y
        x0 = round(x0 + h, 15)  # увеличиваем x на шаг h
        x_values.append(x0)  # добавляем новое значение x
        y_values.append(y0)  # добавляем новое значение y

    return x_values, y_values


def cauchy_solution(x_values):
    y_values = np.exp(-np.square(x_values)) * (1 + 0.5 * np.square(x_values))
    return y_values


def write_to_file(filename, x_values, y_values):
    with open(filename, 'w') as file:
        for x, y in zip(x_values, y_values):
            file.write(f"{x} {y}\n")


x0, y0 = 0, 1  # начальные условия
h = 0.05  # шаг
x_end = 1  # конечное значение x

x_values_euler, y_values_euler = euler_method(x0, y0, h, x_end)
x_values_rk4, y_values_rk4 = runge_kutta_4th_order(x0, y0, h, x_end)

write_to_file("euler_results.txt", x_values_euler, y_values_euler)
write_to_file("runge_kutta_4th_order_results.txt", x_values_rk4, y_values_rk4)

print(x_values_euler)
print(y_values_euler)

print('-------------------')

print(x_values_rk4)
print(y_values_rk4)

print('-------------------  y(b) = 0,5518191618')

# значение аналитического решения в точке b
y_exact_b = 0.5518191618

# Погрешности для метода Эйлера и метода Рунге-Кутта 4-го порядка
epsilon_euler = abs(y_exact_b - y_values_euler[-1])
epsilon_rk4 = abs(y_exact_b - y_values_rk4[-1])

print(f"Погрешность метода Эйлера: {epsilon_euler:.15f}")
print(f"Погрешность метода Рунге-Кутта 4-го порядка: {epsilon_rk4:.15f}")

x_values = np.arange(0, 1.05, 0.05)
y_values = cauchy_solution(x_values)

plt.figure(figsize=(10, 6))

plt.plot(x_values_euler, y_values_euler, label='Метод Эйлера', color='blue')

plt.plot(x_values_rk4, y_values_rk4, label='Метод Рунге-Кутта 4 порядка', color='red', linestyle='dashed')

plt.plot(x_values, y_values, label='Аналитическое решение', color='green')

plt.title('Сравнение методов Эйлера и Рунге-Кутта 4 порядка')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Отображаем график
plt.grid(True)
plt.show()
