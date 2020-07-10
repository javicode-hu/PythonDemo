import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "shopping")

# 使用cursor()方法获取操作游标
cursor = db.cursor()
name = "name The Everything Learning German Book: Speak, write, and understand basic German in no time"
number = 317
gphoto = "The Everyt1.jpg&The Everyt2.jpg"
types= "书籍"
publisher = "Adams Media; 2 (2009年11月18日)"
price = 98.03
carrige = 6.0
date = "2009年11月18日"
asin = "159869989X"
content="Order <I>das beste Bier</I> at Oktoberfest!<BR>Hitch a ride on <I>der Autobahn!</I><BR>Say <I>Wilkommen</I> to your <I>neuen deutschen Freunde!</I><P>Learning to <I>sprechen Sie Deutsches</I> is funand far easier than you might think. German and English are closely relatedyou already know <I>viele Phrasen!</I> With this guide, you will make sense of this fascinating language in no time.<P>This practical, hands-on <I>Buch</I> comes with easy-to-understand lessons, useful exercises, and a CD for pronunciation help. Building on the German languages close relation to English, this all-new edition covers everything from basic introductions to verb conversions. You will learn to:<UL><LI><I>Ich möchte ein Berliner, bitte.</I> Order food with ease.<LI><I>Wie viel kostet der Käse?</I> Ask how much items cost.<LI><I>Der Vater kaufte seinem Sohn ein Fahrrad.</I> Understand direct and indirect objects.<LI><I>viel / mehr / am meisten.</I> Use superlatives to communicate more effectively.<LI><I>Der Ball wird von dem Mann geschlagen.</I> Know when to use passive voice.</UL>Whether you want to sample <I>das stoutest Lager</I> or converse with your grandparents in their native tongue, youll soon discover just how easy it is to learn German! <P><B>This edition includes completely new material on:</B><UL><LI>Rules of spelling and punctuation <LI>Appropriate language for correspondence in German, including e-mail<LI>Updated exercises</UL>"


# SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', '%d', '%s', '%s')"%(a,b,c,e,f)
sql = "INSERT INTO ymxgoods(gname,number, gphoto, types, producer,price,carriage,pdate,paddress,described)VALUES ('%s','%d','%s','%s','%s','%f','%f','%s','%s','%s')" % (
name, number, gphoto, types, publisher, price, carrige, date, asin, content)
# try:
# 执行sql语句
cursor.execute(sql)
# 提交到数据库执行
db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()
#
# # 关闭数据库连接
db.close()