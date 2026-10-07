public class Solution {

    public string Encode(IList<string> strs) {
        var retVal = string.Concat(strs.Select(s => $"{s.Length}#{s}"));
        Console.WriteLine(retVal);
        return retVal;
    }

    public List<string> Decode(string s) {
        var retVal = new List<string>();
        int i = 0;

        while (i < s.Length) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }

            int.TryParse(s.Substring(i, j-i), out var strLen);
            j++;
            retVal.Add(s.Substring(j, strLen));
            i = j + strLen;
        }

        return retVal;
   }
}
