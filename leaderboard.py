from dataclasses import dataclass
from config import BENCHMARK_SCORE, GREATER_IS_BETTER
import numpy as np
import pandas as pd
import os


@dataclass
class LeaderBoard:
    benchmark_score: float = BENCHMARK_SCORE
    db_file: str = 'leaderboard.csv'
    current_path: str = os.path.abspath(os.path.dirname(__file__))

    def get(self):
        try:
            leaderboard = pd.read_csv(os.path.join(self.current_path, self.db_file))
        except FileNotFoundError:
            leaderboard = self.create()
        return leaderboard

    def create(self):
        ldb = pd.DataFrame(columns=['id', 'score', 'nb_submissions'], index=[0])
        ldb.loc[0, 'id'] = 'benchmark'
        ldb.loc[0, 'score'] = self.benchmark_score
        ldb.loc[0, 'nb_submissions'] = 1
        ldb.to_csv(os.path.join(self.current_path, self.db_file), index=False)
        return ldb

    def edit(self, leaderboard: pd.DataFrame, id: str, score: float) -> pd.DataFrame:
        new_lb = leaderboard.copy()
        if new_lb[new_lb.id == id].shape[0] == 0:
            new_lb = new_lb.append({'id': id, 'score': score, 'nb_submissions': 1}, ignore_index=True)
        else:
            current_score = new_lb.loc[new_lb.id == id, 'score'].values[0]
            if self.compare_score(score, current_score, greater_is_better=GREATER_IS_BETTER):
                new_lb.loc[new_lb.id == id, 'score'] = score
        new_lb.loc[new_lb.id == id, 'nb_submissions'] += 1
        new_lb.to_csv(os.path.join(self.current_path, self.db_file),  index=False)
        return new_lb

    @staticmethod
    def show(leaderboard: pd.DataFrame, ascending: bool) -> pd.DataFrame:
        new_lb = leaderboard.sort_values('score', ascending=ascending, ignore_index=True)
        new_lb['rank'] = np.arange(1, new_lb.shape[0] + 1)
        return new_lb

    @staticmethod
    def compare_score(new_score: float, current_score: float, greater_is_better: bool=True) -> bool:
        if greater_is_better:
            return new_score > current_score
        else:
            return new_score < current_score
        