from tkinter import *
import feedparser
from time import gmtime, strftime

class Application(Frame):
    def  __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.theLabel=Label(self, text="                                                                  RSS FEED TO JSON CONVERTER                                                                     ")
        self.theLabel.config(font=(60),fg='orange',bg='grey',height=2)
        self.theLabel1 = Label(self, text = '                           ENTER URL ----    ')
        self.theLabel1.config(font=60,fg='white',bg='grey')
        self.theLabel.grid(row=0, column=0, sticky='NW')
        self.theLabel1.grid(row=1, column=0, sticky='NW')
        self.entry1 = Entry(self,width=50)
        self.entry1.grid(row=1, column=0)
        self.button1 = Button(self, text = 'CONVERT',command=self.signn)
        self.button1.grid(row=8, column= 0, sticky='N')
        self.button2 = Button(self, text = 'CANCEL',command=self.canc)
        self.button2.grid(row=9, column= 0, sticky='N')
        self.text=Text(self,width=110,height=1,wrap=WORD)
        self.text.grid(row=10,column=0,columnspan=4,sticky='w')
        self.configure(background='grey')
    def signn(self):
        f = open('reqjson.txt','w')
        url=self.entry1.get()
        d = feedparser.parse(url)
        f.write('{')
        f.write('\n')
        f.write(' "feed":[')
        f.write('\n  ')
        
        try:
            
            for post in d.entries:
                
                l=post.title
                
                le=post.coverimage
                seven=post.author
                zero=post.description
                zero=zero.replace('"','')
                dPub = post.published
                dPubPretty = strftime(dPub, gmtime())
                c=post.guid
                f.write('\n')
                f.write('{')
                f.write('\n                     ')
                f.write('"id":"(%s)",'%c)
                f.write('\n                     ')
                f.write('"name":"%s",'%l)
                f.write('\n                     ')
                f.write('"image":"%s",'%le)
                f.write('\n                     ')
                f.write('"status":"%s",'%zero)
                f.write('\n                     ')
                f.write('"timestamp":"%s",'%dPubPretty)
                f.write('\n                     ')      
                f.write('"url":"%s",'%c)
                f.write('\n                     ')
                f.write('"author":"%s",'%seven)
                f.write('\n      ')
                f.write('},')
                f.write('\n')
            f.write(']}')
            message="json is written on attached text file "
            self.text.insert(0.0,message)
            f.close()
        except:
            message1="json is on command prompt opened in background"
            self.text.delete(0.0,END)
            self.text.insert(0.0,message1)
            print('{')
            print('\n')
            print(' "feed":[')
            print('\n  ')
            
            for post in d.entries:
                l=post.title
                le=post.coverimage
                seven=post.author
                #four=post.url
                zero=post.description
                zero=zero.replace('"','')
                dPub = post.published  
                dPubPretty = strftime(dPub, gmtime())
                c=post.guid
                print('{')
                print('\n                     ')
                print('"id":"(%s)",'%c)
                print('\n                     ')
                print('"name":"%s",'%l)
                print('\n                     ')
                print('"image":"%s",'%le)
                print('\n                     ')
                print('"status":"%s",'%zero)
                print('\n                     ')
                print('"timestamp":"%s",'%dPubPretty)
                print('\n                     ')      
                print('"url":"%s",'%c)
                print('\n                     ')
                print('"author":"%s",'%seven)
                print('\n      ')
                print('},')
                print('\n')
            print(']}')
    def canc(self):
        self.text.delete(0.0,END)
        self.entry1.delete(0,END)
root=Tk()

root.title("rss to json")
app=Application(root)
root.mainloop()
