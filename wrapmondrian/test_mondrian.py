from mondrian import *
import os
import numpy as np
import pandas as pd


def test1_mondrian_strict():
    data = [[6, 1, 'haha'],
            [6, 1, 'test'],
            [8, 2, 'haha'],
            [8, 2, 'test'],
            [4, 1, 'hha'],
            [4, 2, 'hha'],
            [4, 3, 'hha'],
            [4, 4, 'hha']]
    result, eval_r = mondrian(data, 2, False)
    print(result)
    print(abs(eval_r[0] - 100.0 / 12) < 0.05)


def test2_mondrian_strict():
    # data = pd.read_csv('data/adult.data', header=None)
    data = pd.read_csv('data/adult.data', header=None).iloc[:, [0, 1, 2]]
    print(data.head())
    data = np.array(data).tolist()
    print(data[:3])
    result, eval_r = mondrian(data, 2, False, [0, 1])
    print(result[:3])
    print(abs(eval_r[0] - 100.0 / 12) < 0.05)


if __name__ == '__main__':
    test1_mondrian_strict()
    test2_mondrian_strict()
