#!/usr/local/bin/python

import MySQLdb

def getNextCombo(combo, num):
  combo[num] += 1
  if ((combo[num] > 9) and (num == 0)):
    return (-1, combo)
  while (combo[num] > 9):
    nc_tuple = getNextCombo(combo, num-1)
    i = nc_tuple[0]
    combo = nc_tuple[1]
    if (i == -1):
      return (-1, combo)
    combo[num] = i+1
  return (combo[num], combo)

def getAllCombos():
  all_combos = []
  for slots in range(2,10):
    combo = range(1,slots+1) 
    flag = 0
    while (flag != -1):
      all_combos.append(list(combo)) # pass in a copy so we 
                                     # don't keep modifying the thing
      c_tuple = getNextCombo(combo, slots-1)
      flag = c_tuple[0]
      combo = c_tuple[1]
  return all_combos

# Means we're running as an executable from the command line 
db = MySQLdb.connect(user='janedoe', passwd='xxxxxxxx', db='kakuro')
db_cursor = db.cursor()  # Execute on the cursor
combos = getAllCombos()
for combo in combos:
  if (sum(combo) in range(3,45)):
    # Add sum-combo pair to combos table
    sql = '''INSERT INTO combos (slots, sum)
             VALUES ('%s', '%s')
          ''' % (len(combo), sum(combo))
    db_cursor.execute(sql)
    # Now, grab the just-created id (will be highest in table)
    sql = 'SELECT id FROM combos ORDER BY id DESC LIMIT 1'
    db_cursor.execute(sql)
    result = db_cursor.fetchone()
    combo_id = result[0]
    # Add all values in the sum to number combo id, tied to
    #  identifier from the combos table
    for num in combo:
      sql = '''INSERT INTO number_combos (combo_id, number_value)
               VALUES ('%s', '%s')
            ''' % (combo_id, num)
      db_cursor.execute(sql)  
