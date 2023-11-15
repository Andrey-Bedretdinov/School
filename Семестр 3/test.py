import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('MacOSX')

rho_air = 1.2041
C = 0.47
rho_projectile = 7200
d = 0.1
v0 = 1000
alpha = 45

alpha_rad = np.radians(alpha)

area = np.pi * (d / 2) ** 2

volume = (4 / 3) * np.pi * (d / 2) ** 3
mass = rho_projectile * volume

g = 9.81

x01 = 0
x02 = 0
v01 = abs(v0) * np.cos(alpha_rad)
v02 = abs(v0) * np.sin(alpha_rad)
initial_conditions = [x01, x02, v01, v02]

t0 = 0
tm = 150
t_eval = np.arange(t0, tm, 1)


def ode_system(t, y, k):
    x1, x2, v1, v2 = y
    dx1dt = v1
    dx2dt = v2
    dv1dt = -k * np.sqrt(v1 ** 2 + v2 ** 2) * v1
    dv2dt = -k * np.sqrt(v1 ** 2 + v2 ** 2) * v2 - g
    return [dx1dt, dx2dt, dv1dt, dv2dt]


def runge_kutta_4(ode_func, t_span, y0, h, k):
    t0, tf = t_span
    t_values = np.arange(t0, tf, h)
    y_values = np.zeros((len(y0), len(t_values)))

    y_values[:, 0] = y0

    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[:, i - 1]

        k1 = h * np.array(ode_func(t, y, k))
        k2 = h * np.array(ode_func(t + h / 2, y + k1 / 2, k))
        k3 = h * np.array(ode_func(t + h / 2, y + k2 / 2, k))
        k4 = h * np.array(ode_func(t + h, y + k3, k))

        y_values[:, i] = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t_values, y_values


h = 1
k0 = 0
t_a, solution_a = runge_kutta_4(ode_system, [t0, tm], initial_conditions, h, k0)

k1 = C * rho_air * area / (2 * mass)
t_b, solution_b = runge_kutta_4(ode_system, [t0, tm], initial_conditions, h, k1)


def calculate_flight_metrics(t_values, y_values):
    index_touchdown = np.where(y_values[1] <= -0.00001)[0][0] if np.any(y_values[1] <= -0.00001) else -1
    max_distance = y_values[0][index_touchdown] if index_touchdown != -1 else y_values[0][-1]
    max_height = np.max(y_values[1])
    flight_time = t_values[index_touchdown] if index_touchdown != -1 else t_values[-1]
    return max_distance, max_height, flight_time


max_distance_a, max_height_a, flight_time_a = calculate_flight_metrics(t_a, solution_a)
max_distance_b, max_height_b, flight_time_b = calculate_flight_metrics(t_b, solution_b)

print("Без сопротивления воздуха:")
print(f"Максимальная дальность: {max_distance_a} м")
print(f"Максимальная высота: {max_height_a} м")
print(f"Время полета: {flight_time_a} с")

print("\nС сопротивлением воздуха:")
print(f"Максимальная дальность: {max_distance_b} м")
print(f"Максимальная высота: {max_height_b} м")
print(f"Время полета: {flight_time_b} с")

plt.figure(figsize=(10, 6))

plt.plot(solution_a[0], solution_a[1], label='Без сопротивления воздуха')
plt.plot(solution_b[0], solution_b[1], label='С сопротивлением воздуха')
plt.xlabel('x1 (м)')
plt.ylabel('x2 (м)')
plt.title('Траектория x2(x1)')
plt.legend()

plt.tight_layout()
plt.show()
