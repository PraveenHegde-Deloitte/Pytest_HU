#changing city Name

sampleDict = {
  "name": "praveen",
  "age":25,
  "salary": 8000,
  "city": "Sirsi"
}
v=sampleDict['city']
del sampleDict['city']
sampleDict['Location']=v
print(sampleDict)
