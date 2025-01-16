import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

# Clean data
#df = df[(df['value'] < df['value'].quantile(q=0.025)) | (df['value'] > df['value'].quantile(q=0.975))]
df = df.drop(df[(df['value'] < df['value'].quantile(q=0.025)) | (df['value'] > df['value'].quantile(q=0.975))].index)


def draw_line_plot():
    # Draw line plot

#    fig, ax = plt.subplots()
#    ax = df.plot(figsize=(16,4))
#    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
#    ax.set_xlabel("Date")
#    ax.set_ylabel("Page Views")

    fig, ax = plt.subplots()
    df.plot(figsize=(16,4), title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Views", ax=ax)



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    
    df.index = pd.to_datetime(df.index)

    df_bar = df.reset_index()

    df_bar["Year"] = df_bar['date'].dt.year
    df_bar["Month"] = df_bar['date'].dt.strftime("%B")

    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']

    fig, ax = plt.subplots()
    sns.barplot(data=df_bar, x='Year', y='value', hue="Month", errorbar=None, ax=ax, hue_order=month_order)
    #ax.legend(title='Months')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    handles, labels = plt.gca().get_legend_handles_labels()
    ordered_handles = [handles[i] for i in range(len(labels)) if labels[i] in month_order]
    ordered_labels = [labels[i] for i in range(len(labels)) if labels[i] in month_order]
    ordered_handles = sorted(ordered_handles, key=lambda x: month_order.index(x.get_label()))
    ordered_labels = sorted(ordered_labels, key=lambda x: month_order.index(x))
    plt.legend(handles=ordered_handles, labels=ordered_labels, title='Meses del Año')
    plt.legend(fontsize=9)
    #print("Todo OK")




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
#    df_box = df.copy()
#    df_box.reset_index(inplace=True)
#    df_box['year'] = [d.year for d in df_box.date]
#    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
    df = df.drop(df[(df['value'] < df['value'].quantile(q=0.025)) | (df['value'] > df['value'].quantile(q=0.975))].index)
    df.index = pd.to_datetime(df.index)

    df_box = df.reset_index()

    df_box["Year"] = df_box['date'].dt.year
    df_box["Month"] = df_box['date'].dt.strftime("%b")


    # Draw box plots (using Seaborn)

    fig, axs = plt.subplots(1, 2, figsize=(20,6))

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    month_order2 = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']

    sns.boxplot(data=df_box, x='Year', y='value', ax=axs[0])
    sns.boxplot(data=df_box, x='Month', y='value', ax=axs[1], order=month_order)

    axs[0].set_title("Year-wise Box Plot (Trend)")
    axs[0].set_ylabel("Page Views")
    axs[1].set_title("Month-wise Box Plot (Seasonality)")
    axs[1].set_ylabel("Page Views")

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
