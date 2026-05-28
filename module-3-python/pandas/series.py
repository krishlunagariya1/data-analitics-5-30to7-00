# series is an inbuild method
# series used to provide data of one column of data frame

import pandas as pd
age = [12, 14, 25, 16, 18, 90, 20]
age_series = pd.Series(age)
print(age_series)