import pymysql.cursors

print(pymysql.__file__)
print(dir(pymysql))

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='python3',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    '''
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `passwd`) VALUES (%s, %s)"
        cursor.execute(sql, ('thanhnm@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    '''

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `passwd` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
        print(type(result))

        sql = "SELECT * FROM users"
        cursor.execute(sql)
        print(cursor.description)
        print('*********')

        for row in cursor :
            print(row)
            print(type(row))
            print(row.keys())
            print(row['email'])
finally:
    connection.close()