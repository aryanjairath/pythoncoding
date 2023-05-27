data = [2,5,104,105,110,120,
        130,130,150,160,170,183,185,187,188,191,350,360]
# del data[0:2]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# stop = 0
# for index, value in enumerate(data):
#         if value >= min_valid:
#                 stop = index
#                 break
#         if value < max_valid:
#                 stop = index
#                 break
# del data[:stop]
# print(data)

start = 0
stop = 0
for index in range(len(data) -1, -1, -1):
        if data[index] <= max_valid:
                start = index+1
                break
print(start)
del data[start:]
del data[:stop]

print(data)
