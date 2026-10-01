import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D  # Necesario para la proyección 3D

# Función objetivo: f(x, y) = (x-2)^2 + (y+2)^2
def objective(w):
    x, y = w[0], w[1]
    return (x - 2)**2 + (y + 2)**2

# Gradiente de la función objetivo
def grad_f(w):
    x, y = w[0], w[1]
    df_dx = 2 * (x - 2)
    df_dy = 2 * (y + 2)
    return np.array([df_dx, df_dy])

# Parámetros de la optimización
eta = 0.02            # Tasa de aprendizaje
num_iterations = 200  # Número de iteraciones (puedes ajustar este valor)
w = np.array([0.0, 0.0])  # Inicialización en (0, 0)

# Lista para almacenar el recorrido (trayectoria)
trajectory = [w.copy()]

# Bucle de descenso de gradiente
for i in range(num_iterations):
    g = grad_f(w)
    w = w - eta * g
    trajectory.append(w.copy())

trajectory = np.array(trajectory)

# Configuración del gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear una malla para graficar la superficie de la función
x_range = np.linspace(-1, 5, 50)
y_range = np.linspace(-5, 3, 50)
X, Y = np.meshgrid(x_range, y_range)
Z = (X - 2)**2 + (Y + 1)**2

# Graficar la superficie con transparencia
ax.plot_surface(X, Y, Z, alpha=0.5, cmap='viridis')

# Configurar etiquetas y límites
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.set_title('Animación del Descenso de Gradiente')
ax.set_xlim(-1, 5)
ax.set_ylim(-5, 3)
ax.set_zlim(0, np.max(Z))

# Inicializar objetos para la animación: línea y punto actual
line, = ax.plot([], [], [], 'r-', lw=2, label='Trayectoria')
point, = ax.plot([], [], [], 'ko', markersize=5)

# Función de inicialización de la animación
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return line, point

# Función que se ejecuta en cada frame de la animación
def animate(i):
    xs = trajectory[:i+1, 0]
    ys = trajectory[:i+1, 1]
    zs = (xs - 2)**2 + (ys + 1)**2
    line.set_data(xs, ys)
    line.set_3d_properties(zs)
    point.set_data(xs[-1:], ys[-1:])
    point.set_3d_properties(zs[-1:])
    return line, point

# Crear la animación
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(trajectory), interval=20, blit=False)

plt.legend()

# Guardar la animación en un archivo MP4
# Se utiliza el writer 'ffmpeg' con 30 fps
anim.save('descenso_gradiente-s.mp4', writer='ffmpeg', fps=30)

plt.show()