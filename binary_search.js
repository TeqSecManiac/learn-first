var search = function(nums, target) {
  let lo = 0
  let hi = nums.length
  let mid

  while(lo <= hi) {
    mid = Math.floor((lo + hi)/2)

    if (nums[mid] === target) {
      return mid
    } else if (nums[mid] > target) {
      hi = mid - 1
    } else {
      lo = mid + 1
    }
  }
  return -1
};
