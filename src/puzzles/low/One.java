package puzzles.low;

import java.util.stream.IntStream;

public class One {
    public static void main(String[] arg) {
        System.out.println(IntStream.range(0, 1000).filter(x -> x%3 == 0 || x%5 == 0).reduce(0,(ans,i)-> ans+i));
    }
}
