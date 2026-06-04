class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];

        for (int temp = 0; temp < temperatures.length - 1; temp++) {
            for (int next_temp = temp + 1; next_temp < temperatures.length; next_temp++) {
                if (temperatures[next_temp] > temperatures[temp]) {
                    res[temp] = next_temp - temp;
                    break;
                }  
            }
        }
        return res;
    }
}
