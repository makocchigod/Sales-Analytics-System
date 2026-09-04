import matplotlib.pyplot as plt

def create_plot(df, column, x_label):
    df[column].plot(kind='line', color='black', ylabel=column, xlabel=x_label)
    plt.show()
