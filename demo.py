class pari_Element:
    def twoSum(self, nums, target):
        lookup={}

        for i , num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target-num],i)
            lookup[num] = i

value = int(input("Enter Target : "))
print("Index1 = %d, Index2 = %d"% pari_Element().twoSum((10,20,30,40,50,60,70),value))