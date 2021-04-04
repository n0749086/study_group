test_num = 1

def check_answer(answer, true_answer):
    result = False
    if answer == int(true_answer):
        result = True
    else:
        result = False
    return result

def print_result(answer, true_answer):
    global test_num
    if check_answer(answer, true_answer):
        print("test#{:2d}:pass".format(test_num))
    else:
        print("test#{:2d}:fail(answer->{}:true->{})".format(test_num, answer, true_answer))
    test_num += 1