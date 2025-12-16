guests = ['Hussain','Noman','Yasir','Farhan','Ayan']
 
print(f"Dear {guests[0]}, You are invited to have dinner at my house.")
print(f"Dear {guests[1]}, You are invited to have dinner at my house.")
print(f"Dear {guests[2]}, You are invited to have dinner at my house.")
print(f"Dear {guests[3]}, You are invited to have dinner at my house.")
print(f"Dear {guests[4]}, You are invited to have dinner at my house.")

print(f"{guests[0]} cant make to dinner.")
guests[0] = 'Ali'
print(f"Dear {guests[0]}, You are invited to have dinner at my house.")

print("I found bigger dinner table so, I am inviting three more person.")
guests.append('Mansoor')
guests.insert(0,'Arham')
guests.insert(2, 'Abdullah')

print(f"Dear {guests[0]}, You are invited to have dinner at my house.")
print(f"Dear {guests[2]}, You are invited to have dinner at my house.")
print(f"Dear {guests[-1]}, You are invited to have dinner at my house.")

print("Bigger cant make it on time.So,I am inviting two people")
guests.pop(-1)
print(f"Sorry, Mansoor dinner is canceled.")

print(len(guests))


