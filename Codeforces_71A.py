new_variable=int(input())

for i in range(new_variable):
  word=input()
  if len(word)<=10:
    print(word)
  
  else:
    new=word.lower()
    test=word[0]
    test_1=len(word[1:-1])
    test_2=word[-1]
    print(f'{test}{test_1}{test_2}')
  

