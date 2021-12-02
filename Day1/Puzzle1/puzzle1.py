my_file = open("input.txt", "r")
content_list = my_file.readlines()

print(content_list)

def depth_increase(nums):
    total = 1
    for i in range(0, len(nums)):
        

        try:
            a = (int(nums[i])+ int(nums[i+1]) + int(nums[i+2]))
            b = (int(nums[i+1]) + int(nums[i+2]) + int(nums[i+3]))
            if a < b:
                total += 1
                print(a)
        
        except:
           pass
    
    return total


print(depth_increase(content_list))