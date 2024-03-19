def quickSort(nums,left,right):
  if left<right:
    pi = partition(nums,left,right)
    quickSort(nums,left,pi-1)
    quickSort(nums,pi+1,right)
    
def partition(nums,left,right):
  pivot = nums[right]
  i=left-1
  for j in range(left,right):
    if nums[j]<=pivot:
      i+=1
      nums[i],nums[j]=nums[j],nums[i]
  nums[i+1],nums[right]=nums[right],nums[i+1]
  return i+1

nums = [9,8,7,6,4,5,3,1,2]
quickSort(nums,0,len(nums)-1)
print(nums)
