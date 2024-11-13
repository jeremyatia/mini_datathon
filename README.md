[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[HuggingFace space](https://huggingface.co/spaces/jeremyadd/mini_datathon)

![](mini_datathon.gif)

# Mini Datathon

This datathon platform is fully developped in python using *streamlit* with very few lines of code!

As written in the title, it is designed for *small datathon* (but can easily scale) and the scripts are easy to understand.

## Installation

1) Easy way => using docker hub:
`docker pull spotep/mini_datathon:latest`

2) Alternative way => clone the repo into your server:
`git clone mini_datathon; cd mini_datathon`

## Usage

You need 3 simple steps to setup your mini hackathon:

1) Edit the password of the **admin** user in [users.csv](users.csv) and the login & passwords for the participants 
2) Edit the [config.py](config.py) file\
    a) The **presentation** & the **context** of the challenge \
    b) The **data content** and `X_train`, `y_train`, `X_test` & `y_test` that you can upload on google drive and just **share the links**. \
    c) The **evaluation metric** & **benchmark score**
3) Run the scripts\
    a) If you installed it the _alternative way_: `streamlit run main.py` \
    b) If you pulled the docker image, just **build** and **run** the container.

Please do not forget to notify the participants that the submission file need to be a csv **ordered the same way as given 
in `y_train`**.

_Ps: anytime the admin user has the possibility to **pause** the challenge, in that case the participants won't be able to upload their submissions._

## Example

An example version of the code is deployed on heroku here: [web app](https://minidatathon.herokuapp.com/)

In the deployed version, we have the [UCI Secom](https://archive.ics.uci.edu/ml/datasets/SECOM)
imbalanced dataset (binary classification) and evaluated by the [PR-AUC score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score):

in the [config.py](config.py) file you would need to fill the following parameters:

- `GREATER_IS_BETTER = True`
- `SKLEARN_SCORER = average_precision_score`
- `SKLEARN_ADDITIONAL_PARAMETERS = {'average': 'micro'}`
- upload the relevant data the your Google Drive & share the links.

## Behind the scenes
### Databases
The platform needs only 2 components to be saved:
#### The leaderboard
The leaderboard is in fact a csv file that is being updated everytime a user submit predictions. 
The csv file contains 4 columns: 
- _id_: the login  of the team
- _score_: the **best** score of the team
- _nb\_submissions_: the number of submissions the team uploads
- _rank_: the live rank of the team

We will have only 1 row per team since only the best score is being saved.

By default, a benchmark score is pushed to the leaderboard:

| id        | score |
|-----------|-------|
| benchmark | 0.6   |

For more details, please refer to the script [leaderboard](leaderboard.py).

#### The users
Like the leaderboard, it is a csv file.
It is supposed to be defined by the admin of the competition.
It contains 2 columns: 
- login
- password

A default user is created at first to begin to play with the platform:

| login     | password |
|-----------|----------|
| admin     | password |

In order to add new participants, simply add rows to the current users.csv file.

For more details, please refer to the script [users](users.py).

## Next steps

- [ ] allow to have a *private* and *public* leaderboard like it is done on kaggle.com
- [ ] allow to connect using oauth


## License
MIT License [here](LICENSE).

## Credits
We could not find an easy implementation for our yearly internal hackathon at Intel.
The idea originally came from my dear devops coworker [Elhay Efrat](https://github.com/shdowofdeath)
and I took the responsability to develop it.

If you like this project, let me know by [buying me a coffee](https://www.buymeacoffee.com/jeremyatia) :)

<a href="https://www.buymeacoffee.com/jeremyatia" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 100px !important;width: 300px !important;" ></a>
