import json
import calendar
from bokeh.plotting import figure,show,output_file
X_categories=[]
month =[]
month_dic={}
with open('info.json','r') as f1:
	dic = json.load(f1)
	for i in range(len(dic)):
		mo = list(dic.values())
		date= mo[i]
		month.append(str(date.split('/')[1]))
	#print(month)
	for i in month:
		mo_name= calendar.month_abbr[int(i)]
		month_dic[mo_name]=month.count(i)
	#print(month_dic)
if __name__=="__main__":
	
	for i in range(1,13):
		m_name = calendar.month_abbr[i]
		X_categories.append(m_name)
	#print(X_categories)
	output_file("vbar.html")
	x= list(month_dic.keys())
	y= list(month_dic.values())
	#print(x,y)
	p = figure(x_range=X_categories)
	p.xaxis.axis_label="bday months"
	p.yaxis.axis_label="bday moth counts"
	p.vbar (x=x,top=y, width=0.5)
	show(p)
