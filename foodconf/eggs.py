import sqlite3
import xlrd
conn = sqlite3.connect('foodtable/db.sqlite3')

c= conn.cursor()
group = 'Bakery'

workbook = xlrd.open_workbook('eggs.xlsx')
worksheet = workbook.sheet_by_index(0)
for i in range(0,5) :
	
	# item_name = worksheet.cell(i,0).value
	item_name        = worksheet.cell(i,0).value
	item_arabic_name = worksheet.cell(i,1).value
	the_ingredients  = worksheet.cell(i,2).value
	item_group       = 3
	refuse           = worksheet.cell(i,3).value
	water            = worksheet.cell(i,4).value
	enerygy          = worksheet.cell(i,5).value
	protein          = worksheet.cell(i,6).value
	fat              = worksheet.cell(i,7).value
	ASH              = worksheet.cell(i,8).value
	fiber            = worksheet.cell(i,9).value
	Carbohydrate     = worksheet.cell(i,10).value
	sodium           = worksheet.cell(i,11).value
	potasium         = worksheet.cell(i,12).value
	Calcium          = worksheet.cell(i,13).value
	phorphorus       = worksheet.cell(i,14).value
	magnisum         = worksheet.cell(i,15).value
	iron             = worksheet.cell(i,16).value
	zinc             = worksheet.cell(i,17).value
	coper            = worksheet.cell(i,18).value
	vitamen_a        = worksheet.cell(i,19).value
	vitamen_c        = worksheet.cell(i,20).value
	thiamen          = worksheet.cell(i,21).value
	riboflabn        = worksheet.cell(i,22).value
	# print(str(item_name) ,str(item_arabic_name),str(the_ingredients),str(item_group),(refuse) or 0,(water) or 0,(enerygy) or 0,(protein) or 0,(fat) or 0,(ASH) or 0,(fiber) or 0,(Carbohydrate) or 0, (sodium) or 0,(potasium) or 0,(Calcium) or 0, (phorphorus) or 0, (magnisum) or 0, (iron) or 0,(zinc) or 0,(coper) or 0, (vitamen_a) or 0, (vitamen_c) or 0, (thiamen )or 0,(riboflabn) or 0)

	strin  =  """INSERT INTO  foodconf_foodtable
	 (item_name, item_arabic_name, the_ingredients,item_group_id, refuse, water, enerygy, protein, fat, ASH, fiber, Carbohydrate, sodium, potasium, Calcium, phorphorus, magnisum, iron, zinc, coper, vitamen_a, vitamen_c, thiamen, riboflabn)
	 VALUES
	  ('%s', '%s', '%s',%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """%(str(item_name) ,str(item_arabic_name),str(the_ingredients),item_group,(refuse) or 0,(water) or 0,(enerygy) or 0,(protein) or 0,(fat) or 0,(ASH) or 0,(fiber) or 0,(Carbohydrate) or 0, (sodium) or 0,(potasium) or 0,(Calcium) or 0, (phorphorus) or 0, (magnisum) or 0, (iron) or 0,(zinc) or 0,(coper) or 0, (vitamen_a) or 0, (vitamen_c) or 0, (thiamen )or 0,(riboflabn) or 0)
	c.execute(strin)
	conn.commit()