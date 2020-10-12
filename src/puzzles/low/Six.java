package puzzles.low;

import java.util.stream.IntStream;

public class Six {
    public static void main(String[] args) {
        int sumOfSquares = IntStream.range(1, 101).map(x -> x*x).reduce(0, Integer::sum);
        int sumofVals = IntStream.range(1, 101).reduce(0, Integer::sum);
        System.out.println(sumOfSquares - sumofVals*sumofVals);
    }
}
