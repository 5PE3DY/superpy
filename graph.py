import matplotlib.pyplot as plt

def get_graph(x_list, y_list, type):
    plt.bar(x_list, y_list, zorder=3)
    plt.xticks(rotation=90)
    plt.xlabel("Days")
    plt.ylabel(type)
    plt.title(f"{type} over last week")
    plt.tight_layout()
    plt.grid(zorder=0)
    plt.savefig(f"{type}_graph.png")
    plt.show()