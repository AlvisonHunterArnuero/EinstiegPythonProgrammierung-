L = [8,6,11,3]

def two_sum(nums,target):
    d={}

    for i in range(len(nums)):
        if target - nums[i] in d:
            print(d)
            return [d[target-nums[i]],i]

        d[nums[i]]=i

    return -1


two_sum(L,9)
