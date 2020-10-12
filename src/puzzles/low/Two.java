package puzzles.low;

public class Two {
    public static void main(String[] args) {
        long sum = 0;
        int first = 1;
        int second = 2;
        int end = 4000000;

        while (second < end) {
            if (second % 2 == 0) {
                sum += second;
            }
            int prev = first;
            first = second;
            second = prev + second;
        }
        System.out.println(sum);
    }
}
