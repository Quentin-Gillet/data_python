import matplotlib.pyplot as plt
import numpy as np

plt.rcdefaults()


def create_diagramme(names, numbers, graph_name):
    ind = np.arange(len(names))

    fig = plt.figure()
    rect = fig.patch

    ax1 = fig.add_axes([0.065, 0.2, 0.9, 0.55])
    rect = ax1.patch

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        label.set_fontsize(10)

    plt.bar(ind, numbers, align='center')
    plt.xticks(ind, names)
    plt.ylabel('Nombre de fois utilisés')
    plt.title(graph_name)

    plt.savefig(
        'C:\\Users\\Master_Fire\\Desktop\\data_python\\saveFig\\' + graph_name + '.png')
    plt.show()
    pass


def create_double_diagramme(name_1, name_2, numbers_1, numbers_2, real_name_1, real_name_2, graph_name):
    all_dates = []
    all_ind = []

    ind1 = []
    ind2 = []

    for x in range(1900, 2018):
        all_dates.append(str(x))
        pass

    for x in range(0, 118):
        all_ind.append(x)
        pass

    for x in name_1:
        if x in all_dates:
            ind1.append(all_dates.index(x))
        pass
    for x in name_2:
        if x in all_dates:
            ind2.append(all_dates.index(x))
        pass

    fig = plt.figure()
    var = fig.patch

    ax1 = fig.add_axes([0.065, 0.2, 0.9, 0.55])
    var = ax1.patch

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        label.set_fontsize(10)

    plt.plot(ind1, numbers_1, label=real_name_1)
    plt.plot(ind2, numbers_2, label=real_name_2)

    plt.legend(loc='best')

    plt.xticks(all_ind, all_dates)
    plt.ylabel('Nombre de fois utilisés')
    plt.title(graph_name)

    plt.savefig(
        'C:\\Users\\Master_Fire\\Desktop\\data_python\\saveFig\\' + graph_name + '.png')
    plt.show()
    pass
