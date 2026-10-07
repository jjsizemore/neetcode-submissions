public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        var remDays = new Stack<int>();

        for (int i = temperatures.Length - 1; i >= 0; i--) {
            remDays.Push(temperatures[i]);
        }

        var daysPassed = new Stack<int>();

        var res = new int[temperatures.Length];

        for (int i = 0; i < res.Length; i++) {
            int curTemp = remDays.Pop();
            daysPassed.Push(curTemp);
            
            while (remDays.Count > 0 && remDays.Peek() <= curTemp) {
                daysPassed.Push(remDays.Pop());
            }

            if (remDays.Count == 0) {
                res[i] = 0;
            } else {
                res[i] = daysPassed.Count;
            }

            while (daysPassed.Count > 0) {
                remDays.Push(daysPassed.Pop());
            }
            if (remDays.Count > 0)
                remDays.Pop();
        }
        return res;
    }
}
