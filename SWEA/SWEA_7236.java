import java.util.*;

public class SWEA_7236 {
	static int[] dx = { -1, 1, 0, 0, 1, 1, -1, -1 };
	static int[] dy = { 0, 0, -1, 1, -1, 1, -1, 1 };
	static char[][] matrix;
	static int N;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			N = sc.nextInt();
			int cnt = 1;
			matrix = new char[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					matrix[i][j] = sc.next().charAt(0);
				}
			}
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (matrix[i][j] == 'W') {
						int tmp = bfs(i, j);
						cnt = tmp > cnt ? tmp : cnt;
					}
				}
			}
			System.out.println("#" + test_case + " " + cnt);

		}
	}

	private static int bfs(int i, int j) {
		// TODO Auto-generated method stub
		int cnt = 0;
		for (int idx = 0; idx < 8; idx++) {
			int x = i + dx[idx];
			int y = j + dy[idx];
			if (x < 0 || x >= N || y < 0 || y >= N)
				continue;
			if (matrix[x][y] == 'W')
				cnt++;
		}

		return cnt;

	}

}
