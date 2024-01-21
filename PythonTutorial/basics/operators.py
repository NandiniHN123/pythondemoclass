'''
operators: symbols which performs any operations on one or more variables
1. Airthmetic operators : +, -, *, /, %, **(power),//(int division)
2. logical/Boolean operators: AND OR NOT
3. Relational/comparison operators: >, <, >=, <=, ==,!=
4. Assigning operator: =
5. Negation operator: -
6. Membership operator: in, not in
7. Identity operator: is, is not
'''
a="abc"
b="ABC"
c=a is b
print(c)
print(id(a))
print(id(b))