import data_saver.data_dump as dumper


def main():
    data = ["hello", "world."]
    file_path = "./data.pkl"

    result = dumper.save_data(data, file_path)
    if result:  # save success
        data_loaded = dumper.load_data(file_path)
        if data_loaded is not None: # load success
            print(' '.join(data_loaded))
    else:
        print("save failed.")


if __name__ == '__main__':
    main()
