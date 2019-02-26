from tkinter import *
import sqlite3
from tkinter import messagebox as box

from tkinter import ttk
from PIL import Image, ImageTk

conn=sqlite3.connect('ta.db')
c=conn.cursor()

#c.execute("CREATE TABLE Test(fname TEXT,lname TEXT,sap INTEGER,seq TEXT,ans TEXT,depart TEXT,year INTEGER,div TEXT,pasw INTEGER,attend INTEGER)")
#c.execute("CREATE TABLE Feep(fname TEXT,lname TEXT,sap INTEGER,depart TEXT,div TEXT,feepa INTEGER)")
conn.commit()

root=Tk()

root.title("Welcome")

fnt1=StringVar()
lnt1=StringVar()
s1=IntVar()

fnt1p1=StringVar()

fnt1p=StringVar()
lnt1p=StringVar()
s1p=IntVar()
lnt1phm=StringVar()
lnt1phk=StringVar()
fnt1ph=StringVar()
lnt1ph=StringVar()
s1ph=IntVar()
s=StringVar()
fnt5=StringVar()
lnt5=StringVar()
s5=IntVar()

seq1=StringVar()
ans1=StringVar()
fnt8=StringVar()
lnt8=StringVar()
s8=IntVar()
pro11=StringVar()

seq8=StringVar()
ans8=StringVar()
past8=StringVar()

year11=StringVar()
div1=StringVar()
dep1=StringVar()
past1=StringVar()
past5=StringVar()
attend1=IntVar()

dep6=StringVar()
y6=StringVar()
div6=StringVar()
f2=StringVar()
f3=StringVar()
f4=StringVar()
f5=StringVar()
f6=StringVar()
f1=IntVar()

class Application:
	"""docstring for ClassName"""
	def __init__(self, master1):
		
		self.master1 = master1
		'''
		self.f=Frame(master1,width=650,height=600, bg='lightgreen')
		self.f.pack()
		'''
		self.fro=Canvas(root,bg='lightgreen',height=600,width=650)
		self.image1=PhotoImage(file="C:/Users/Lenovo/Desktop/school.png")
		self.fro.create_image(100,50,anchor=NW,image=self.image1)
		self.fro.pack()



		self.h=Label(root,text="D.J.SANGHVI COLLEGE OF ENGINEERING",font=('arial 20 bold'),fg='black')
		self.h.place(x=50,y=0)

		self.a=Button(root,command=self.stu1)
		self.okb1 = PhotoImage(file="C:/Users/Lenovo/Desktop/book.png")
		
		self.tmi=self.okb1.subsample(3,3)
		self.a.config(image=self.tmi)
		self.a.place(x=200,y=200)
		
		self.a1=Button(root,command=self.fac)
		self.okb11 = PhotoImage(file="C:/Users/Lenovo/Desktop/hello.png")
		
		self.tmi1=self.okb11.subsample(3,3)
		self.a1.config(image=self.tmi1)
		self.a1.place(x=350,y=200)

		self.stu=Label(root,text="STUDENT",font=('arial 15 bold'),fg='black')
		self.stu.place(x=210,y=325)

		self.tea=Label(root,text="FACULTY",font=('arial 15 bold'),fg='black')
		self.tea.place(x=360,y=325)

		self.gal=Button(root,text="GALLERY",width=10,height=3,bg='steelblue',command=self.gal1)
		self.gal.place(x=289,y=370)




		

	def fac(self):
		fac1=Toplevel()
		o=App21(fac1)




	
	def stu1(self):
		tr1=Toplevel()
		m=Application3(tr1)

	

		



		'''
	def reg():
		count=0
		firstname=self.fnt.get()
		lastname=self.lnt.get()
		sapid=self.s.get()
		depo=self.dep.get()
			year1=self.ye.get()
			divi=self.di.get()
			password=self.past.get()
			
			if(firstname=="" or lastname=="" or sapid=="" or depo=="" or year1=="" or divi=="" or password==""):
				box.showinfo('ERROR','Enter all details')
			else:
				for row in c.execute("SELECT * FROM Test where sap=?",(sapid,)):
					count=count+1
				
			
				
				if(count==0):
					c.execute("INSERT INTO Test VALUES(?,?,?,?,?,?,?)",(firstname,lastname,sapid,depo,year1,divi,password))
					box.showinfo('Successful Registration','Done')
					
				else:
					box.showinfo('Error','User already exists')
					
				conn.commit()	
				'''
		
		

	


	def gal1(self):
		tr=Toplevel()
		p=Application5(tr)


class App21:
	
		def __init__(self, we1):
			
			self.we1 = we1
			self.we1.title('Faculty Update Attendance')

			self.f15=Frame(we1,width=600,height=800, bg='pink')
			self.f15.pack()
			
		

			self.fc1=Label(we1,text="D.J.SANGHVI COLLEGE OF ENGINEERING",font=('arial 20 bold'),fg='red')
			self.fc1.place(x=20,y=0)

			self.fc2=Label(we1,text="Sap Id:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.fc2.place(x=60,y=60)

			self.fc3=Label(we1,text="Department:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.fc3.place(x=60,y=110)

			self.fc4=Label(we1,text="First name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.fc4.place(x=60,y=160)

			self.fc5=Label(we1,text="Last name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.fc5.place(x=60,y=210)

			self.fc6=Label(we1,text="Div:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.fc6.place(x=60,y=260)

			self.fc7=Label(we1,text="Update Attendance:",font=('arial 15 bold'),fg='black',bg='cyan')
			self.fc7.place(x=60,y=310)

			self.fc11=Entry(we1,textvariable=f1,width=30)
			self.fc11.place(x=300,y=70)
			f1.set("")

			self.fc22=Entry(we1,textvariable=f2,width=30)
			self.fc22.place(x=300,y=110)

			self.fc33=Entry(we1,textvariable=f3,width=30)
			self.fc33.place(x=300,y=160)
		

			self.fc44=Entry(we1,width=30,textvariable=f4)
			self.fc44.place(x=300,y=210)
			

			self.fc55=Entry(we1,textvariable=f5,width=30)
			self.fc55.place(x=300,y=260)

			self.fc66=Entry(we1,textvariable=f6,width=30)
			self.fc66.place(x=300,y=310)
			
			self.resfa=Button(we1,text="RESET",font=('arial 15 bold'),width=10,height=2,bg='steelblue',command=self.resetf11)
			self.resfa.place(x=60,y=450)

			self.upf=Button(we1,text="UPDATE ",font=('arial 15 bold'),width=14,height=2,bg='steelblue',command=self.upfa)
			self.upf.place(x=225,y=450)

			#self.bacf=Button(we1,text="BACK",font=('arial 15 bold'),width=10,height=2,bg='steelblue')
			#self.bacf.place(x=440,y=450)

			self.getfor=Button(we1,text="GET",font=('arial'),width=8,height=1,bg='steelblue',command=self.getfac)
			self.getfor.place(x=500,y=160)
			


			we1.resizable(False,False)
			we1.mainloop()


		def upfa(self):
			count61=0
			facfi1=self.fc33.get()
			
			facde1=self.fc22.get()
			facsa1=self.fc11.get()
			facatt=self.fc66.get()
			
			if(facfi1=="" or facde1=="" or facsa1=="" ):
				box.showinfo('ERROR','Enter all details')
			else:
				sql71="SELECT * FROM Test where sap=? AND fname=? AND depart=?"
				for row in c.execute(sql71,(facsa1,facfi1,facde1)):
					count61=count61+1
				if(count61>0):
					c.execute("UPDATE Test SET attend=(?) WHERE sap=(?)", (facatt, facsa1))
					box.showinfo('Successful','Done')

					
    
        
		def getfac(self):
			count6=0
			facfi=self.fc33.get()
			
			facde=self.fc22.get()
			facsa=self.fc11.get()
			
			if(facfi=="" or facde=="" or facsa=="" ):
				box.showinfo('ERROR','Enter all details')
			else:
				sql7="SELECT * FROM Test where sap=? AND fname=? AND depart=?"
				for row in c.execute(sql7,(facsa,facfi,facde)):
					count6=count6+1
				if(count6==0):
					box.showinfo('Error','User does not exist')
				else:
					
					sql7="SELECT * FROM Test where sap=? AND fname=? AND depart=?"
					for row in c.execute(sql7,(facsa,facfi,facde)):
						count6=count6+1
					p11=row[1]
					p12=row[7]
					f4.set(p11)
					f5.set(p12)
					

		def resetf11(self):
			f1.set("")
			f2.set("")
			f3.set("")
			f4.set("")
			f5.set("")
			f6.set("")






class Application3:
	
	def __init__(self, tr1):
		
		self.tr1 = tr1
		self.tr1.title('Student page')

		self.f=Canvas(tr1,bg='white',height=550,width=610)
		self.image11=PhotoImage(file="C:/Users/Lenovo/Desktop/bo1.png")
		self.f.create_image(100,50,anchor=NW,image=self.image11)
		self.f.pack()

		self.h=Label(tr1,text="D.J.SANGHVI COLLEGE OF ENGINEERING",font=('arial 20 bold'),fg='red')
		self.h.place(x=25,y=0)

		self.b1=Button(tr1,text="LOGIN",font=('arial 15 bold'),width=20,height=3,bg='steelblue',command=self.log)
		self.b1.place(x=200,y=100)

		self.b2=Button(tr1,text="REGISTER",font=('arial 15 bold'),width=20,height=3,bg='steelblue',command=self.reg)
		self.b2.place(x=200,y=200)

		self.b3=Button(tr1,text="FORGOT PASSWORD",font=('arial 15 bold'),width=20,height=3,bg='steelblue',command=self.fog)
		self.b3.place(x=200,y=300)

		self.b4=Button(tr1,text="FACULTY INFO",font=('arial 15 bold'),width=20,height=3,bg='steelblue')
		self.b4.place(x=200,y=400)

		tr1.resizable(False,False)
		tr1.mainloop()

	def log(self):
		hr=Toplevel()
		j=Application7(hr)


	def reg(self):

			tm=Toplevel()
			k=Application2(tm)

	def fog(self):
		we=Toplevel()
		k=App2(we)

class App2:
	
		def __init__(self, we):
			
			self.we = we
			self.we.title('Student-Forgot Password')
			self.frofor=Canvas(we,bg='white',height=600,width=650)
			self.image1for=PhotoImage(file="C:/Users/Lenovo/Desktop/quest.png")
			self.frofor.create_image(70,50,anchor=NW,image=self.image1for)
			self.frofor.pack()

			self.h1for=Label(we,text="D.J.SANGHVI COLLEGE OF ENGINEERING",font=('arial 20 bold'),fg='red')
			self.h1for.place(x=20,y=0)

			self.fn1for=Label(we,text="First name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.fn1for.place(x=60,y=60)

			self.ln1for=Label(we,text="Last name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.ln1for.place(x=60,y=110)

			self.s1for=Label(we,text="Sap ID:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.s1for.place(x=60,y=160)

			self.seur1for=Label(we,text="Security Question",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.seur1for.place(x=60,y=210)

			self.an1for=Label(we,text="Answer",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.an1for.place(x=60,y=260)

			self.pas12for=Label(we,text="Password:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.pas12for.place(x=60,y=310)

			self.fntfor=Entry(we,textvariable=fnt8,width=30)
			self.fntfor.place(x=300,y=70)

			self.lntfor=Entry(we,textvariable=lnt8,width=30)
			self.lntfor.place(x=300,y=110)

			self.sfor=Entry(we,textvariable=s8,width=30)
			self.sfor.place(x=300,y=160)
			s8.set("")

			self.sqfor=Entry(we,width=30,textvariable=seq8)
			self.sqfor.place(x=300,y=210)
			

			self.answfor=Entry(we,textvariable=ans8,width=30)
			self.answfor.place(x=300,y=260)

			self.pastfor=Entry(we,textvariable=past8,width=30)
			self.pastfor.place(x=300,y=310)

			self.res12for=Button(we,text="RESET",font=('arial 15 bold'),width=10,height=2,bg='steelblue',command=self.resetfog)
			self.res12for.place(x=60,y=450)

			self.reg12for=Button(we,text="GET PASSWORD",font=('arial 15 bold'),width=14,height=2,bg='steelblue',command=self.detfog)
			self.reg12for.place(x=225,y=450)

			#self.bac12for=Button(we,text="BACK",font=('arial 15 bold'),width=10,height=2,bg='steelblue')
			#self.bac12for.place(x=440,y=450)

			self.getfor=Button(we,text="GET",font=('arial'),width=10,height=1,bg='steelblue',command=self.getfor1)
			self.getfor.place(x=525,y=200)



			we.resizable(False,False)
			we.mainloop()


		def getfor1(self):
			count=0
			count1=0
			count11=0
			firstnamef=self.fntfor.get()
			
			lastnamef=self.lntfor.get()
			sapidf=self.sfor.get()
			
			if(firstnamef=="" or lastnamef=="" or sapidf=="" ):
				box.showinfo('ERROR','Enter all details')
			else:
				sql="SELECT * FROM Test where sap=? AND fname=? AND lname=?"
				for row in c.execute(sql,(sapidf,firstnamef,lastnamef)):
					count=count+1
				if(count==0):
					box.showinfo('Error','User does not exist')
				else:
					
					sql1="SELECT * FROM Test where sap=? AND fname=? AND lname=?"
					for row in c.execute(sql1,(sapidf,firstnamef,lastnamef)):
						count1=count1+1
					ds=row[3]
					seq8.set(ds)

		def detfog(self):
						count11=0
						firstnameff=self.fntfor.get()
			
						lastnameff=self.lntfor.get()
						sapidff=self.sfor.get()
						seqff=self.sqfor.get()
						anssfor=self.answfor.get()
						sql12="SELECT * FROM Test where sap=? AND fname=? AND lname=? AND ans=?"
						for row in c.execute(sql12,(sapidff,firstnameff,lastnameff,anssfor)):
							count11=count11+1
						ds1=row[8]
						if(count11==0):
							box.showinfo('Error','Invalid Answer')
						else:
							past8.set(ds1)
						



					




		def resetfog(self):
			fnt8.set("")
			lnt8.set("")
			s8.set("")
			seq8.set("")
			ans8.set("")
			past8.set("")


class Application7:
	
		def __init__(self, tm):
			
			self.tm = tm
			self.tm.title('Student Login')

			self.f21=Frame(tm,width=600,height=800, bg='yellow')
			self.f21.pack()

			self.h1=Label(tm,text="D.J.SANGHVI COLLEGE OF ENGINEERING",font=('arial 20 bold'),fg='black')
			self.h1.place(x=20,y=0)


			self.s12=Label(tm,text="Sap ID:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.s12.place(x=60,y=60)

			self.fn1=Label(tm,text="First name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.fn1.place(x=60,y=110)

			self.ln1=Label(tm,text="Last name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.ln1.place(x=60,y=160)

			

			self.dep12=Label(tm,text="Department:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.dep12.place(x=60,y=210)

			self.ye12=Label(tm,text="Year:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.ye12.place(x=60,y=260)

			self.di12=Label(tm,text="Division:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.di12.place(x=60,y=310)

			self.pas12=Label(tm,text="Password:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.pas12.place(x=60,y=360)


			self.s123=Entry(tm,textvariable=s5,width=30)
			self.s123.place(x=300,y=70)
			s5.set("")


			
			self.fnt12=Entry(tm,textvariable=fnt5,width=30)
			self.fnt12.place(x=300,y=110)

			self.lnt12=Entry(tm,textvariable=lnt5,width=30)
			self.lnt12.place(x=300,y=160)

			
			
		

			self.dep67=Entry(tm,textvariable=dep6,width=30)
			self.dep67.place(x=300,y=210)

			self.ye6=Entry(tm,textvariable=y6,width=30)
			self.ye6.place(x=300,y=260)
			y6.set("")
			

			self.di6=Entry(tm,textvariable=div6,width=30)
			self.di6.place(x=300,y=310)

			self.past12=Entry(tm,textvariable=past5,width=30,show="*")
			self.past12.place(x=300,y=360)

			self.res12=Button(tm,text="RESET",font=('arial 15 bold'),width=10,height=2,bg='steelblue',command=self.resetlog)
			self.res12.place(x=60,y=500)

			self.reg12=Button(tm,text="LOGIN",font=('arial 15 bold'),width=10,height=2,bg='steelblue',command=self.reglog)
			self.reg12.place(x=250,y=500)

			#self.bac12=Button(tm,text="BACK",font=('arial 15 bold'),width=10,height=2,bg='steelblue')
			#self.bac12.place(x=440,y=500)

			self.ret=Button(tm,text="RETRIEVE",font=('arial'),width=8,height=1,bg='steelblue',command=self.ret1)
			self.ret.place(x=490,y=70)

			

			tm.resizable(False,False)
			tm.mainloop()
		
		def ret1(self):
			sapidq=self.s123.get()
			ff=self.fnt12.get()

			ll=self.lnt12.get()
			co=0
			
			if(sapidq=="" or ff=="" or ll==""):
				box.showinfo('ERROR','Enter details')
			else:
				sql="SELECT * FROM Test where sap=? AND fname=? AND lname=?"
				for row in c.execute(sql,(sapidq,ff,ll)):
					co=co+1
				if(co==0):
					box.showinfo('Error','User does not exist')
				else:

					firstname1=row[0]
					lastname1=row[1]
					sapid1=row[2]


					depo1=row[5]
					year111=row[6]
					divi1=row[7]

					
					
					div6.set(divi1)
					dep6.set(depo1)
					y6.set(year111)



				
				


		def resetlog(self):
			fnt5.set("")
			lnt5.set("")
			s5.set("")
			past5.set("")
			div6.set("")
			dep6.set("")
			y6.set("")

		def reglog(self):
			count=0
			count1=0
			firstname=self.fnt12.get()
			
			lastname=self.lnt12.get()
			sapid=self.s123.get()
			password=self.past12.get()
			if(firstname=="" or lastname=="" or sapid=="" or password==""):
				box.showinfo('ERROR','Enter all details')
			else:
				sql="SELECT * FROM Test where sap=? AND fname=? AND lname=?"
				for row in c.execute(sql,(sapid,firstname,lastname)):
					count=count+1
				if(count==0):
					box.showinfo('Error','User does not exist')
				else:
					
					sql1="SELECT * FROM Test where sap=? AND fname=? AND lname=? AND pasw=?"
					for row in c.execute(sql1,(sapid,firstname,lastname,password)):
						count1=count1+1
					if(count1==0):
						box.showinfo('Error','Password Incorrect')
					else:
						
						window=Toplevel()
						g=App1(window)
						
						

						
		

class App1:
	
		def __init__(self,kk):
								
			self.kk = kk

			self.kk.title("WELCOME")

			self.fro23=Canvas(kk,bg='white',height=530,width=590)
			self.image23=PhotoImage(file="C:/Users/Lenovo/Desktop/logbook.png")
			self.fro23.create_image(100,50,anchor=NW,image=self.image23)
			self.fro23.pack()

			
			

			self.kk=Label(kk,text="D.J.SANGHVI COLLEGE OF ENGINEERING",font=('arial 20 bold'),fg='black')
			self.kk.place(x=25,y=0)

			self.tim=Button(kk,text="TIMETABLE",font=('arial 15 bold'),width=20,height=3,bg='pink',command=self.time)
			self.tim.place(x=200,y=100)
			self.att=Button(kk,text="ATTENDANCE",font=('arial 15 bold'),width=20,height=3,bg='pink',command=self.go1)
			self.att.place(x=200,y=250)

			#self.fee=Button(kk,text="PAY FEES",font=('arial 15 bold'),width=20,height=3,bg='pink',command=self.pay)
			#self.fee.place(x=200,y=400)

			



			kk.resizable(False,False)
			kk.mainloop()


		def pay(self):
			win111=Toplevel()
			q1=Atte1(win111)

		def go1(self):
			win11=Toplevel()
			q=Atte(win11)
			'''
		firstnamea=self.fnt.get()
		pro11.set(firstnamea)
		'''


		def time(self):
			ha=Toplevel()
			c=Time2(ha)


class Atte1:
	
		def __init__(self, tm1g1):
			
			self.tm1g1 = tm1g1
			self.tm1g1.title('Check Attendance')

			self.f1g1=Frame(tm1g1,width=600,height=630, bg='blue')
			self.f1g1.pack()

			self.h1g1=Label(tm1g1,text="D.J.SANGHVI COLLEGE OF ENGINEERING",font=('arial 20 bold'),fg='black')
			self.h1g1.place(x=20,y=0)

			self.fn1gk=Label(tm1g1,text="First name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.fn1gk.place(x=60,y=60)

			self.ln1gk=Label(tm1g1,text="Sap Id:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.ln1gk.place(x=60,y=110)

			self.d1gk=Label(tm1g1,text="Department:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.d1gk.place(x=60,y=160)

			self.d1gk1=Label(tm1g1,text="Last name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.d1gk1.place(x=60,y=210)

			self.d1gk2=Label(tm1g1,text="Division:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.d1gk2.place(x=60,y=260)

			self.fntgh=Entry(tm1g1,textvariable=fnt1ph,width=30)
			self.fntgh.place(x=300,y=70)

			self.sgh=Entry(tm1g1,textvariable=s1ph,width=30)
			self.sgh.place(x=300,y=110)
			s1ph.set("")

			self.dgh=Entry(tm1g1,textvariable=lnt1ph,width=30)
			self.dgh.place(x=300,y=160)

			self.dghf=Entry(tm1g1,textvariable=lnt1phm,width=30)
			self.dghf.place(x=300,y=210)

			self.dghn=Entry(tm1g1,textvariable=lnt1phk,width=30)
			self.dghn.place(x=300,y=260)

			self.resetpa=Button(tm1g1,text="RESET",font=('arial 15 bold'),width=10,height=2,bg='lightgreen',command=self.pafe1)
			self.resetpa.place(x=50,y=330)

			self.pafe=Button(tm1g1,text="PAY FEES",font=('arial 15 bold'),width=10,height=2,bg='lightgreen')
			self.pafe.place(x=200,y=330)

			#self.backfe=Button(tm1g1,text="BACK",font=('arial 15 bold'),width=10,height=2,bg='lightgreen')
			#self.backfe.place(x=350,y=330)

			self.retp=Button(tm1g1,text="RETRIEVE",font=('arial'),width=10,height=1,bg='lightgreen')
			self.retp.place(x=500,y=110)

			self.tm1g1.resizable(False,False)
			self.tm1g1.mainloop()


		def pafe1(self):
			fnt1ph.set("")
			lnt1ph.set("")
			s1ph.set("")
			lnt1phm.set("")
			lnt1phk.set("")
			

class Atte:
	
		def __init__(self, tm1g):
			
			self.tm1g = tm1g
			self.tm1g.title('Check Attendance')

			self.f1g=Frame(tm1g,width=600,height=600, bg='pink')
			self.f1g.pack()

			self.h1g=Label(tm1g,text="D.J.SANGHVI COLLEGE OF ENGINEERING",font=('arial 20 bold'),fg='black')
			self.h1g.place(x=20,y=0)

			self.fn1g=Label(tm1g,text="First name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.fn1g.place(x=60,y=60)

			self.ln1g=Label(tm1g,text="Sap Id:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.ln1g.place(x=60,y=110)

			self.d1g=Label(tm1g,text="Department:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.d1g.place(x=60,y=160)

			self.fntg=Entry(tm1g,textvariable=fnt1p,width=30)
			self.fntg.place(x=300,y=70)

			self.sg=Entry(tm1g,textvariable=s1p,width=30)
			self.sg.place(x=300,y=110)
			s1p.set("")

			self.dg=Entry(tm1g,textvariable=lnt1p,width=30)
			self.dg.place(x=300,y=160)

			self.resetat=Button(tm1g,text="RESET",font=('arial 15 bold'),width=10,height=2,bg='steelblue',command=self.reseta)
			self.resetat.place(x=60,y=220)

			self.check=Button(tm1g,text="Check",font=('arial 15 bold'),width=10,height=2,bg='steelblue',command=self.yo)
			self.check.place(x=250,y=220)

			self.d1g1=Label(tm1g,text="Attendance(%):",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.d1g1.place(x=60,y=310)

			self.fntg1=Entry(tm1g,textvariable=fnt1p1,width=30)
			self.fntg1.place(x=300,y=310)
			 
			#self.backa=Button(tm1g,text="Back",font=('arial 15 bold'),width=10,height=2,bg='steelblue')
			#self.backa.place(x=180,y=380)
			


		def yo(self):
				sapido=self.sg.get()
				ffo=self.fntg.get()

				dgo=self.dg.get()
				co1=0
				
				if(sapido=="" or ffo=="" or dgo==""):
					box.showinfo('ERROR','Enter details')
				else:
					sql4="SELECT * FROM Test where sap=? AND fname=? AND depart=?"
					for row in c.execute(sql4,(sapido,ffo,dgo)):
						co1=co1+1
					if(co1==0):
						box.showinfo('Error','User does not exist')
					else:

						ap=row[9]
						fnt1p1.set(ap)

		def reseta(self):
			fnt1p1.set("")
			lnt1p.set("")
			s1p.set("")
			fnt1p.set("")
					
			




class Time2:
	
	def __init__(self, ha1):
		
		self.ha1 = ha1
		self.ha1.title('Timetable')
		self.fro1g=Canvas(ha1,bg='black',height=600,width=1000)
		
		
		self.image1g=PhotoImage(file="C:/Users/Lenovo/Desktop/t1.png")
		self.image2g=PhotoImage(file="C:/Users/Lenovo/Desktop/t3.png")
		
		self.image11g=self.image1g.subsample(1,1)
		self.image21g=self.image2g.subsample(1,1)
		


		def i1g():
			self.imagg=self.fro1g.create_image(100,50,anchor=NW,image=self.image11g)
		def i2g():
			self.imagg=self.fro1g.create_image(100,50,anchor=NW,image=self.image21g)
		

		varg=IntVar()

		R1g=Radiobutton(ha1,text="A div",variable=varg,value=1,command=i1g)
		R1g.pack(anchor=W)

		R2g=Radiobutton(ha1,text="B div",variable=varg,value=2,command=i2g)
		R2g.pack(anchor=W)

		
		self.fro1g.pack()
		self.ha1.resizable(False,False)
		self.ha1.mainloop()






class Application2:
	
		def __init__(self, tm1):
			
			self.tm1 = tm1
			self.tm1.title('Student Register')

			self.f1=Frame(tm1,width=600,height=600, bg='pink')
			self.f1.pack()

			self.h1=Label(tm1,text="D.J.SANGHVI COLLEGE OF ENGINEERING",font=('arial 20 bold'),fg='black')
			self.h1.place(x=20,y=0)

			self.fn1=Label(tm1,text="First name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.fn1.place(x=60,y=60)

			self.ln1=Label(tm1,text="Last name:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.ln1.place(x=60,y=110)

			self.s1=Label(tm1,text="Sap ID:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.s1.place(x=60,y=160)


			self.seur1=Label(tm1,text="Security Question",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.seur1.place(x=60,y=210)

			self.an1=Label(tm1,text="Answer",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.an1.place(x=60,y=260)

			self.dep1=Label(tm1,text="Department:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.dep1.place(x=60,y=310)

			self.ye1=Label(tm1,text="Year:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.ye1.place(x=60,y=360)

			self.di1=Label(tm1,text="Division:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.di1.place(x=60,y=410)

			self.pas1=Label(tm1,text="Password:",font=('arial 15 bold'),fg='black',bg='lightgreen')
			self.pas1.place(x=60,y=460)

			

			self.fnt=Entry(tm1,textvariable=fnt1,width=30)
			self.fnt.place(x=300,y=70)

			self.lnt=Entry(tm1,textvariable=lnt1,width=30)
			self.lnt.place(x=300,y=110)

			self.s=Entry(tm1,textvariable=s1,width=30)
			self.s.place(x=300,y=160)
			s1.set("")

			self.sq=ttk.Combobox(tm1,width=30,textvariable=seq1)
			self.sq.place(x=300,y=210)
			self.sq['values']=("Pizza or Pasta?","Nationality?","Hobby?")

			self.answ=Entry(tm1,textvariable=ans1,width=30)
			self.answ.place(x=300,y=260)

			self.dep=Entry(tm1,textvariable=dep1,width=30)
			self.dep.place(x=300,y=310)

			self.ye=ttk.Combobox(tm1,width=30,textvariable=year11)
			self.ye.place(x=300,y=360)
			self.ye['values']=("FE","SE","TE","BE")

			self.di=Entry(tm1,textvariable=div1,width=30)
			self.di.place(x=300,y=410)

			self.past=Entry(tm1,textvariable=past1,width=30,show="*")
			self.past.place(x=300,y=460)

			self.res=Button(tm1,text="RESET",font=('arial 15 bold'),width=10,height=2,bg='steelblue',command=self.res1)
			self.res.place(x=60,y=500)

			self.reg=Button(tm1,text="REGISTER",font=('arial 15 bold'),width=10,height=2,bg='steelblue',command=self.reg1)
			self.reg.place(x=250,y=500)

			#self.bac=Button(tm1,text="BACK",font=('arial 15 bold'),width=10,height=2,bg='steelblue')
			#self.bac.place(x=440,y=500)
			
			self.dis=Button(tm1,text="DISPLAY",font=('arial'),width=5,height=2,bg='steelblue',command=self.dis1)
			self.dis.place(x=500,y=400)

			



			tm1.resizable(False,False)
			tm1.mainloop()



		def res1(self):
			fnt1.set("")
			lnt1.set("")
			s1.set("")
			ans1.set("")
			seq1.set("")
			div1.set("")
			dep1.set("")
			year11.set("")
			past1.set("")



		def dis1(self):
			sapid=self.s.get()
			c.execute("SELECT * FROM Test")
			print(c.fetchall())
			conn.commit()

		def reg1(self):
			count=0
			firstname=self.fnt.get()
			lastname=self.lnt.get()
			sapid=self.s.get()
			depo=self.dep.get()
			year1=self.ye.get()
			divi=self.di.get()
			password=self.past.get()

			securityq=self.sq.get()
			answerq=self.answ.get()
			
			if(firstname=="" or lastname=="" or sapid=="" or depo=="" or year1=="" or divi=="" or password=="" or securityq=="" or answerq==""):
				box.showinfo('ERROR','Enter all details')
			else:
				for row in c.execute("SELECT * FROM Test where sap=?",(sapid,)):
					count=count+1
				
			
				
				if(count==0):
					c.execute("INSERT INTO Test VALUES(?,?,?,?,?,?,?,?,?,?)",(firstname,lastname,sapid,securityq,answerq,depo,year1,divi,password,0))
					box.showinfo('Successful Registration','Done')
					
				else:
					box.showinfo('Error','User already exists')
					
				conn.commit()	




			



class Application5:
	
	def __init__(self, ha):
		
		self.ha = ha
		self.ha.title('Gallery')
		self.fro1=Canvas(ha,bg='yellow',height=600,width=1000)
		
		
		self.image1=PhotoImage(file="C:/Users/Lenovo/Desktop/collegepic.png")
		self.image2=PhotoImage(file="C:/Users/Lenovo/Desktop/canpic.png")
		self.image3=PhotoImage(file="C:/Users/Lenovo/Desktop/libpic.png")
		self.image4=PhotoImage(file="C:/Users/Lenovo/Desktop/lab.png")
		self.image11=self.image1.subsample(1,1)
		self.image21=self.image2.subsample(1,1)
		self.image31=self.image3.subsample(1,1)
		self.image41=self.image4.subsample(1,1)


		def i1():
			self.imag=self.fro1.create_image(100,50,anchor=NW,image=self.image11)
		def i2():
			self.imag=self.fro1.create_image(100,50,anchor=NW,image=self.image21)
		def i3():
			self.imag=self.fro1.create_image(100,50,anchor=NW,image=self.image31)
		def i4():
			self.imag=self.fro1.create_image(100,50,anchor=NW,image=self.image41)

		var=IntVar()

		R1=Radiobutton(ha,text="College",variable=var,value=1,command=i1)
		R1.pack(anchor=W)

		R2=Radiobutton(ha,text="Canteen",variable=var,value=2,command=i2)
		R2.pack(anchor=W)

		R3=Radiobutton(ha,text="Library",variable=var,value=3,command=i3)
		R3.pack(anchor=W)

		R4=Radiobutton(ha,text="Lab",variable=var,value=4,command=i4)
		R4.pack(anchor=W)

		self.fro1.pack()
		self.ha.resizable(False,False)
		self.ha.mainloop()



b=Application(root)

root.resizable(False,False)
root.mainloop()
		
