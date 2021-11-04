# file_name ='demo.txt'
# print(open(file_name))

##
file_name= 'demo2.txt'
# file_obj=open(file_name)
# con=file_obj.read()
# file_obj.close()
# print(con)

with open(file_name,encoding='utf-8') as file_obj:
    print(file_obj.read())
