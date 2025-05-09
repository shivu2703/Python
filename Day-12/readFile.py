def readFile(file_path):
    with open(file_path,'r') as file:
        for line in file:
            print(line.strip())

def writeFile(file_path, text_to_write):
    with open(file_path,'w') as file:
        file.write(text_to_write , "\n")
        
def appendFile(file_path, text_to_write):
    with open(file_path,'a') as file:
        file.write(text_to_write , "\n")


# readFile("./app.log")
# writeFile("./app.log", "This is the new line")
appendFile("./app.log", "This is the new line")