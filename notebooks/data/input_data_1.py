from sklearn.datasets import make_blobs
import numpy as np


class DatasetCreator:
    @staticmethod
    def create_blob_dataset() -> dict:
        n_samples_1 = 1000
        n_samples_2 = 100
        centers = [[0.0, 0.0], [2.0, 2.0]]
        cluster_std = [2.0, 1.0]

        X, y = make_blobs(n_samples=[n_samples_1, n_samples_2],
                          centers=centers,
                          cluster_std=cluster_std,
                          random_state=0,
                          shuffle=False)

        return {'X': X, 'y': y}



    @staticmethod
    def create_points_dataset() -> dict:
        np.random.seed(0)
        n_points_per_cluster = 30000
        c1 = [-6, -2] + 0.7 * np.random.randn(n_points_per_cluster, 2)
        c2 = [-2, 2] + 0.3 * np.random.randn(n_points_per_cluster, 2)
        c3 = [1, -2] + 0.2 * np.random.randn(n_points_per_cluster, 2)
        c4 = [4, 4] + 0.1 * np.random.randn(n_points_per_cluster, 2)
        c5 = [5, 0] + 1.4 * np.random.randn(n_points_per_cluster, 2)
        c6 = [5, 6] + 2.0 * np.random.randn(n_points_per_cluster, 2)
        x = np.vstack((c1, c2, c3, c4, c5, c6))
        return {'X': x}


