import requests
import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import ipaddress
import folium
import json
import sys






def set_window():
    global window
    window = tk.Tk()
    window.geometry('1000x500')
    path = os.getcwd()
    icon_address = path+'\icons\icon-window.ico'
    _ico = Image.open(icon_address)
    ico = ImageTk.PhotoImage(_ico)
    window.wm_iconphoto(False, ico)
    window.title('IP-FINDER')
set_window()

def get_copied_text():
    import win32clipboard
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
        print('no copied text on clipboard or clipboard is in use')
        sys.exit(1)
    if ent.get() == '':
        ent.insert(0, data)
    else:
        ent.delete(0, 'end')
        ent.insert(0, data)
def Go():
    print("Loadding")
    ip_ = ent.get()
    if ip_ == '':
        messagebox.showinfo('information', 'empty box shows your own ip')
    window.destroy()
    def new_window():
        global window2
        window2 = tk.Tk()
        window2.geometry('1000x500')
        path = os.getcwd()
        icon_address = path+'\icons\icon-window.ico'
        _ico = Image.open(icon_address)
        ico = ImageTk.PhotoImage(_ico)
        window2.wm_iconphoto(False, ico)
        window2.title('IP-FINDER')
    new_window()

        
    f2 = tk.Frame(bg='lightgray')
    f3 = tk.Frame(bg='lightblue')
    f4 = tk.Frame(bg='lightblue')
    f5 = tk.Frame(bg='lightblue')
    f6 = tk.Frame(bg='lightblue')
    f7 = tk.Frame(bg='lightblue')
    f8 = tk.Frame(bg='lightblue')
    f9 = tk.Frame(bg='lightblue')
    f10 = tk.Frame(bg='lightblue')
    f11 = tk.Frame(bg='lightblue')
    f12 = tk.Frame(bg='lightblue')
    f13 = tk.Frame(bg='lightblue')
    f14 = tk.Frame(bg='lightblue')
    f15 = tk.Frame(bg='lightblue')
    f16 = tk.Frame(bg='lightblue')
    f17 = tk.Frame(bg='lightblue')
    f18 = tk.Frame(bg='lightblue')
    f12 = tk.Frame(bg='lightblue')
    f13 = tk.Frame(bg='lightblue')
    f14 = tk.Frame(bg='lightblue')
    f15 = tk.Frame(bg='lightblue')
    f16 = tk.Frame(bg='lightblue')
    f17 = tk.Frame(bg='lightblue')
    f18 = tk.Frame(bg='lightblue')
    f19 = tk.Frame(bg='lightblue')
    f20 = tk.Frame(bg='lightblue')
    f21 = tk.Frame(bg='lightblue')
    f22 = tk.Frame(bg='lightblue')
    f23 = tk.Frame(bg='lightblue')
    f24 = tk.Frame(bg='lightblue')
    f25 = tk.Frame(bg='lightblue')
    


    
    label2 = tk.Label(master=f2, text='INFORMATION', bg='lightgray')
    url = 'https://www.iplocate.io/api/lookup/'+ip_
    data = requests.get(url)
    data = data.text
    data_ = json.loads(data)
    _data_list = list(data_)
    check_proxy = data_['threat']
    check_proxy_ = list(data_['threat'])
    label3 = tk.Label(master=f3, text=_data_list[0]+' : ', bg='orange', font=('Times', 13))
    label4 = tk.Label(master=f3, text=data_['ip'], bg='yellow', font=('Times', 13))
    label5 = tk.Label(master=f4, text=_data_list[1]+' : ', bg='orange', font=('Times', 13))
    label6 = tk.Label(master=f4, text=data_['country'], bg='yellow', font=('Times', 13))
    label7 = tk.Label(master=f5, text=_data_list[2]+' : ', bg='orange', font=('Times', 13))
    label8 = tk.Label(master=f5, text=data_['country_code'], bg='yellow', font=('Times', 13))
    label9 = tk.Label(master=f6, text=_data_list[3]+' : ', bg='orange', font=('Times', 13))
    label10 = tk.Label(master=f6, text=str(data_['is_eu']), bg='yellow', font=('Times', 13))
    label11 = tk.Label(master=f7, text=_data_list[4]+' : ', bg='orange', font=('Times', 13))
    label12 = tk.Label(master=f7, text=data_['city'], bg='yellow', font=('Times', 13))
    label13 = tk.Label(master=f8, text=_data_list[5]+' : ', bg='orange', font=('Times', 13))
    label14 = tk.Label(master=f8, text=data_['continent'], bg='yellow', font=('Times', 13))
    label15 = tk.Label(master=f9, text=_data_list[6]+' : ', bg='orange', font=('Times', 13))
    label16 = tk.Label(master=f9, text=data_['latitude'], bg='yellow', font=('Times', 13))
    label17 = tk.Label(master=f10, text=_data_list[7]+' : ', bg='orange', font=('Times', 13))
    label18 = tk.Label(master=f10, text=data_['longitude'], bg='yellow', font=('Times', 13))
    label19 = tk.Label(master=f11, text=_data_list[8]+' : ', bg='orange', font=('Times', 13))
    label20 = tk.Label(master=f11, text=data_['time_zone'], bg='yellow', font=('Times', 13))
    label21 = tk.Label(master=f12, text=_data_list[9]+' : ', bg='orange', font=('Times', 13))
    label22 = tk.Label(master=f12, text=data_['postal_code'], bg='yellow', font=('Times', 13))
    label23 = tk.Label(master=f13, text=_data_list[10]+' : ', bg='orange', font=('Times', 13))
    label24 = tk.Label(master=f13, text=data_['subdivision'], bg='yellow', font=('Times', 13))
    label25 = tk.Label(master=f14, text=_data_list[11]+' : ', bg='orange', font=('Times', 13))
    label26 = tk.Label(master=f14, text=data_['subdivision2'], bg='yellow', font=('Times', 13))
    label27 = tk.Label(master=f15, text=_data_list[12]+' : ', bg='orange', font=('Times', 13))
    label28 = tk.Label(master=f15, text=data_['network'], bg='yellow', font=('Times', 13))
    label29 = tk.Label(master=f19, text=_data_list[13]+' : ', bg='orange', font=('Times', 13))
    label30 = tk.Label(master=f19, text=data_['org'], bg='yellow', font=('Times', 13))
    label31 = tk.Label(master=f20, text=_data_list[14]+' : ', bg='orange', font=('Times', 13))
    label32 = tk.Label(master=f20, text=data_['asn'], bg='yellow', font=('Times', 13))
    label33 = tk.Label(master=f21, text=_data_list[15]+' : ', bg='orange', font=('Times', 13))
    label34 = tk.Label(master=f21, text=data_['asn_network'], bg='yellow', font=('Times', 13))
    label35 = tk.Label(master=f22, text=check_proxy_[0]+' : ', bg='orange', font=('Times', 13))
    label36 = tk.Label(master=f22, text=str(check_proxy['is_proxy']), bg='yellow', font=('Times', 13))
    label33 = tk.Label(master=f23, text='net mask : ', bg='orange', font=('Times', 13))
    label34 = tk.Label(master=f23, text=str(ipaddress.IPv4Network(data_['ip']).netmask), bg='yellow', font=('Times', 13))
    if checkvar.get() == 1:
        os.chdir('maps')
        location_ = [data_['latitude'], data_['longitude']]
        MAP1 = folium.Map(location = location_, zoom_start=12) 
        MAP_ = folium.Marker(location=location_, popup = "IP location: "+data_['ip'], icon=folium.Icon(color = 'green')).add_to(MAP1)
        MAP_.save('Map'+data_['ip']+'.html')

    

        
















    #*************
    f2.pack(fill=tk.BOTH)
    label2.pack(side=tk.TOP)
    label3.pack(side=tk.LEFT)
    f3.pack(fill=tk.BOTH)
    label4.pack(side=tk.LEFT)
    label5.pack(side=tk.LEFT)
    label6.pack(side=tk.LEFT)
    label7.pack(side=tk.LEFT)
    label8.pack(side=tk.LEFT)
    label9.pack(side=tk.LEFT)
    label10.pack(side=tk.LEFT)
    label11.pack(side=tk.LEFT)
    label12.pack(side=tk.LEFT)
    label13.pack(side=tk.LEFT)
    label14.pack(side=tk.LEFT)
    label15.pack(side=tk.LEFT)
    label16.pack(side=tk.LEFT)
    label17.pack(side=tk.LEFT)
    label18.pack(side=tk.LEFT)
    label19.pack(side=tk.LEFT)
    label20.pack(side=tk.LEFT)
    label21.pack(side=tk.LEFT)
    label22.pack(side=tk.LEFT)
    label23.pack(side=tk.LEFT)
    label24.pack(side=tk.LEFT)
    label25.pack(side=tk.LEFT)
    label26.pack(side=tk.LEFT)
    label27.pack(side=tk.LEFT)
    label28.pack(side=tk.LEFT)
    label29.pack(side=tk.LEFT)
    label30.pack(side=tk.LEFT)
    label31.pack(side=tk.LEFT)
    label32.pack(side=tk.LEFT)
    label33.pack(side=tk.LEFT)
    label34.pack(side=tk.LEFT)
    label35.pack(side=tk.LEFT)
    label36.pack(side=tk.LEFT)


    f4.pack(fill=tk.BOTH)
    f5.pack(fill=tk.BOTH)
    f6.pack(fill=tk.BOTH)
    f7.pack(fill=tk.BOTH)
    f8.pack(fill=tk.BOTH)
    f9.pack(fill=tk.BOTH)
    f10.pack(fill=tk.BOTH)
    f11.pack(fill=tk.BOTH)
    f12.pack(fill=tk.BOTH)
    f13.pack(fill=tk.BOTH)
    f14.pack(fill=tk.BOTH)
    f15.pack(fill=tk.BOTH)
    f16.pack(fill=tk.BOTH)
    f17.pack(fill=tk.BOTH)
    f18.pack(fill=tk.BOTH)
    f19.pack(fill=tk.BOTH)
    f20.pack(fill=tk.BOTH)
    f21.pack(fill=tk.BOTH)
    f22.pack(fill=tk.BOTH)
    f23.pack(fill=tk.BOTH)
    f24.pack(fill=tk.BOTH)
    f25.pack(fill=tk.BOTH)





















        
#----------------------
f = tk.Frame(master=window)


#----------------------
label = tk.Label(master=f, text='Write or Past your IP Address here')
label.config(font=('Times', 20))






#----------------------
ent = tk.Entry(master=f, font=('Times', 20), fg='blue', width=25)






#----------------------
button = tk.Button(master=f, text='PAST', command=get_copied_text, width=5, height=3)
checkvar = tk.IntVar()
cb = tk.Checkbutton(master=window, text='Create HTML map file for my ip location', variable = checkvar, onvalue=1, offvalue=0, height=3, width=3)
button_nw = tk.Button(master=f, width=9, height=4, font=('Times', 15),  fg='white',bg='green', text='Check Now', command=Go)



#----------------------
f.pack(fill=tk.BOTH)
label.pack(side=tk.LEFT)
ent.pack(side=tk.LEFT)
button.pack(side=tk.LEFT)
cb.pack(fill = tk.X, side=tk.BOTTOM)
button_nw.pack(side=tk.RIGHT)




























window.mainloop()
