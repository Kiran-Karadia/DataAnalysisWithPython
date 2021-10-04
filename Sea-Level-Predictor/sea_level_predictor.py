import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    df.plot(x='Year', y='CSIRO Adjusted Sea Level', kind='scatter', ax=ax)


    # Create first line of best fit
    lbf1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x = range(df['Year'].min(), df['Year'].max() + 38)
    y = lbf1.intercept+lbf1.slope*(x)
    ax.plot(x, y)
    

    # Create second line of best fit
    predict_df = df.loc[df['Year'] >= 2000]
    lbf2 = linregress(x=predict_df['Year'], y=predict_df['CSIRO Adjusted Sea Level'])
    x = range(predict_df['Year'].min(), predict_df['Year'].max() + 38)
    y = lbf2.intercept+lbf2.slope*(x)
    ax.plot(x, y)

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()