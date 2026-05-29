import matplotlib.pyplot as plt

def grafico_por_area(dataframe):

    contagem = dataframe["area"].value_counts()

    contagem.plot(kind="bar")
    
    plt.title("Inscritos por Área")
    plt.xlabel("Área")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.show()

