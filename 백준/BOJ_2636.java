import java.awt.Point;
import java.util.*;

public class BOJ_2636 {
	static Scanner sc = new Scanner(System.in);
	static int n, m, cnt;
	static int[][] matrix;

	static final int[] dx = { 0, 0, -1, 1 };
	static final int[] dy = { 1, -1, 0, 0 };
	static List<Integer> list = new ArrayList<>();

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		n = sc.nextInt();
		m = sc.nextInt();
		matrix = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				matrix[i][j] = sc.nextInt();
			}
		}
		cnt = 0;
		while (true) {
			if (bfs() == 0) {
				break;
			}
			cnt++;
		}
		System.out.println(cnt);
		System.out.println(list.get(list.size() - 2));
	}

	private static int bfs() {
		// TODO Auto-generated method stub
		boolean[][] visited = new boolean[n][m];
		Queue<Point> queue = new LinkedList<Point>();
		queue.add(new Point(0, 0));
		visited[0][0] = true;
		int cheseCnt = 0;
		while (!queue.isEmpty()) {
			Point point = queue.poll();
			int x = point.x;
			int y = point.y;
			for (int i = 0; i < 4; i++) {
				int _x = x + dx[i];
				int _y = y + dy[i];
				// 이동 가능하고 방문하지 않은 경우
				if (_x >= 0 && _x < n && _y >= 0 && _y < m && !visited[_x][_y]) {
					// 치즈가 아닌 경우
					if (matrix[_x][_y] == 0) {
						visited[_x][_y] = true;
						queue.add(new Point(_x, _y));
					} else if(matrix[_x][_y] == 1) { // 치즈인 경우 -> 녹인 치즈 개수를 하나씩 증가
						visited[_x][_y] = true;
						matrix[_x][_y] = 0;
						cheseCnt++;
					}
				}
			}
		}
		list.add(cheseCnt);
		return cheseCnt;
	}

}
