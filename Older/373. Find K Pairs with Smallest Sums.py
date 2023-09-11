import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        k = min(len(nums1) * len(nums2), k)
        res = []
        q = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(q, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        while q and len(res) < k:
            _, i, j = heapq.heappop(q)
            res.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return res

nums1 = [1,2]
nums2 = [3]
k = 3
