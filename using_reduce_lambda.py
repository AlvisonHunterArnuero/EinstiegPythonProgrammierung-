# Made with ❤️ in Python 3 by Alvison Hunter - November 24th, 2020
# # importing functools for reduce()
import functools
# importing operator for operator functions
import operator
# importing itertools for accumulate()
import itertools

#First, the regular way, pure a + B
def simple_sum():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    print(f'The simple sum of {a} plus {b} is: ',a + b)
    print('='*20)
#Let's call the function now
simple_sum()

#let us get simpler, we get the params and add them up now
def sum_with_params(a,b):
    print(f'The sum of {a} plus {b} with params is: ',int(a) + int(b))
    print('='*20)
#Let's call the function now
sum_with_params(10,20)

#not enough simple? ok let us go this way now...
def quick_sum():
    print('The quick sum is: ',(int(input('Enter first number: ')) + int(input('Enter second number: '))))
    print('='*20)
#Let's call the function now
quick_sum()

#Well, now is time for us to use some IIFE functions
#Let's call the function directly by invoking it with the params in the end
print('This function is invoked by itself, hence, we will only gonna see its results:')
(lambda a,b: print('The sum using IFFE functions is: ',a + b))(10,20)
print('='*20)

# sum more than two numbers, not problem sir, let's do it
def sum_list_items(numbers_lst):
    print('The sum with reduce is: ',functools.reduce(lambda x,y: x+y, numbers_lst))
    print('='*20)
#Let's call the function now
sum_list_items([10,20,45])

#not enough? let us do this using the operator & reduce module and the add method of it
def sum_list_with_operator(numbers_lst):
    print("The sum with reduce & operator.add is : ",functools.reduce(operator.add,numbers_lst))
    print('='*20)
#Let's call the function now
sum_list_with_operator([10,20,50,15])

#last, let us use the accumulate method to make these calculations
def sum_list_with_accumulate(numbers_lst):
    print("The acumulative sum with accumulate is : ",list(itertools.accumulate(numbers_lst,lambda x,y : x+y)))
    print('='*20)
#Let's call the function now
sum_list_with_accumulate([10,20,30,40])



