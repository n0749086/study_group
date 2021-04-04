# coding=utf-8

import csv
#from kim import solver
from kim2 import solver
from check_answer import print_result

def main():
    with open("test.csv") as f:
        test_data = csv.reader(f)
        next(test_data)     # skip header
        for row in test_data:   # read test line by line
            question = row[0]
            true_answer = row[1]
            answer = solver.solve(question)
            print_result(answer, true_answer)




if __name__ == '__main__':
    main()
