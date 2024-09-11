class Solution:
    def candy(self, ratings):
        n = len(ratings)
        # gives each chiild one candy
        candies = [1]*n

        # left to right pass
        for i in range (1, n):
            # if the rating to the left is less than the current add one more than the left rating
            if ratings[i] > ratings[i -1]:
                candies[i] = candies[i -1] + 1

        # right to left pass
        for i in range(n -2, -1, -1):
            # if the rating of the current child  is greater than on the right increase the candy
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies [i], candies[i + 1] + 1)

        return sum(candies)
    
ratings = [3, 0, 2, 5, 1]
solution = Solution()
print(solution.candy(ratings))
            
        