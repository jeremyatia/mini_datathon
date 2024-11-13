# Presentation of the challenge
context_markdown = """
Manufacturing process feature selection and categorization
"""
content_markdown = """
Abstract: Data from a semi-conductor manufacturing process
    Data Set Characteristics: Multivariate
    Number of Instances: 1567
    Area: Computer
    Attribute Characteristics: Real
    Number of Attributes: 591
    Date Donated: 2008-11-19
    Associated Tasks: Classification, Causal-Discovery
    Missing Values? Yes
A complex modern semi-conductor manufacturing process is normally under consistent
surveillance via the monitoring of signals/variables collected from sensors and or
process measurement points. However, not all of these signals are equally valuable
in a specific monitoring system. The measured signals contain a combination of
useful information, irrelevant information as well as noise. It is often the case
that useful information is buried in the latter two. Engineers typically have a
much larger number of signals than are actually required. If we consider each type
of signal as a feature, then feature selection may be applied to identify the most
relevant signals. The Process Engineers may then use these signals to determine key
factors contributing to yield excursions downstream in the process. This will
enable an increase in process throughput, decreased time to learning and reduce the
per unit production costs.
"""
#------------------------------------------------------------------------------------------------------------------#

# Guide for the participants to get X_train, y_train and X_test
# The google link can be placed in your google drive => get the shared links and place them here.
data_instruction_commands = """
In order to get the data simply run the following command:
```python
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/secom/secom.data', sep=' ', header=None)
```
Please ask the admin in order to get the target and the random seed used for train/test split.
"""

# Target on test (hidden from the participants)
Y_TEST_GOOGLE_PUBLIC_LINK = 'https://drive.google.com/file/d/1-3X4eN_xk00GY4Bf6YU4mGtvQ8s_MDCQ/view?usp=sharing'
#------------------------------------------------------------------------------------------------------------------#

# Evaluation metric and content 
from sklearn.metrics import precision_recall_curve as prauc
GREATER_IS_BETTER = True  # example for ROC-AUC == True, for MSE == False, etc.
SKLEARN_SCORER = prauc
SKLEARN_ADDITIONAL_PARAMETERS = {}

evaluation_content = """
The predictions are evaluated according to the PR-AUC score.
You can get it using 
```python
from sklearn.metrics import average_precision_score as prauc
```
More details [here](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html).
"""
#------------------------------------------------------------------------------------------------------------------#

# leaderboard benchmark score, will be displayed to everyone
BENCHMARK_SCORE = 0.7
#------------------------------------------------------------------------------------------------------------------#