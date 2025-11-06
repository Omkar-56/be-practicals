def f(x):
    return (x + 3)**2

def df(x):
    return 2*(x+3)

def grad(x, iter):
    lr = 0.1
    tolerance = 1e-6
    history = [x]

    for i in range(iter):
        x_new = x - lr * df(x)

        if abs(x_new - x) < tolerance:
            print(f"Converged after {i+1} iterations.")
            break

        x = x_new
        history.append(x)
        print(f"Iteration {i+1}: x = {x:.4f}, f(x) = {f(x):.4f}")

    print("Local minima at x =", x)
    print("Function value at local minima y =", f(x))

    return history



# def plot_grad(history):
#     plt.plot(history, [f(val) for val in history], marker='o')
#     plt.xlabel("x values")
#     plt.ylabel("f(x)")
#     plt.title("Gradient Descent Convergence")
#     plt.grid()
#     plt.show()


def main():
    history = grad(2, 25)
    # plot_grad(history)


if __name__ == "__main__":
    main()