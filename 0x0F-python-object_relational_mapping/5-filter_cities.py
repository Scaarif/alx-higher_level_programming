#!/usr/bin/python3
""" Lists all the cities in state matching the 4th argument
    from the database htbn_0e_0_usa.
    The scripts takes 4 arguments:
        the username, password, database name & the name of
        state to be searched for.
    Also, its safe from SQL Injections...
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
    # query the database (using actual SQL queries) for the states
    query = "SELECT name \
             FROM cities \
             WHERE state_id = ( SELECT id FROM states WHERE name = %s);"
    cur.execute(query, (sys.argv[4],))
    # get query results
    states = cur.fetchall()
    # do something with the results (print them out)
    for index, state in enumerate(states):
        if (index):
            print(', ', end="")
        print(state[0], end="")
    print()

    # clean up (close all open connections) once done
    cur.close()
    conn.close()
