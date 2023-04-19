import requests, os 
user_id = input("What is the ID of the account you want info for? ")

url = 'https://users.roblox.com/v1/users/' + user_id

x = requests.get(url)

response = requests.get(url)

for k,v in response.json().items():
  print(f'{k}: {v}')
  
os.system('pause')
