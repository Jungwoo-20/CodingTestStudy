import java.util.*;

public class BOJ_7576 {
	static int[] dx = new int[] { 1, -1, 0, 0 };
	static int[] dy = new int[] { 0, 0, 1, -1 };
	static Scanner sc;
	static int[][] matrix;
	static Queue<int[]> queue;
	static boolean flag;
	static int res;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		sc = new Scanner(System.in);
		int M = sc.nextInt();
		int N = sc.nextInt();
		queue = new LinkedList<int[]>();
		matrix = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				matrix[i][j] = sc.nextInt();
				if (matrix[i][j] == 1) {
					queue.add(new int[] { i, j });
				}
			}
		}
		while (!queue.isEmpty()) {
			int[] data = queue.poll();
			int x = data[0];
			int y = data[1];
			for (int i = 0; i < 4; i++) {
				int _x = x + dx[i];
				int _y = y + dy[i];
				if (0 <= _x && _x < N && 0 <= _y && _y < M && matrix[_x][_y] == 0) {
					matrix[_x][_y] = matrix[x][y] + 1;
					queue.add(new int[] { _x, _y });
				}
			}
		}
		flag = false;
		res = -2;
		for (int[] ma : matrix) {
			for (int m : ma) {
				if (m == 0) {
					flag = true;
				}
				res = Math.max(res, m);
			}
		}
		if (flag) {
			System.out.println(-1);
		} else if (res == -1) {
			System.out.println(0);
		} else {
			System.out.println(res - 1);
		}
	}

}
