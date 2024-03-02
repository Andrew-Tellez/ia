import matplotlib.pyplot as plt
import numpy as np


def newton_raphson(f, df, x, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f_value = f(x)
        f_prime_value = df(x)

        if f_prime_value == 0 :
            return None
        # Evitar división por cero
        if abs(f_prime_value) < 1e-6:
            raise ValueError("La derivada es muy pequeña, posible división por cero.")

        # Método de Newton-Raphson
        x = x - f_value / f_prime_value
        # Comprobar la convergencia
        if abs(f_value) < tol:
            return x
    raise ValueError(
        "El método de Newton-Raphson no converge después de {} iteraciones.".format(
            max_iter
        )
    )


if __name__ == "__main__":
    raices = []

    # Definir la función y su derivada
    def f(x):
        return np.sin(np.pi * x)

    def df(x):
        return np.pi * (np.cos(np.pi * x))

    # Calcular las raíces utilizando el método de Newton-Raphson
    valores_iniciales = range(-10, 11)
    for x0 in valores_iniciales:
        root_approximation = newton_raphson(f, df, x0)
        if root_approximation is not None:
             raices.append(round(root_approximation, 6))

    conjunto_raices = list(set(raices))
    print(conjunto_raices)

    x_valores = np.linspace(-10, 11)
    y_valores = f(x_valores)
    funcion = "f(x)=sin(pi * x)"
    plt.plot(x_valores, y_valores, label=funcion)
    plt.xlabel("x")

    plt.axhline(0, color="black", linestyle="--", linewidth=1.0)

    datos = {
        "x": conjunto_raices,
        "y": np.zeros(len(conjunto_raices))
    }
    plt.scatter("x", "y", color="red", marker="o" ,data=datos,label="raíces")

    for e in datos["x"]:
        plt.axvline(e,0, color="green", linestyle="--", linewidth=1.0)

    plt.ylabel("f(x)")
    plt.title("Grafico del metodo de newton raphson")
    plt.legend()
    plt.show()
