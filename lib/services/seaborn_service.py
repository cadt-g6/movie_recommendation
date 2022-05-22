import seaborn as sns
import pandas as pd


class SeabornService:
    def __init__(self, x: pd.Series, y: pd.Series, file_name: str):
        self.x = x
        self.y = y
        self.file_name = file_name

    def render(self):
        ax = sns.barplot(x=self.x, y=self.y)
        ax.bar_label(ax.containers[0])

        figure = ax.get_figure()
        figure.savefig("../assets/{}.png".format(self.file_name), bbox_inches='tight')

        return ax
