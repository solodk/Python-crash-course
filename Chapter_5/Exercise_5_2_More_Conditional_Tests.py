# Have at least one True and one False result for each of the following:
# Tests for equality and inequality with string
if 'cars' != 'Cars':
    print('cars is not equal to Cars')
if 'Cars' == 'Cars':
    print('Cars is equal to Cars')
# Tests using the lower() method
if 'Cars'.lower() != 'Cars':
    print('Cars.lower() is not equal to Cars')
if 'cars' == 'Cars'.lower():
    print('cars is equal to Cars.lower()')
# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
if 2 < 3:
    print('2<3')
if 3 <= 3:
    print('3<=3')
if 4 > 3:
    print('4>3')
if 3 >= 3:
    print('3>=3')
if 3 != 2:
    print('3!=2')
if 3 == 3:
    print('3==3')
# Tests using the and keyword and the or keyword
if 3 > 2 and 2 < 3:
    print('3>2 and 2<3')
if 1<0 or 1<2:
    print('1<0 or 1<2')
# Test whether an item is in a list
somelist = [1,2,3]
if 2 in somelist: 
    print('2 is in list')
# Test whether an item is not in a list
if 4 not in somelist:
    print('4 is not in list')
