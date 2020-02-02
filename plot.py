import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# create vars for csv files
church_data = 'church.csv'
home_data = 'home.csv'

# create DataFrames
church_df = pd.read_csv(church_data)
home_df = pd.read_csv(home_data)

# define function to build scatterplot
def scatterplot(temp, y_var):
    sns.scatterplot(x = temp, y = y_var)
    plt.show()

# Show plots
print('CO2 Home')
scatterplot(home_df['Temperature'], home_df['CO2'])
print('CO2 Church')
scatterplot(church_df['Temperature'], church_df['CO2'])

print('VOC Home')
scatterplot(home_df['Temperature'], home_df['VOC'])
print('VOC Church')
scatterplot(church_df['Temperature'], church_df['VOC'])
