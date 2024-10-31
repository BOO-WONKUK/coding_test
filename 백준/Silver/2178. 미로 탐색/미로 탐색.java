import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] dx = {0,0,-1,1};
        int[] dy = {-1,1,0,0};
        boolean[][] visited = new boolean[N][M];
        int[][] A = new int[N][M];
        
        for (int i = 0 ; i < N ; i++){
            st = new StringTokenizer(br.readLine());
            String line = st.nextToken();
            for (int j = 0 ; j < M ; j++){
                A[i][j] = Integer.parseInt(line.substring(j,j+1));
            }
        }

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0,0});
        visited[0][0] = true;
        while (!q.isEmpty()){
            int now[] = q.poll();
            int i = now[0];
            int j = now[1];
            for (int k = 0 ; k < 4 ; k++){
                int ni = i + dx[k];
                int nj = j + dy[k];
                if (ni >= 0 && nj >= 0 && ni < N && nj < M){
                    if (A[ni][nj] == 1 && visited[ni][nj] == false){
                        visited[ni][nj] = true;
                        A[ni][nj] = A[i][j] + 1;
                        q.add(new int[] {ni,nj});

                    }
                }
            }
        }
        System.out.print(A[N-1][M-1]);
    }
}