df[['mean', 'stdev']].plot(grid=True, kind='line', subplots=True)
plt.legend(loc='upper right'); plt.savefig('dframe.png')

df.to_json('data.json') # save dataframe in json format
