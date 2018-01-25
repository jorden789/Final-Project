import mysql.connector
from mysql.connector import Error

def connect():

    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='information_repo',
                                       user='jallcock',
                                       password='M@rshall789')
        if conn.is_connected():
            print('Connected to MySQL database')

        records	= conn.cursor()

        records.execute("SELECT r.role_name, c2.competency_group_name, c1.competency_group_name, c.role_competency_level FROM competency_role_matrix c, competency_groups c1, roles r, competency_groups c2 WHERE c.competency_group_id = c1.competency_group_id AND  c.role_id = r.role_id and c1.competency_group_parent = c2.competency_group_id AND role_name = 'Software Engineer'")

        for record in records:
            competency_type = record[1]
            competency_name = record[2]
            print(competency_type + ' ' + competency_name)

    except Error as err:
        print(err)

    finally:
        conn.close()

if __name__ == '__main__':
    connect()
