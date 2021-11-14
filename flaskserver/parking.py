import requests
response = requests.get('https://api.iq.inrix.com/lots/v3?point=37.74638779388551%7C-122.42209196090698&radius=300', headers={ 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6InBlYzh4a2ZmbWoiLCJ0b2tlbiI6eyJpdiI6IjQzNDhiMDFhYTEzOGM0MGJhZTI2ZjU3MzBlOTY5YzlkIiwiY29udGVudCI6Ijc1YjUwZmNiODA1ODNlNTIxNWRkZTk2N2U5NWE0ZTM3YjY0MTllYmIxNGUzNGNmNjA3M2Q5MzVkMDJiMjg4MTBlYzQ5MDJmNTdhYmFhM2M2OTQ3YzNjNTIwNWYyZjk2NzQ2NjAxYTAwZThmZjdiN2UwYTQwY2UyM2FiYWU0Mjg1ZDM3OTEwZGMyZjc5MGFiZWFkNGYzYTk3YjNmYzcyNGI1MDQ3N2E4ZmEwNDgyYmU4ODRkYzVkY2U5NzA3Yzc3MmMxYzU3ZGY2Yzk3OWNjNmE0MDYwY2YxZjJkODc0YWQ4NmFlNzU5MTViMDEwYTYzMjVhMmNjNWZiYmY5YmE5ZDA4Mjk4YzUzMWU4MjQ2ODlmYmQ3NTMxMzljYWNiNDBlY2ZkYTc1MTI2NWNhZjdlNzdiYzJkNDVjOThiMTA4Mjk1Y2VhMjlkZjFkZjkzNjQ0MzNhOWNiNGFmMDU3Y2QxZTIxMDg4Y2I3OTE4ZjhkYWZlMWI2MDgzZjNkODdlNjVhY2RmNzMyYTU2MzZiZTdlYTAzZmIxNDMyYjZhNmNmY2NiOWQ2NmNiMWZlODk5Y2VjZDIwNjI3ZDFhNDVjY2FmNjg3ODQ5MDIwZTcxNmRkMmE2ZDllOGMzZDU5NTlkYmI4YzM1NDU0ZGYxZDVkM2UwNWQwMTk4ZWY0NGQ3MzYzZmFjMGEyZjNjYWE3ZTBiZDllNGIxMzgyMmY4ODY5MzYyNGE3ZjBkNmZlZGQxYjBlZDc1ZTBhY2JlNzczMTliMjNlNjI0M2M1YTNlNTBmZjNiZjU5YjQzNzU4MzU5ZDc0YmQ1OThkOGNhM2EzZDQzZmZjMTM2YWIyMTYwM2E5ZDI0ZGVhYWI2MTljMjdkM2M3MDlmNDFlODk3In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI0MzQ4YjAxYWExMzhjNDBiYWUyNmY1NzMwZTk2OWM5ZCIsImNvbnRlbnQiOiI3ZDljN2NlYzkxNWEwZjA4MWQ4MWU5N2RjYzQxNmUzZjhkNDA4MTkwMGFjYzViZjQyOTRjZjc1MjMyODFiYjFhZjc0OTAzZmQzMThiOTZiYjkxMmIxYjZjIn0sImp0aSI6ImZkNTU4ZDI2LTBmMWItNDkxOS05MGMxLTFjMGFmZmI3ZTU3NyIsImlhdCI6MTYzNjg0NzUyMywiZXhwIjoxNjM2ODUxMTIxfQ.NVIGF4L0ZPKGeJStDLrH893RlSi5nXHM8rLSRr3B7_A' })

data = response.json()

street = data['result']
count = len(street)
print(count)


namepark = []
spacepark = []
latlongpark = []
for i in range(0,count):
    name = street[i]['name']
    spaces = street[i]['spacesTotal']
    latlong = street[i]['peps'][0]['pepPt']
    namepark.append(name)
    spacepark.append(spaces)
    latlongpark.append(latlong)
print(namepark)
print(spacepark)
print(latlongpark)

res = {i:[j, k] for i, j, k in zip(namepark, spacepark,latlongpark)}
  
# Printing resultant dictionary 
print ("dictionary is : " +  str(res))