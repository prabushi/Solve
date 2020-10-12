package puzzles.low;

public class Five {
    public static void main(String[] args) {
        long val = 20;
        while(val % 20 != 0 || val % 19 != 0 || val % 18 != 0 || val % 17 != 0 || val % 16 != 0 ||
                val % 15 != 0 || val % 14 != 0 || val % 13 != 0 || val % 12 != 0 || val % 11 != 0) {
            val += 10;
        }
        System.out.println(val);
    }
}