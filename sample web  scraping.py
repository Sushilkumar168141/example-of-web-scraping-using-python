import datetime
import requests
import string
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
import winsound

#url="https://www.equitymaster.com/stock-markets/8/-220/50/bse-above-rs-20-gainers-over-1-year"
url = "https://www.equitymaster.com/stock-markets/8/-220/50/bse-above-rs-20-gainers-over-1-year"
page=requests.get(url).text
doc=lh.fromstring(page)
#print(doc)
soup = BeautifulSoup(page,'lxml')
#print(soup.prettify())
thead=soup.find_all('thead')
tbody=soup.find_all('tbody')


def write_data_head_f1(thead):
    write_data=[]
    if (len(thead)!=0):
        for row in thead[0].find_all('tr'):
            cells=row.find_all('th')
            if len(cells)==6:
                write_data.append(str((cells[0].find(text=True))))
                write_data.append(str((cells[1].find(text=True))))
                write_data.append(str((cells[2].find(text=True))))
                write_data.append(str((cells[3].find(text=True))))
                #write_data.append(str((cells[4].find(text=True))))
                write_data.append(str('52-WEEK High (Rs.)'))
                write_data.append(str('52-WEEK Low (Rs.)'))
                #write_data=write_data+"\n"
    '''
    for i in write_data:
        print(i)
    '''
    print(write_data)
    return (write_data)

def write_data_body_f1(tbody):
    write_data=[]
    i=0
    if(len(tbody)!=5):
        for row in tbody[5].find_all('tr'):
            cells=row.find_all('td')
            #write_data.append([])
            #print(len(cells))
            #input()
            if len(cells)==6:
                #print(cells)
                #input()
                write_data.append([])



                cell=cells[0].get_text()
                #cell=cell.replace(" ","")            
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)
                
                cell=cells[1].find(text=True)
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)

                cell=cells[2].get_text()
                cell=cell.replace(" ","")            
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)
                
                cell=cells[3].find(text=True)
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                write_data[i].append(cell)
                
                cell=cells[4].find(text=True)
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                cell_4=cell.split('\xa0/\xa0')
                write_data[i].append(str(cell_4[0]))
                write_data[i].append(str(cell_4[1]))
                i+=1
    '''
    for i  in write_data:
        print(write_data)
    '''
    return (write_data)
t=write_data_head_f1(thead)
#print(t)
s = write_data_body_f1(tbody)
#print(s)
for i in s:
    print(i)
