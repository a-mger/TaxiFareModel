# imports
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


class Trainer():
    def __init__(self, X, y):
        """
            X: pandas DataFrame
            y: pandas Series
        """
        self.pipeline = None
        self.X = X
        self.y = y


    def set_pipeline():
        '''returns a pipelined model'''
        dist_pipe = Pipeline([('dist_trans', DistanceTransformer()),
                            ('stdscaler', StandardScaler())])
        time_pipe = Pipeline([('time_enc', TimeFeaturesEncoder('pickup_datetime')),
                            ('ohe', OneHotEncoder(handle_unknown='ignore'))])
        preproc_pipe = ColumnTransformer([('distance', dist_pipe, [
            "pickup_latitude", "pickup_longitude", 'dropoff_latitude',
            'dropoff_longitude'
        ]), ('time', time_pipe, ['pickup_datetime'])],
                                        remainder="drop")
        pipe = Pipeline([('preproc', preproc_pipe),
                        ('linear_model', LinearRegression())])
        return pipe

    def run(self):
        """set and train the pipeline"""
        self.pipeline = set_pipeline()
        self.pipeline.fit(self.X, self.y)
        return self.pipeline

    def evaluate(self, X_test, y_test):
        """evaluates the pipeline on df_test and return the RMSE"""
        y_pred = self.pipeline.predict(X_test)
        rmse = np.sqrt(((y_pred - y_test)**2).mean())
        return rmse


if __name__ == "__main__":
    # get_data
    # clean data
    # set X and y
    # hold out
    # train
    # evaluate
    print(df.head())
