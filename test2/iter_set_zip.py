# python iter()
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)

# python set()
# Exemplu1
# initializing list
lis1 = [3, 4, 1, 4, 5]
# initializing tuple
tup1 = (3, 4, 1, 4, 5)
# Printing iterables before conversion
print("The list before conversion is : " + str(lis1))
print("The tuple before conversion is : " + str(tup1))
# The list before conversion is : [3, 4, 1, 4, 5]
# The tuple before conversion is : (3, 4, 1, 4, 5)
# Iterables after conversion are: (notice distinct and elements)
print("The list after conversion is : " + str(set(lis1)))
print("The tuple after conversion is : " + str(set(tup1)))
# The list after conversion is : {1, 3, 4, 5}
# The tuple after conversion is : {1, 3, 4, 5}
# Exemplu2
# initializing dict

dic1 = {4: 'geeks', 1: 'for', 3: 'geeks'}
# Printing dictionary before conversion
# internaly sorted
print("Dictionary before conversion is : " + str(dic1))
# Dictionary after conversion are:(notice lost keys)
print("Dictionary afer conversion is : " + str(set(dic1)))

# Output:
# Dictionary before conversion is : {1: 'for', 3: 'geeks', 4: 'geeks'}
# Dictionary afer conversion is : {1, 3, 4}

# python zip()
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

result1 = zip(number_list, str_list)
print("result1=", list(result1))
result2 = zip(number_list, str_list)
print("result2=", tuple(result2))
result3 = zip(number_list, str_list)
print("result3=", set(result3))

# Output:
# result1= [(1, 'one'), (2, 'two'), (3, 'three')]
# result2= ((1, 'one'), (2, 'two'), (3, 'three'))
# result3= {(1, 'one'), (2, 'two'), (3, 'three')}
