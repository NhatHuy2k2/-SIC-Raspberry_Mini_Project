import matplotlib.pyplot as plt

data {
    "x" [i for i in range(1, 10)],
    "y" [ii for i in range(1, 10)]
}

plt.plot(data["x"],data["y"],)
plt.show()