from csv import reader

# read bestseller data
def read_file():
    try:
        with open("../kaggle-datasets/bestsellers with categories.csv", "r", encoding="utf-8") as fi:
            csv_reader = reader(fi)
            for row in csv_reader:
                print(row)
                print(row[1])
                print(row[2])
    except Exception as e:
        print(e)

def main():
    read_file()

if __name__ == "__main__":
    main()