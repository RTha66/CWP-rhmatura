import sys
if len(sys.argv) != 3:
    print("none")
else:
    start_num = int(sys.argv[1])
    end_num = int(sys.argv[2])
    number_array = list(range(start_num, end_num + 1))
    print(number_array)