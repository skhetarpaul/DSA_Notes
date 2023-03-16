'''nCk equivalents to n!/((n-k)!*k!)'''
'''nck in recursive terms can be written as take + nottake i.e. take = fn(n-1, k-1) and nottake = fn(n-1, k)
where if k>n-> ans is 0 or n==k or k==0 ans is 1'''

# https://www.geeksforgeeks.org/permutation-coefficient/
'''nPk can be represented as :
take = k*fn(n-1, k-1)
nottake = fn(n-1, k)
'''



'''

Nth Catalan number:
Follow the steps below to implement the above recursive formula

Base condition for the recursive approach, when n <= 1, return 1
Iterate from i = 0 to i < n
Make a recursive call catalan(i) and catalan(n – i – 1) and keep adding the product of both into res.
Return the res.'''