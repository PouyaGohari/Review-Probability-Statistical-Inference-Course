import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import skew, kurtosis
import seaborn as sns

file_path = 'prob10.csv'
df = pd.read_csv(file_path)
print(df.head())

column_names = df.columns.to_list()
print(column_names)

df_no_duplicates = df.drop_duplicates(keep=False)
print(df.shape, df_no_duplicates.shape)

df_cleaned = df_no_duplicates[~df_no_duplicates.astype(str).apply(lambda x : x.str.contains(r'\?')).any(axis=1)]
cleaned_file_path = 'cleaned_data.csv'
df_cleaned.to_csv(cleaned_file_path)
print(df_cleaned.shape, df_no_duplicates.shape)

df_cleaned['horsepower'] = df_cleaned['horsepower'].astype('int64')
df_cleaned['peak-rpm'] = df_cleaned['peak-rpm'].astype('int64')
df_cleaned['stroke'] = df_cleaned['stroke'].astype('float')
df_cleaned['bore'] = df_cleaned['bore'].astype('float')
df_cleaned['price'] = df_cleaned['price'].astype('int64')

print(df_cleaned.describe(include='all'))


make_cars_counts = df['make'].value_counts()
fig , axe = plt.subplots(figsize=(10,10))
colors = plt.cm.viridis(np.linspace(0, 1, len(make_cars_counts)))
make_cars_counts.plot(kind='bar', color=colors)
plt.title('Manufacturer Frequencies')
plt.xlabel('Manufacturer')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.show()


numeric_columns = df_cleaned.select_dtypes(include=['int64','float64','number']).columns
for col in numeric_columns:
    skewness = skew(df_cleaned[col])
    kurt = kurtosis(df_cleaned[col])
    print(f'skewness & kurtosis of {col} are:  {skewness, kurt}')



x_values = df_cleaned['engine-size']
y_values = df_cleaned['price'].astype('int64')
plt.title('scatter plot between engine-size, price')
plt.xlabel('engine-size')
plt.ylabel('price')
plt.scatter(x=x_values, y=y_values, alpha=0.7)
plt.show()



my_pair_plot = sns.pairplot(df_cleaned, vars=numeric_columns , diag_kind='kde')
for ax in my_pair_plot.axes.flat:
    ax.set_ylabel(ax.get_ylabel(), rotation=45)
plt.show()


correlation_between_variables = df_cleaned[numeric_columns].corr()
sns.heatmap(correlation_between_variables, annot=True)
plt.title('correlation matrix')
plt.show()

result = df_cleaned[numeric_columns].describe(percentiles=[0.25, 0.75])
print(result.loc['25%'])
print(result.loc['75%'])

iqr_calc = result.loc['75%'] - result.loc['25%']
print(iqr_calc)
print('whiskers: ')
for i,col in enumerate(numeric_columns):
    upper_wiskers = df_cleaned[df_cleaned[col] <= result.loc['75%'][i] + 1.5 * iqr_calc[i]][col].max()
    lower_wiskers = df_cleaned[df_cleaned[col] >= result.loc['25%'][i] - 1.5 * iqr_calc[i]][col].min()
    print(col + ': ', lower_wiskers, ',' ,upper_wiskers)


for col in numeric_columns:
    sns.boxplot(x=df_cleaned[col])
    plt.title(f'Box plot for {col}')
    plt.xlabel(col)
    plt.show()