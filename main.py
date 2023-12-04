#This was a project to parse a URL list and validate
import re, os #we import regular expression and os (for deletion)
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|)' #the (sub)domain portion of the regex
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)#any trailing characters
with open ("urlTestLinks.txt") as file: #first thing we do here is open the file
  for line in file: #then we extract the URL's
    urls=re.findall(regex, line)#We regex the lines
    with open("goodurls.txt", "a") as fw:#we create our test file to make sure everything is working properly while stripping out the extra characters that we added : []' on the import additionally we print the output to the screen 
      for item in urls:   
        fw.writelines("%s\n" % item)
        print("%s\n" % item)
#we ask the user if they want to save the file,         
do_save = input("Do you want to save this file? Y or N ")
#The input is not validated here, since it wasn't asked for in the rubric
if do_save=='y':#If they answer in the affirmative 'y' we process the code below
  file_name = input("Please input a filename ") #we ask them to input their filename
  with open('goodurls.txt','r') as firstfile, open(file_name,'w') as secondfile: #we open our test file (goodurls.txt) and create a file that the user chose the name for   
      for line in firstfile: #we read from goodurls
             secondfile.write(line)#we write to $name that the user chose
      os.remove("goodurls.txt") #we delete our test doc in case you want to run the program again
      quit() #we quit the program 
else: #if they answer in the negative above 'n' we quit the program
  os.remove("goodurls.txt")#we delete our test doc in case you want to run the program again
  quit() #End it all
