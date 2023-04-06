from konlpy.tag import Hannanum
import sqlite3
import mariadb
import re

try:
    conn = mariadb.connect(
		user="root",
		password="1234",
		host="localhost",
		port=3306,
		database="peerna"
	)
except sqlite3.Error as e:
    print(f"Error connecting to sqlite3: {e}")
    
cur = conn.cursor()

sql = 'SELECT problem_id, answer FROM REPLY'
cur.execute(sql)
results = cur.fetchall()

hannanum = Hannanum()

for item in results:
	problem_id = item[0]
	answer = item[1]
	
	nouns_list = hannanum.nouns(answer)
	kor_nouns = list(set(nouns_list))

	eng_str = re.sub(r"[^a-zA-Z\s]", "", answer).split()
	for i in range(len(eng_str)):
		eng_str[i] = eng_str[i].lower()
	eng_nouns = list(set(eng_str))
	for noun in kor_nouns:
		cur.execute("begin")
		cur.execute("INSERT INTO KEYWORD (COUNT, NAME, PROBLEM_ID) VALUES (1, '%s', %d) ON DUPLICATE KEY UPDATE COUNT=COUNT+1" %(noun, problem_id))
		cur.execute("commit")
	for noun in eng_nouns:
		cur.execute("begin")
		cur.execute("INSERT INTO KEYWORD (COUNT, NAME, PROBLEM_ID) VALUES (1, '%s', %d) ON DUPLICATE KEY UPDATE COUNT=COUNT+1" %(noun, problem_id))
		cur.execute("commit")
 
 # 기본 Connection 설정이 auto-commit 인지 확인한다.
 # auto-commit 이 아니고, 스프링 JPA의 격리수준이 commit read 같이
 # 커밋된 것만 읽을 수 있으면 지금 이 상황이 벌어질 수 있다는 추측