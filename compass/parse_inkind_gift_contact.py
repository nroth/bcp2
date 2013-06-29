#Make sure to set the DJANGO_SETTINGS_MODULE enviornment variable to the appropriate settings python file

import csv
from finances.models import Business

donor_data = []

with open('in_kind_gift_contact.csv', 'U') as f:
    reader = csv.reader(f)
    for row in reader:
        donor_data.append(row)

#0  Business name 
#1  Stret address
#2  City
#3  State
#4  Zip
#5  First name
#6  Last name
#7  Job title
#8  Gift asked
#9  Gift received
#10 Notes

for bs in donor_data:
    b = Business(name = bs[0], street=bs[1], city = bs[2], state = bs[3], postcode = bs[4], contact_name = bs[5] + " " + bs[6], contact_title = bs[7], comment = bs[10] )
    
    b.save()


