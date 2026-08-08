# age = 17
# if age>= 18:
#     print ('You are eligible to vote')
# else:
#     print('you are not eligible to vote')

# if-elif-else ladder
# score = 0
# if score >= 90:
#     print('You got an A grade')
# elif score >=80:
#     print('You got a B grade')
# elif score >= 70:
#     print('You got a C grade')
# elif score >= 60:
#     print('You got a D grade')
# elif score >= 50:
#     print('You got a E grade')
# else:
#     print('You got a F grade')

# sum = 10
# if sum >=10:
#     if sum >10:
#         print('Super')
#     else:
#         print('okayish')
# else:
#     print('Not Optimum')

# remaining_budget = 45.00

# if remaining_budget == 0:
#     print("CRITICAL: Ads have stopped! Budget is completely empty.")
# elif remaining_budget < 100:
#     print("WARNING: Budget is running low. Please alert the client.")
# else:
#     print("Status: Active. Budget looks healthy.")


# fruits = ["apple","banana","cherry"]
# for i in fruits:
#     print(i)

# for i in range(1,10):
#     print(i)

# top_clients = ["Nike", "Blue Bottle Coffee", "Local Gym LLC"]

# for rank, client in enumerate(top_clients, start=1):
#     print(f"Rank #{rank}: {client}")

# keywords = ["running shoes", "espresso beans"]
# searches = [45000, 3400]

# for word, volume in zip(keywords, searches):
#     print(f"The word '{word}' gets {volume} searches per month.")
   
pen = ['blue','green','black','red']
count = 1
while count <= 3:
    for i in pen:
        print(f"Count is {i} - {count}")
    count += 1 
    # count += 1 => count = count + 1

# count = 4
# while count >= 3:
#     print(f"Count is {count}")
#     count -= 1 
# for num in range(1, 10):
#     if num == 5:
#         break
#     print(num)
    
# for item in [1, 2, 3]:
#     print(item)
# else:
#     print("Loop finished with no break interruptions!") 

keywords = ['red','blue','pink']
sample = ['apple', 'mango','pear']
for x in keywords:
    for y in sample:
        print(x,y)

