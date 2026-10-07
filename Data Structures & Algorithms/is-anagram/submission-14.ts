class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length != t.length) return false;

        const counts: number[] = new Array(26).fill(0);
        const ref: number = 'a'.charCodeAt(0);

        for (let i: number = 0; i < s.length; i++) {
            counts[s.charCodeAt(i) - ref]++;
            counts[t.charCodeAt(i) - ref]--;
        }

        return counts.every(x => x === 0);
    }
}
