class Graph :
    def __init__(self,value):
        self.value = value
        self.points = []

class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        nodes =[]
        for i in range(n):
            if i+1 > len(nodes) :
                nodes.append(Graph(nums[i]))
            for j in range(i+1,min(i+nums[i]+1,n)):
                if j +1 > len(nodes) :
                    nodes.append(Graph(nums[j]))
                nodes[i].points.append(j)
            print("node:",i ,nodes[i],nodes[i].points)
            print('===========================================================')
        # 寻找最短路径
        dis =[1<<31-1 for i in range(n)]
        dis[0]=0
        s={0}
        ns={i for i in range(n)} -s
        for v in nodes[0].points :
            dis[v] = 1
        while  ns :
            mx = 1<<31
            index = 0
            for v in ns :
                if dis[v] <  mx :
                    mx = dis[v]
                    index = v
            s.add(index)
            ns.remove(index)
            for v in nodes[index].points:
                if  dis[index] + 1 < dis[v] :
                    dis[v] = dis[index] + 1
        return dis[-1]

s=Solution()
s.jump([2,3,1,1,4])


