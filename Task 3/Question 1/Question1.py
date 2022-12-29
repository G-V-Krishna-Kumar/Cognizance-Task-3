import csv


def read_text_file(file_name):
    with open(file_name, "r") as read_object:
        content = read_object.read()
        read_object.close()
        
    new_content = ''
    for i in range(len(content)):
        if ((content[i-1].isalpha() and content[i-1] != '.') and content[i].isdigit() and ((content[i+1].isalpha() or content[i+1].isdigit()) and content[i+1] !=  '.')):
            new_content += ('\n' + content[i])
            continue
        if ((content[i-1].isdigit() and content[i].isalpha() and content[i+1].isalpha()) or (content[i-1].isalpha() and content[i].isdigit() and content[i+1] == '.')):       
            new_content += (',' + content[i])
        else:
            new_content += content[i]

    return new_content


def write_csv(file_name, new_content):
    with open(file_name, "w", newline="") as write_object:
        writer_object = csv.writer(write_object)
        writer_object.writerows(new_content)
    write_object.close()



new_content = read_text_file("onelinefile.txt")
a = new_content.split("\n")
lst = []
for i in a:
    lst.append([i])
write_csv("Filename2.csv", lst)
    
