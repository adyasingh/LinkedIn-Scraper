from bs4 import BeautifulSoup
import csv

emails=set()
soup = BeautifulSoup(open('temp.html'), "html.parser")

# EMAIL
for a in soup.find_all('a', href=True):
    if (a['href'].startswith("mailto",0)):
        # print ("Email:", a['href'][7:])
        emails.add(a['href'][7:])
        
#___________________________________________________________     
print(emails)

csvfile=open('emails.csv','a+', newline='')
writer_csv =csv.writer(csvfile)
# writer_csv.writerow(["Email"])

for mail in emails: 
    writer_csv.writerow([mail])
    
    