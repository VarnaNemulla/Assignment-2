#counting the words in the input.txt file

input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

content = {}
for line in input_file:
    output_file.write(line)
    new_l = line.split()
    for x in new_l:
        if(content.get(x)==None):
            content[x]=1
        else:
            content[x] = content[x] + 1
            
output_file.write("\n Word_Count : ")
for key, value in content.items(): 
        output_file.write('\n %s:%s\n' % (key, value))
input_file.close()
output_file.close()

