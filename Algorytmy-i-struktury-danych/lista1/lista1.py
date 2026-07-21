import random
import numpy
import time

# Przygotowanie tablic do testów

# main_table = numpy.arange(random.randint(5,7))

# for item in main_table:
#     main_table[item] = float(random.randint(1,100))

#-----------------------------------------------------------------------------

def insertionsort(table):
  for item in range(len(table)):
      temp = table[item]
      i = item - 1
      while(temp < table[i] and i >= 0):
         table[i+1] = table[i]
         i-=1
      if(i != item - 1):
         table[i+1] = temp
  return table

def insertionsortplus(table):
  count_e, count_p = 0,0
  for item in range(len(table)):
      temp = table[item]
      i = item - 1
      count_p += 1
      while(temp < table[i] and i >= 0):
         count_p += 1
         table[i+1] = table[i]
         count_e += 1
         i-=1
      if(i != item - 1):
         table[i+1] = temp
         count_e += 1
  return (count_p,count_e)

# print(insertionsortplus(main_table))
#print(insertionsort(main_table))


#------------------------------------------------------------------


def bubblesort(table):
   for item in range(1,len(table):
      for i in range(len(table)-item,0,-1):
         if(table[i] < table[i-1]):
            table[i], table[i-1] = table[i-1], table[i]
   return table


def bubblesortplus(table):
   count_e, count_p = 0,0
   for item in range(1,len(table)):
      for i in range(len(table)-item,0,-1):
         count_p += 1
         if(table[i] < table[i-1]):
            table[i], table[i-1] = table[i-1], table[i]
            count_e += 2
   return (count_p, count_e)


# print(main_table)
print(bubblesort([3,2,1]))


#------------------------------------------------------------------

def mergesort(table):
   def sort(table_a, table_b):
      #print(table_a," ",table_b)
      index_a, index_b = 0,0
      new_table = numpy.arange(len(table_a) + len(table_b))
      for index in new_table:
         if(index_a == len(table_a)):
            while (index_b < len(table_b)):
               new_table[index] = table_b[index_b]
               index_b += 1
               index += 1
            #print(new_table)
            return new_table
         
         elif(index_b == len(table_b)):
            while (index_a < len(table_a)):
               new_table[index] = table_a[index_a]
               index_a += 1
               index += 1
            #print(new_table)
            return new_table 
          
         if(table_a[index_a] < table_b[index_b]):
            new_table[index] = table_a[index_a]
            index_a += 1
         else:
            new_table[index] = table_b[index_b]
            index_b += 1
      return new_table
   
   if(len(table) == 1): return table
   if(len(table) == 2):
      if(table[1] < table[0]):
         table[0], table[1] = table[1], table[0]
      return table
   middle = len(table) // 2
   return sort(mergesort(table[:middle]), mergesort(table[middle:]))
      


def mergesortplus(table, main_lenght):
   count_e, count_p = 0,0
   def sort(table_a, table_b):
      nonlocal count_e, count_p
      #print(table_a," ",table_b)
      index_a, index_b = 0,0
      new_table = numpy.arange(len(table_a) + len(table_b))
      for index in new_table:
         if(index_a == len(table_a)):
            while (index_b < len(table_b)):
               new_table[index] = table_b[index_b]
               index_b += 1
               index += 1
               count_e += 1
            #print(new_table)
            return new_table
         
         elif(index_b == len(table_b)):
            while (index_a < len(table_a)):
               new_table[index] = table_a[index_a]
               index_a += 1
               index += 1
               count_e += 1
            #print(new_table)
            return new_table 
         
         count_p += 1
         if(table_a[index_a] < table_b[index_b]):
            new_table[index] = table_a[index_a]
            index_a += 1
            count_e += 1
         else:
            new_table[index] = table_b[index_b]
            count_e += 1
            index_b += 1
      return new_table
   
   if(len(table) == 1): return table
   if(len(table) == 2):
      count_p += 1
      if(table[1] < table[0]):
         table[0], table[1] = table[1], table[0]
         count_e += 2
      return table
   middle = len(table) // 2
   if(len(table) == main_lenght):
      sort(mergesortplus(table[:middle], main_lenght), mergesortplus(table[middle:], main_lenght))
      return (count_p, count_e)
   else:
      return sort(mergesortplus(table[:middle], main_lenght), mergesortplus(table[middle:],main_lenght))


# print(main_table)
# print(mergesortplus(main_table))

 #--------------------------------------------------------------------------

def mergesort21(table):
   def sort(table_a, table_b):
      #print(table_a," ",table_b)
      index_a, index_b = 0,0
      new_table = numpy.arange(len(table_a) + len(table_b))
      for index in new_table:
         if(index_a == len(table_a)):
            while (index_b < len(table_b)):
               new_table[index] = table_b[index_b]
               index_b += 1
               index += 1
            #print(new_table)
            return new_table
         
         elif(index_b == len(table_b)):
            while (index_a < len(table_a)):
               new_table[index] = table_a[index_a]
               index_a += 1
               index += 1
            #print(new_table)
            return new_table 
          
         if(table_a[index_a] < table_b[index_b]):
            new_table[index] = table_a[index_a]
            index_a += 1
         else:
            new_table[index] = table_b[index_b]
            index_b += 1
      return new_table
   
   if(len(table) == 1): return table
   if(len(table) == 2):
      if(table[1] < table[0]):
         table[0], table[1] = table[1], table[0]
      return table
   middle = len(table) // 3
   return sort(mergesort21(table[:middle]), mergesort21(table[middle:]))
      

def mergesort21plus(table, main_lenght):
   count_e, count_p = 0,0
   def sort(table_a, table_b):
      nonlocal count_e, count_p
      #print(table_a," ",table_b)
      index_a, index_b = 0,0
      new_table = numpy.arange(len(table_a) + len(table_b))
      for index in new_table:
         if(index_a == len(table_a)):
            while (index_b < len(table_b)):
               new_table[index] = table_b[index_b]
               index_b += 1
               index += 1
               count_e += 1
            #print(new_table)
            return new_table
         
         elif(index_b == len(table_b)):
            while (index_a < len(table_a)):
               new_table[index] = table_a[index_a]
               index_a += 1
               index += 1
               count_e += 1
            #print(new_table)
            return new_table 
         
         count_p += 1
         if(table_a[index_a] < table_b[index_b]):
            new_table[index] = table_a[index_a]
            index_a += 1
            count_e += 1
         else:
            new_table[index] = table_b[index_b]
            index_b += 1
            count_e += 1
      return new_table
   
   if(len(table) == 1): return table
   if(len(table) == 2):
      count_p += 1
      if(table[1] < table[0]):
         table[0], table[1] = table[1], table[0]
         count_e += 2
      return table
   middle = len(table) // 3
   if(len(table) == main_lenght):
      sort(mergesort21plus(table[:middle], main_lenght), mergesort21plus(table[middle:], main_lenght))
      return (count_p, count_e)
   else:
      return sort(mergesort21plus(table[:middle], main_lenght), mergesort21plus(table[middle:], main_lenght))


# print(main_table)
# print(mergesort21plus(main_table))

 #--------------------------------------------------------------------------
def tests(size = 6000):
      
   main_table = numpy.arange(size)
   for item in main_table:
      main_table[item] = float(random.randint(1,500))
   
   copy1, copy2, copy3 = numpy.copy(main_table), numpy.copy(main_table), numpy.copy(main_table)
   results = []
   start = time.time()
   results.append([size, insertionsortplus(copy1), "insertionsort"])
   end = time.time()
   results[0].append(end-start)
   start = time.time()
   results.append([size, bubblesortplus(copy2), "bubblesort"])
   end = time.time()
   results[1].append(end-start)
   start = time.time()
   results.append([size, mergesortplus(copy3, len(copy3)), "mergesort"])
   end = time.time()
   results[2].append(end-start)
   start = time.time()
   results.append([size, mergesort21plus(main_table, len(main_table)), "mergesort21"])
   end = time.time()
   results[3].append(end-start)

   return results

#print(tests())