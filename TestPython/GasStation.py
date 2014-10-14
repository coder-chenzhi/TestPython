class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        now = 0
        end = len(gas) - 1
        count = 0

        while (now <= end):
        	count += gas[now] - cost[now]
        	#print "count =", count
        	now += 1
        	
        	while (count < 0 and now <= end):
        		count += gas[end] - cost[end]
        		#print "count =", count
        		end -= 1	

        if count >= 0:
        	return (end + 1) % len(gas)
        else:
        	return -1

s = Solution()
print s.canCompleteCircuit([1,2],[2,1])