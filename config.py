# Presentation of the challenge
context_markdown = """
Small introduction about the challenge
"""
content_markdown = """
Description about the problem

Task 

Number of features

etc.
"""
#------------------------------------------------------------------------------------------------------------------#

# Guide for the participants to get X_train, y_train and X_test
# The google link can be placed in your google drive => get the shared links and place them here.
data_instruction_commands = """
```python
import pandas as pd

url='https://drive.google.com/file/d/1-4YpXkd2kIOM5viSRw8g7oOQm8sicciB/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
y_train = pd.read_csv(url, index_col=0)

url='https://drive.google.com/file/d/1-7VK3dNry2-AYnfRsxMWsOKhHHMTN_ZA/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
test_indices = pd.read_csv(url, index_col=0)
```
"""

# Target on test (hidden from the participants)
Y_TEST_GOOGLE_PUBLIC_LINK = 'https://drive.google.com/file/d/1-3X4eN_xk00GY4Bf6YU4mGtvQ8s_MDCQ/view?usp=sharing'
#------------------------------------------------------------------------------------------------------------------#

# Evaluation metric and content 
from sklearn.metrics import mean_squared_error as rmse
GREATER_IS_BETTER = False  # example for ROC-AUC == True, for MSE == False, etc.
SKLEARN_SCORER = rmse
SKLEARN_ADDITIONAL_PARAMETERS = {'squared': False}

evaluation_content = """
The predictions are evaluated according to the 'evaluation your choose'.

You can get it using 
```python
from sklearn.metrics import mean_squared_error as mse

mse(y_train, y_pred_train, squared=False)
```
More details [here](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html).
"""
#------------------------------------------------------------------------------------------------------------------#

# leaderboard benchmark score, will be displayed to everyone
BENCHMARK_SCORE = 5859.21
#------------------------------------------------------------------------------------------------------------------#