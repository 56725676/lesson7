first = int(input('введите целое число:  '))
second = int(input('введите целое число:  '))
third = int(input('введите целое число:  '))
if first == second == third:
  print('3')
elif first == second:
  print('2')
elif second == third:
  print('2')
elif third == first:
  print('2')
  #не использовал операторы or, and и not, потому что в примечании сказано постараться справиться без них.
else:
  print('0')

#first = int(input('введите целое число:  '))
#second = int(input('введите целое число:  '))
#third = int(input('введите целое число:  '))
#if first == second == third:
#  print('3')
#elif first == second or second == third or third == first:
#  print('2')
#else:
#print('0')
#так было бы с операторами