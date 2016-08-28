GET_ALL_USERS = """SELECT * FROM Users"""
ADD_USER = """INSERT INTO Users (firstname, lastname, isadmin, email, datemodified)
              VALUES (%(first)s, %(last)s, %(admin)s, %(email)s, %(date)s);"""