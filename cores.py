import seaborn as sns
import matplotlib.pyplot as plt

def exibir_paleta(paleta, nome_paleta):
    """ Exibe uma paleta de cores usando matplotlib. """
    plt.figure(figsize=(10, 2))
    sns.palplot(paleta)
    plt.title(nome_paleta)
    plt.axis('off')
    plt.show()

def gerar_paletas():
    """ Gera e exibe várias paletas de cores. """
    # Paletas de cores predefinidas do seaborn
    paletas = {
        'Deep': sns.color_palette('deep'),
        'Pastel': sns.color_palette('pastel'),
        'Dark': sns.color_palette('dark'),
        'Set1': sns.color_palette('Set1'),
        'Paired': sns.color_palette('Paired'),
        'Spectral': sns.color_palette('Spectral'),
        'husl': sns.husl_palette(8),
        'cubehelix': sns.cubehelix_palette(8, start=2, rot=0)
    }

    # Exibe cada paleta de cores
    for nome, paleta in paletas.items():
        exibir_paleta(paleta, nome)

if __name__ == "__main__":
    gerar_paletas()
