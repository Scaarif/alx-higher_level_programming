#!/usr/bin/python3
""" Lists all cities from the database htbn_0e_4_usa
    The scripts takes 3 arguments:
        the username, password and database name
        i.e. (credentials to access the database)
"""
import sys
import MySQLdb


if __name__ == '__main__':
    # establish connection to the database
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    # get cursor (for multiple working envs using the same connection)
    cur = conn.cursor()
    # query the database (using actual SQL queries) for all states
    cur.execute(
        "SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON state_id=states.id \
                ORDER BY cities.id ASC")
    # get query results
    states = cur.fetchall()
    # do something with the results (print them out)
    for state in states:
        print(state)

    # clean up (close all open connections) once done
    cur.close()
    conn.close()
