import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date')

# Clean data
df_clean = df[ df['value'] >= df['value'].quantile(0.025) ]
df_clean = df_clean[ df['value'] <= df['value'].quantile(0.975) ]
df = df_clean.copy()
 

def draw_line_plot():
    # Draw line plot
    plt.figure()
    df.plot(color = "red", legend = False, title = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.ylabel("Page Views")
    plt.xlabel("Date")
    
    fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().reset_index()
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    df_bar.plot(kind='bar', figsize=(10,10))
    plt.legend(title="Months", labels=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    plt.ylabel("Average Page Views")
    plt.xlabel("Years")

    fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = pd.DatetimeIndex(df_box['date']).year
    df_box['month'] = pd.DatetimeIndex(df_box['date']).month

    # Draw box plots (using Seaborn)
    
    fig, axes = plt.subplots(1,2, figsize=(20,10))
    plot1 = sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    plot1.set_title("Year-wise Box Plot (Trend)")
    plot1.set_ylabel("Page Views")
    plot1.set_xlabel("Year")



    plot2 = sns.boxplot(data=df_box, x='month', y='value', ax=axes[1])
    plot2.set_title("Month-wise Box Plot (Seasonality)")
    plot2.set_ylabel("Page Views")
    plot2.set_xlabel("Month")
    plot2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    

    #fig = plt.gcf()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
