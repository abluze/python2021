fileObject = open("/Users/raniasutton/Downloads/other files/coding/beaver.txt",'a')

#print(fileObject.readlines(200))
#print(fileObject.read())

fileObject.write("\nit is now about not being about beavers")

fileObject.close()