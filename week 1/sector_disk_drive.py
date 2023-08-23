#Requirement
#Hardisk drive 16 GB, disk size multiple 1024 three times
#Sector Sizes 512 bytes

#The code
#create variable
disk_size = 16*1024*1024*1024
sector_size = 512

#process
sector_amount = disk_size/sector_size

#print value
print(sector_amount) # Should print 33554432.0