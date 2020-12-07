#!/usr/bin/python


import MySQLdb as mdb
import sys

con = None

try:

    con = mdb.connect('localhost', 'gpio', 
        'cellbiol', 'gpio');

    cur = con.cursor()
    cur.execute("SELECT pinDescription FROM pinDescription WHERE pinNumber='25'")
    desc = cur.fetchone()
    
    cur.execute("SELECT pinDirection FROM pinDirection WHERE pinNumber='25'")
    data = cur.fetchone()

    cur.execute("SELECT pinStatus FROM pinStatus WHERE pinNumber='25'")
    status = cur.fetchone()

    print (desc[0], data[0], status[0])
    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()
