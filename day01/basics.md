## If-Else
- Used for decision making
- elif = multiple conditions

## Mistakes
- Used = instead of ==
- Forgot to increment loop → infinite loop
- Crashed program due to int(input()) without validation

## Patterns
- Prime check → loop till sqrt(n)
- Reverse number → use %10 and //10
- Binary conversion → divide by 2 and store remainder

## Insights
- Use dictionary instead of list for flags
- Use try-except for safe input
- Use float('-inf') for tracking max values

## Weak Points
- Still slow in nested loop logic
- Need more practice on pattern problems

## Snippets

### Safe Input
def get_int(prompt):
   while True:
      try:
         return int(input(prompt))
      except:
         print("Invalid input")