from dataclasses import dataclass
import numpy as np
import pandas as pd
import os


@dataclass
class LeaderBoard:
    benchmark_score: int = 0.6
    db_file: str = 'leaderboard.csv'
    current_path: str = os.path.abspath(os.path.dirname(__file__))

    def get(self):
        try:
            leaderboard = pd.read_csv(os.path.join(self.current_path, self.db_file))
        except FileNotFoundError:
            leaderboard = self.create()
        return leaderboard

    def create(self):
        ldb = pd.DataFrame(columns=['id', 'score'], index=[0])
        ldb.loc[0, 'id'] = 'benchmark'
        ldb.loc[0, 'score'] = self.benchmark_score
        ldb.to_csv(os.path.join(self.current_path, self.db_file), index=False)
        return ldb

    def edit(self, leaderboard, id, score):
        new_lb = leaderboard.copy()
        if new_lb[new_lb.id == id].shape[0] == 0:
            new_lb = new_lb.append({'id': id, 'score': score}, ignore_index=True)
        else:
            current_score = new_lb.loc[new_lb.id == id, 'score'].values[0]
            if score > current_score:
                new_lb.loc[new_lb.id == id, 'score'] = score
        new_lb.to_csv(os.path.join(self.current_path, self.db_file),  index=False)
        return new_lb

    @staticmethod
    def show(leaderboard, ascending):
        new_lb = leaderboard.sort_values('score', ascending=ascending)
        new_lb['rank'] = np.arange(1, new_lb.shape[0] + 1)
        return new_lb
