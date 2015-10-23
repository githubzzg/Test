#coding=utf-8  
import MySQLdb  
conn=MySQLdb.Connect(  
                         host='127.0.0.1',  
                         port=3306,  
                         user='root',  
                         passwd='a',  
                         db='tebuy',  
                         charset='utf8'  
                         )  
cursor=conn.cursor()  
sql='select * from spe_Product'  
cursor.execute(sql)  

print cursor.rowcount  
      
cursor.close()  
conn.close()  