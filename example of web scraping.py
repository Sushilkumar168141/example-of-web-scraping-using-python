import datetime
import requests
import string
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
import winsound

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

    return (write_data)




def write_data_body_f1(tbody):
    write_data=[]
    i=0
    if(len(tbody)!=5):
        for row in tbody[5].find_all('tr'):
            cells=row.find_all('td')
            if len(cells)==6:
                write_data.append([])
                cell=cells[0].get_text()
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
    return(write_data)            



def write_data_text_f1(thead1,tbody1):
    write_data="\n"
    write_data=write_data+('='.ljust(185,"="))+"\n"
    if (len(thead1)!=0):
        write_data=write_data+(thead1[0].ljust(50," "))+' | '+thead1[1].ljust(30," ")+" | "+thead1[2].ljust(30," ")+" | "+thead1[3].ljust(11," ")+" | "+thead1[4].ljust(20," ")+" | "+thead1[5].ljust(20," ")+" | "+"\n"
    else:
        write_data=write_data+"Sorry! No scrip found in this category.\n"
    write_data=write_data+('='.ljust(185,"="))+"\n"
    if(len(tbody1)!=0):
        for i in range(len(tbody1)):
            write_data=write_data+tbody1[i][0].ljust(50," ")+" | "
                
            for j in range(1,len(tbody1[i])):
                write_data=write_data+(tbody1[i][j].replace(",","")).rjust(11," ")+" | "
            write_data=write_data+"\n"
    else:
        write_data=write_data+"Sorry! No scrip found in this category.\n"
    write_data=write_data+('='.ljust(185,"="))+"\n\n\n"
    return(write_data)

def url_data_f1(thead,tbody):
    thead1=(write_data_head_f1(thead))
    tbody1=(write_data_body_f1(tbody))
    return(write_data_text_f1(thead1,tbody1))

def url_beautify_f1(url):
    page=requests.get(url).text
    doc=lh.fromstring(page)
    soup = BeautifulSoup(page,'lxml')
    thead=soup.find_all('thead')
    tbody=soup.find_all('tbody')
    return(url_data_f1(thead,tbody))

url_1="https://www.equitymaster.com/stock-markets/8/-220/50/bse-above-rs-20-gainers-over-1-year"


################################################################


def write_data_head_f2(thead):
    write_data=[]
    if (len(thead)!=0):
        for row in thead[0].find_all('tr'):
            cells=row.find_all('th')
            if len(cells)==7:
                write_data.append(str((cells[0].find(text=True))))
                write_data.append(str((cells[1].find(text=True))))
                write_data.append(str((cells[2].find(text=True))))
                write_data.append(str((cells[3].find(text=True))))
                write_data.append(str('DAY\'S High (Rs)'))
                write_data.append(str('DAY\'S Low (Rs)'))
                write_data.append(str('52-WEEK High (Rs.)'))
                write_data.append(str('52-WEEK Low (Rs.)'))
        return (write_data)

    else:
        return ()


def write_data_body_f2(tbody):
    write_data=[]
    i=0
    if (len(tbody)!=5):
        
        for row in tbody[5].find_all('tr'):
            cells=row.find_all('td')
            if len(cells)==7:
                write_data.append([])

                cell=cells[0].get_text()   
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

                cell=cells[5].find(text=True)
                cell=cell.replace(" ","")
                cell=cell.replace("\r","")
                cell=cell.replace("\n","")
                cell_4=cell.split('\xa0/\xa0')
                write_data[i].append(str(cell_4[0]))
                write_data[i].append(str(cell_4[1]))

                i+=1
        return(write_data)            
    else:
        return()





def write_data_text_f2(thead1,tbody1):
    write_data="\n"
    write_data=write_data+('='.ljust(185,"="))+"\n"
    if (len(thead1)!=0):
        write_data=write_data+(thead1[0].ljust(50," "))+' | '+thead1[1].ljust(11," ")+" | "+thead1[2].ljust(11," ")+" | "+thead1[3].ljust(15," ")+" | "+thead1[4].ljust(16," ")+" | "+thead1[5].ljust(16," ")+" | "+thead1[6].ljust(20," ")+" | "+thead1[7].ljust(20," ")+" | "+"\n"
    else:
        write_data=write_data+"Sorry! No scrip found in this category.\n"
    write_data=write_data+('='.ljust(185,"="))+"\n"
    if ((len(tbody1))!=0):
       for i in range(len(tbody1)):
            write_data=write_data+tbody1[i][0].ljust(50," ")+" | "
            for j in range(1,len(tbody1[i])):
                write_data=write_data+(tbody1[i][j].replace(",","")).rjust(11," ")+" | " 
            write_data=write_data+"\n"
    else:
        write_data=write_data+"Sorry! No scrip found in this category.\n"
    write_data=write_data+('='.ljust(185,"="))+"\n\n\n"
    return(write_data)

def url_data_f2(thead,tbody):
    thead1=(write_data_head_f2(thead))
    tbody1=(write_data_body_f2(tbody))
    return(write_data_text_f2(thead1,tbody1))

def url_beautify_f2(url):
    
    page=requests.get(url).text
    doc=lh.fromstring(page)
    soup = BeautifulSoup(page,'lxml')
    thead=soup.find_all('thead')
    tbody=soup.find_all('tbody')
    return(url_data_f2(thead,tbody))

url_2="https://www.equitymaster.com/stock-markets/1/-220/0/bse-above-rs-20-gainers-today"


##########################################################

gainers_losers=[]
for i in range(1,16):
    gainers_losers.append(str(i))
#print(gainers_losers)
bse_nse=[]
for i in range(1,16):
    bse_nse.append(str(i))
#for i in bse_nse:
#    print(i)
for i in range(21,30):
    bse_nse.append(str(i))
bse_nse.extend(['32','33','-201','-202','-203','-204','-205','-220','-301','-302','-320','air','aluminium','auto','autoc','bank','cement','chemicals','construction','energy','engg','fertilizer','consprds','food','finance','media','paint','pharma','reat','ship','sooftware','steel','telecom','textiles'])
#print(bse_nse)
#print(len(bse_nse))

gainers_losers_data=['-gainers-today','-losers-today','-up-circuit-breakers','-down-circuit-breakers','-most-active-stocks','-gainers-over-1-week','-gainers-over-1-month','-gainers-over-1-year','-losers-over-1-week','-losers-over-1-month','-losers-over-1-year','-gainers-over-3-years','-gainers-over-5-years','-losers-over-3-years','-losers-over-5-years']
bse_nse_data=['-bse-sensex','-bse-100','-bse-auto','-bse-bankex','-bse-capital-goods','-bse-consumer-durables','-bse-fmcg','-bse-healthcare','-bse-it','-bse-metal','-bse-oil-and-gas','-bse-psu','-bse-teck','-nse-50','-nse-it','-bse-a-group','-bse-b-group','-nifty-mid-cap-50','-bse-realty','-bse-power','-jr-nifty','-bank-nifty','-bse-500','-bse-200','-bse-mid-cap','-bse-small-cap','bse-rs-0-to-1','bse-rs-1-to-2','bse-rs-2-to-4','bse-rs-4-to-10','bse-rs-10-to-20','bse-above-rs-20','nse-rs-0-to-10','nse-rs-10-to-20','nse-above-rs-20','-sec-air','-sec-aluminium','-sec-auto','-sec-autoc','-sec-bank','-sec-cement','-sec-chemicals','-sec-construction','-sec-energy','-sec-engg','-sec-fertilizer','-sec-consprds','-sec-food','-sec-finance','-sec-media','-sec-paint','-sec-pharma','-sec-reat','-sec-ship','-sec-sooftware','-sec-steel','-sec-telecom','-sec-textiles']

out_data="\n"


a=1
for i in range(1,16):
    #print("i", i)
    for j in range(1,59):
        url='https://www.equitymaster.com/stock-markets/'+str(gainers_losers[i-1])+'/'+str(bse_nse[j-1])+'/0/-'+bse_nse_data[j-1]+gainers_losers_data[i-1]
        out_data=out_data+gainers_losers_data[i-1]+' | '+bse_nse_data[j-1]+'\n'+str(gainers_losers[i-1])+' | '+str(bse_nse[j-1])+'\n'
        out_data=out_data+url+"\n"
        
        if i in range(5):
            out_data=out_data+url_beautify_f2(url)
        else:
            out_data=out_data+url_beautify_f1(url)
        if (a%5==0):
            print("no. of websites : ",a)
        a+=1

date=str((datetime.datetime.now())).split(" ")
date=date[0].replace("-","")
date='.\data\\'+date+'.txt'

with open(date,'w') as f:
    f.write(out_data)



winsound.Beep(720,720)
