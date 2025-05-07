def find_error(file_path):
    with open(file_path,'r') as file:
        lines= file.readlines()
        for line in lines:
            if "ERROR" in line:
                print(line)

find_error("./app.log")                