import numpy as np
import pandas as pd
import statsmodels.api as sm

"""
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.

"""

def linear_regression(features, values):
    """
    Perform linear regression given a data set with an arbitrary number of features.

    This can be the same code as in the lesson #3 exercise.
    """

    features = sm.add_constant(features)
    model = sm.OLS(values, features)
    results = model.fit()
    intercept = results.params[0]
    params = results.params[1:]
    return intercept, params

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.

    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    Your prediction should have a R^2 value of 0.40 or better.
    You need to experiment using various input features contained in the dataframe.
    We recommend that you don't use the EXITSn_hourly feature as an input to the
    linear model because we cannot use it as a predictor: we cannot use exits
    counts as a way to predict entry counts.

    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subet (~10%) of the data contained in
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with
    this exercise on your own computer, locally. If you do, you may want to complete Exercise
    8 using gradient descent, or limit your number of features to 10 or so, since ordinary
    least squares can be very slow for a large number of features.

    If you receive a "server has encountered an error" message, that means you are
    hitting the 30-second limit that's placed on running your program. Try using a
    smaller number of features.
    '''
    # Select Features (try different features!)
    features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']]

    # Add UNIT to features using dummy variables
    dummy_units = pd.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)

    # Values
    values = dataframe['ENTRIESn_hourly']

    # Get the numpy arrays
    features_array = features.values
    values_array = values.values

    # Perform linear regression
    intercept, params = linear_regression(features_array, values_array)

    predictions = intercept + np.dot(features_array, params)
    return predictions

def compute_r_squared(data, predictions):
    SST = ((data-np.mean(data))**2).sum()
    SSReg = ((predictions-np.mean(data))**2).sum()
    r_squared = SSReg / SST

    return r_squared

if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    predicted_values = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predicted_values)
    print r_squared

# import pandas as pd
# import numpy as np
# from ggplot import *
#
# def normalize_features(array):
#    """
#    Normalize the features in our data set.
#    """
#    array_normalized = (array-array.mean())/array.std()
#    mu = array.mean()
#    sigma = array.std()
#
#    return array_normalized, mu, sigma
#
# def compute_cost(features, values, theta):
#     """
#     Compute the cost function given a set of features / values, and the values for our thetas.
#
#     This should be the same code as the compute_cost function in the lesson #3 exercises. But
#     feel free to implement your own.
#     """
#
#     m = len(values)
#     sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
#     cost = sum_of_square_errors / (2*m)
#     return cost
#
# def gradient_descent(features, values, theta, alpha, num_iterations):
#     """
#     Perform gradient descent given a data set with an arbitrary number of features.
#
#     This is the same gradient descent code as in the lesson #3 exercises. But feel free
#     to implement your own.
#     """
#     m = len(values)
#     cost_history = []
#
#     for i in range(num_iterations):
#         predicted_values = np.dot(features, theta)
#         theta = theta - alpha/m*np.dot((predicted_values - values), features)
#         cost = compute_cost(features, values, theta)
#         cost_history.append(cost)
#     return theta, pd.Series(cost_history)
#
# def predictions(dataframe):
#     '''
#     The NYC turnstile data is stored in a pd dataframe called weather_turnstile.
#     Using the information stored in the dataframe, lets predict the ridership of
#     the NYC subway using linear regression with gradient descent.
#
#     You can look at information contained in the turnstile weather dataframe
#     at the link below:
#     https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
#
#     Your prediction should have a R^2 value of .40 or better.
#
#     Note: due to the memory and CPU limitation of our amazon EC2 instance, we will
#     give you a random subet (~15%) of the data contained in turnstile_data_master_with_weather.csv
#
#     If you receive a "server has encountered an error" message, that means you are hitting
#     the 30 second  limit that's placed on running your program. Try using a smaller number
#     for num_iterations if that's the case.
#
#     Or if you are using your own algorithm/modesl, see if you can optimize your code so it
#     runs faster.
#     '''
#
#     dummy_units = pd.get_dummies(dataframe['UNIT'], prefix='unit')
#     features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']].join(dummy_units)
#     values = dataframe[['ENTRIESn_hourly']]
#     m = len(values)
#
#     features, mu, sigma = normalize_features(features)
#
#     features['ones'] = np.ones(m)
#     features_array = np.array(features)
#     values_array = np.array(values).flatten()
#
#     #Set values for alpha, number of iterations.
#     alpha = 0.1 # please feel free to play with this value
#     num_iterations = 75 # please feel free to play with this value
#
#     #Initialize theta, perform gradient descent
#     theta_gradient_descent = np.zeros(len(features.columns))
#     theta_gradient_descent, cost_history = gradient_descent(features_array, values_array, theta_gradient_descent,
#                                                             alpha, num_iterations)
#     predictions = np.dot(features_array, theta_gradient_descent)
#
#     plot = plot_cost_history(alpha, cost_history)
#     return predictions, plot
#
# def plot_cost_history(alpha, cost_history):
#    """This function is for viewing the plot of your cost history.
#    You can run it by uncommenting this plot_cost_history(alpha,
#    cost_history) call in predictions.
#
#    If you want to run this locally, you should print the return value
#    from this function.
#    """
#    cost_df = pd.DataFrame({
#       'Cost_History': cost_history,
#       'Iteration': range(len(cost_history))
#    })
#    return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
#       geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha )
#
#
#
# def compute_r_squared(data, predictions):
#     SST = ((data-np.mean(data))**2).sum()
#     SSReg = ((predictions-np.mean(data))**2).sum()
#     r_squared = SSReg / SST
#
#     return r_squared
#
#
# if __name__ == "__main__":
#     input_filename = "turnstile_data_master_with_weather.csv"
#     turnstile_master = pd.read_csv(input_filename)
#     predicted_values, cost_plot = predictions(turnstile_master)
#     r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predicted_values)
#
#     print r_squared, cost_plot