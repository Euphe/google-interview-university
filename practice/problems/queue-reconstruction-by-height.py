"""
https://leetcode.com/problems/queue-reconstruction-by-height/#/description

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""
def check_invariant(queue, i, person):
    #check that in queue[:i] there are person[1] people that have height >= person[0]
    h = person[0]
    n = person[1]
    
    cur_n = 0
    for i in range(i):
        q_h = queue[i][0]
        if q_h >= h:
            cur_n+=1
        if cur_n > n:
            return False
    if cur_n < n:
        return False
    return True
    
def find_person_pos(queue, person):
    h = person[0]
    n = person[1]
    
    cur_n = 0
    target = None
    for i in range(len(queue)):
        q_h = queue[i][0]
        if q_h >= h:
            cur_n+=1
        if cur_n > n:
            target = i
            break
    if not target:
        target = len(queue)
    return target

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []

        #first sort by n
        ppl_sorted = sorted(people, key=lambda x: 10000000*x[1]+x[0])
        
        queue = []
        queue.append(ppl_sorted.pop(0))

        while ppl_sorted:
            person = ppl_sorted.pop(0)
            queue.insert(find_person_pos(queue, person), person)
        return queue

solution = Solution()
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]


"""barely accepted, terrible solution. Thats pretty close to bruteforce!"""

#Real solution:

class Solution(object):
    def reconstructQueue(self, people):
        if not people: return []

        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, res = {}, [], []
        
        for i in range(len(people)):
            p = people[i]

            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

            print('person', p)
            print('state:')
            print('\t', peopledct)
            print('\t', height)
            print('\t', res)
        height.sort()      # here are different heights we have

        print('Sorting from tallest group')
        # sort from the tallest group
        for h in height[::-1]:
            print('taking group', h)
            peopledct[h].sort()
            print('sorted group', peopledct[h])
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])
                print('res', res)
        return res

solution = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
solution.reconstructQueue(people)