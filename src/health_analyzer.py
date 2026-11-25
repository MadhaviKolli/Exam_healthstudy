import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class HealthAnalyzer:

    def __init__(self, df):   

        """
        initialize the analyzer
        
        parameters
        --------------
        df : pandas.DataFrame
        """

        self.df = df

    def calculate_mean_bp(self):

        """
        Calculate mean of systolic blood pressure

        returns
        --------
        float
        """

        return self.df["systolic_bp"].mean()       

    def disease_rate(self):

        """
        Calculate mean of disease prevalance

        returns
        --------
        float
        """

        return self.df["disease"].mean()

    def plot_bp_vs_age(self):
        """
        plot graph bloodpressure vs age
        """

        plt.figure(figsize=(8,6))

        sns.regplot(
            data=self.df,
            x = "age",
            y="systolic_bp"
        )

        plt.title("Blood Pressure vs age")
        plt.show()


    def plot_disease_by_gender(self):

        """
        plot disease occurence by gender
        """

        disease_gender = self.df.groupby(
            ["sex", "disease"]
        ).size().unstack()

        disease_gender.plot(
            kind="bar",
            figsize=(8,6)
        )

        plt.title("Disease occurence by Gender")
        plt.ylabel("count")
        plt.show()

        

