from dataclasses import dataclass
import pandas as pd
import os


@dataclass
class Users:
    db_file: str = 'users.csv'
    current_path: str = os.path.abspath(os.path.dirname(__file__))

    def get_db(self):
        try:
            db = pd.read_csv(os.path.join(self.current_path, self.db_file))
        except FileNotFoundError:
            db = self.create_db()
        return db

    def create_db(self):
        db = pd.DataFrame(columns=['login', 'password'])
        db = db.append({'login': 'admin', 'password': 'password'}, ignore_index=True)
        db.to_csv(os.path.join(self.current_path, self.db_file), index=False)
        return db

    def exists(self, login, password):
        db = self.get_db()
        if db.loc[db.login == login].shape[0] != 0:
            if db.loc[db.login == login, 'password'].values[0] == password:
                return True
        return False
