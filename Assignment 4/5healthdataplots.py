'''
Description: Reads health_data.csv and creates scatter plots for different relationships using matplotlib.
'''
import pandas as pd
import matplotlib.pyplot as plt

def plot_data():
    try:
        # read csv file
        df = pd.read_csv("health_data.csv")

        # weight vs height
        plt.scatter(df['weight'], df['height'])
        plt.xlabel("Weight")
        plt.ylabel("Height")
        plt.title("Weight vs Height")
        plt.show()

        # age vs weight
        plt.scatter(df['age'], df['weight'])
        plt.xlabel("Age")
        plt.ylabel("Weight")
        plt.title("Age vs Weight")
        plt.show()

        # height vs age
        plt.scatter(df['height'], df['age'])
        plt.xlabel("Height")
        plt.ylabel("Age")
        plt.title("Height vs Age")
        plt.show()

        # gender vs height
        plt.scatter(df['gender'], df['height'])
        plt.xlabel("Gender")
        plt.ylabel("Height")
        plt.title("Gender vs Height")
        plt.show()

        # gender vs weight
        plt.scatter(df['gender'], df['weight'])
        plt.xlabel("Gender")
        plt.ylabel("Weight")
        plt.title("Gender vs Weight")
        plt.show()

    except FileNotFoundError:
        print("File not found!")

if __name__ == "__main__":
    plot_data()