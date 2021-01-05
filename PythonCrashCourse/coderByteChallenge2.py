def SeatingStudents(arr):

  bench = arr[0]
  taken = list(x for x in arr)[1:]

  seq1 = list(x for x in range(1, bench+1))
  seq2 = list(x for x in range(1, bench+1))

  col1 = list(filter(lambda x: x%2==0, seq1))
  col2 = list(filter(lambda x: x%2 != 0, seq2))

  seq1 = list(x for x in range(1, bench))
  seq2 = list(x for x in range(3, bench+1))

  rows = list(zip(col2, col1))
  cols = list(zip(seq1,seq2))
  
  for seat in taken:
    for i, j in rows:
      if i==seat or j==seat:
        # rows.pop(rows.index((i,j)))
        rows.remove((i,j))
    for i, j in cols:
      if i==seat or j==seat:
        cols.pop(cols.index((i,j)))
  
  return (len(rows)+len(cols))

print SeatingStudents(raw_input())


# def SeatingStudents(arr):

#   # code goes here
#   bench = arr[0]

#   # taken = [x for x in arr]
#   # taken.pop(0)
#   taken = list(x for x in arr)[1:]
#   n = len(taken)

#   col = 2
#   row = bench/2

#   total_possib = ((bench/col)+row)
#   available_seat = 0

#   if row == 1:
#     if n == 1:
#       return 0
#       break
#     return total_possib
#     break
  
#   if not n:
#     return total_possib
#     break
#   elif n == 1:
#     if row == 1:
#       return 0
#       break
#     elif row == 2:
#       miss = 2*(taken[0)]
#       available_seat = total_possib - miss
#       return available_seat
#       break
#   else:
#     # second_miss = 0
#     for ben in range(1, bench):
#       if n%2==0:
#         if ben
#         if (taken[ben]==1 and taken[ben==2]):
#           if (taken[ben]==(bench-1)) and (taken[ben]==bench):
#             miss = 2*()
        

#   second_miss = 0
#   n = len(taken)
#   for ben in range(2,n-1):
#     value = 3*(taken[ben])
#     second_miss+=value
  
#   final_miss = first_miss + second_miss
#   available_seat = total_possib - final_miss


#   return available_seat
