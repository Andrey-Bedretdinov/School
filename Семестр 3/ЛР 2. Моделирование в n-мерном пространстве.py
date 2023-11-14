from scipy.integrate import solve_ivp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('MacOSX')

rho_air = 1.2041  # Плотность воздуха
C = 0.47  # Коэффициент сопротивления
rho_projectile = 7200  # Плотность материала снаряда
d = 0.1  # Диаметр снаряда
v0 = 1000  # Начальная скорость
alpha = 45  # Угол наклона (градусы)

# Перевод угла в радианы
alpha_rad = np.radians(alpha)

# Вычисление площади поперечного сечения снаряда
area = np.pi * (d / 2) ** 2

# Вычисление массы снаряда
volume = (4 / 3) * np.pi * (d / 2) ** 3
mass = rho_projectile * volume

# Ускорение свободного падения
g = 9.81

# Начальные условия
x01 = 0
x02 = 0
v01 = abs(v0) * np.cos(alpha_rad)
v02 = abs(v0) * np.sin(alpha_rad)
initial_conditions = [x01, x02, v01, v02]

# Временной интервал
t0 = 0
tm = 150
t_span = [t0, tm]
t_eval = np.arange(t0, tm, 1)


def ode_system(t, y, k):
    x1, x2, v1, v2 = y
    dx1dt = v1
    dx2dt = v2
    dv1dt = -k * np.sqrt(v1 ** 2 + v2 ** 2) * v1
    dv2dt = -k * np.sqrt(v1 ** 2 + v2 ** 2) * v2 - g
    return [dx1dt, dx2dt, dv1dt, dv2dt]


def print_solution(solution, label):
    if solution.success:
        print(f"Результаты для {label}:")
        print("Время: ", solution.t)
        for i, var in enumerate(['x1', 'x2', 'v1', 'v2']):
            print(f"{var}: ", solution.y[i])
        print("\n")
    else:
        print(f"Решение для {label} не было найдено.")


# Случай а) k=0
solution_a = solve_ivp(ode_system, t_span, initial_conditions, args=(0,), t_eval=t_eval, method='RK45')

# Случай б) k=C*rho_air*area/(2*mass)
k_value = C * rho_air * area / (2 * mass)
solution_b = solve_ivp(ode_system, t_span, initial_conditions, args=(k_value,), t_eval=t_eval, method='RK45')

# Вывод решений для solution_a и solution_b
print_solution(solution_a, "случай а (без сопротивления воздуха)")
print_solution(solution_b, "случай б (с сопротивлением воздуха)")

# Построение графиков
plt.figure(figsize=(15, 5))
# plt.figure(figsize=(10, 6))

# Траектория x1(t), x2(t)
plt.subplot(1, 2, 1)
plt.plot(solution_a.t, solution_a.y[0], label='x1(t) - без сопротивления воздуха')
plt.plot(solution_a.t, solution_a.y[1], label='x2(t) - без сопротивления воздуха')
plt.plot(solution_b.t, solution_b.y[0], label='x1(t) - с сопротивлением воздуха')
plt.plot(solution_b.t, solution_b.y[1], label='x2(t) - с сопротивлением воздуха')
plt.xlabel('Время (с)')
plt.ylabel('Позиция (м)')
plt.title('Траектории x1(t) и x2(t)')
plt.legend()

# Траектория x2(x1)
plt.subplot(1, 2, 2)
plt.plot(solution_a.y[0], solution_a.y[1], label='Без сопротивления воздуха')
plt.plot(solution_b.y[0], solution_b.y[1], label='С сопротивлением воздуха')
plt.xlabel('x1 (м)')
plt.ylabel('x2 (м)')
plt.title('Траектория x2(x1)')
plt.legend()

plt.tight_layout()
plt.show()
