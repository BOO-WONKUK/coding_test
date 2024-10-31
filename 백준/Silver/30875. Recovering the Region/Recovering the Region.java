import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        for (int i = 0; i < n; i++) {
            // 리스트의 요소를 문자열로 변환하여 " " 구분자로 연결
            String[] row = new String[n];
            Arrays.fill(row, String.valueOf(i + 1));
            System.out.println(String.join(" ", row));
        }
    }
}
