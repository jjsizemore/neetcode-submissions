public class Solution {
    public int MaxProfit(int[] prices) {
        int least = prices[0], most = prices[0], profit = 0;

        foreach (int price in prices) {
            if (price < least) {
                least = price;
                most = price;
            }
            most = Math.Max(most, price);
            profit = Math.Max(profit, most - least);
        }
        return profit;
    }
}
