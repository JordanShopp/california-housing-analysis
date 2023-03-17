import pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport seaborn as snsfrom sklearn.decomposition import PCAimport osimport sklearn.linear_model as lmfrom matplotlib.pylab import figure, subplot, plot, xlabel, ylabel, hist, showDATA_PATH = '../../data'housing_df_raw = pd.read_csv(os.path.join(DATA_PATH, 'housing.csv'))housing_df = housing_df_raw.dropna()housing_df_numeric = housing_df.iloc[:, :housing_df.shape[1] - 1]# m = entries, n = attributesN, M = housing_df_numeric.shape# normalize data#df_normalized=(housing_df_numeric - housing_df_numeric.mean()) / housing_df_numeric.std()X = housing_df_numeric.values# Split dataset into features and target vectormed_inc_index = 7y = X[:,med_inc_index]X_cols = list(range(0,med_inc_index)) + list(range(med_inc_index+1,M))X = X[:,X_cols]#adds a ones matrix to Xones_matrix = np.ones((N,1))X = np.asarray(np.bmat('ones_matrix, X'))#adds rooms, bedrooms and people per houseroom_idx =3house_idx = 6bedroom_idx = 4pop_idx=5X_rooms_per_house = (X[:,room_idx]/X[:,house_idx]).reshape(-1,1)X_bedrooms_per_house = (X[:,bedroom_idx]/X[:,house_idx]).reshape(-1,1)X_ppl_per_house = (X[:,pop_idx]/X[:,house_idx]).reshape(-1,1)X = np.asarray(np.bmat('X, X_rooms_per_house, X_bedrooms_per_house, X_ppl_per_house'))#adds rooms, bedrooms, and houses per person X_rooms_per_ppl = (X[:,room_idx]/X[:,pop_idx]).reshape(-1,1)X_bedrooms_per_ppl = (X[:,bedroom_idx]/X[:,pop_idx]).reshape(-1,1)X_houses_per_ppl = (X[:,house_idx]/X[:,pop_idx]).reshape(-1,1)X = np.asarray(np.bmat('X, X_rooms_per_ppl, X_bedrooms_per_ppl, X_houses_per_ppl'))# Fit ordinary least squares regression modelmodel = lm.LinearRegression()model.fit(X,y)# Predict alcohol contenty_est = model.predict(X)residual = y_est-y# Display scatter plotfigure()subplot(2,1,1)plot(y, y_est, '.')xlabel('Median Income (true)'); ylabel('Median Income (estimated)');subplot(2,1,2)hist(residual,40)show()def mse(y_true, y_est):    summation = 0    n = len(y_true)    for i in range (0,n):  #looping through each element of the list        difference = y_true[i] - y_est[i]  #finding the difference between observed and predicted value        squared_difference = difference**2  #taking square of the differene         summation = summation + squared_difference  #taking a sum of all the differences    MSE = summation/n    return(MSE)    print('\nThe error in the training data is : {0:.4f}'.format(mse(y,y_est)))#The error w/o any manipulation is 1.226, witbh j rooms, bedrooms, #and ppl per house it is .9276, and if we add the same measures per person, #it goes down to .8987#Oow wow added ones line and it dropped again                    