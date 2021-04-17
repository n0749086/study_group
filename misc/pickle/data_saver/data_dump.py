import os
import pickle


def save_data(data, path):
    """
    save data
    :param data: target data
    :param path: target file name
    :return:  save success / failed(file exists)
    """
    cond = False
    if not os.path.exists(path):
        with open(path, "wb") as f:
            pickle.dump(data, f)
        cond = True

    return cond


def load_data(path):
    """
    load data
    :param path: target path
    :return: loaded data(None-> load failed)
    """
    data = None
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = pickle.load(f)

    return data
