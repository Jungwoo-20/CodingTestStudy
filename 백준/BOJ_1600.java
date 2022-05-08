import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_1600 {
	static Scanner sc;
	static int[][] matrix;
	static int[] dx = { 1, -1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static int[] hdx = { -2, -1, 1, 2, 2, 1, -1, -2 };
	static int[] hdy = { 1, 2, 2, 1, -1, -2, -2, -1 };
	static int[][] visited;
	static int K, W, H;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		sc = new Scanner(System.in);
		K = sc.nextInt();
		W = sc.nextInt();
		H = sc.nextInt();
		matrix = new int[H][W];
		visited = new int[H][W];
//		Arrays.fill(visited, -1); // 1차원 배열에서만 사용 가능
		for (int[] v : visited) {
			Arrays.fill(v, -1);
		}
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				matrix[i][j] = sc.nextInt();
			}
		}
		System.out.println(bfs());
	}

	private static int bfs() {
		Queue<Node> queue = new LinkedList<>();
		queue.offer(new Node(0, 0, 0, K));
		while (!queue.isEmpty()) {
			Node node = queue.poll();
			int x = node.x;
			int y = node.y;
			int cnt = node.cnt;
			int k = node.k;
			// 맨 오른쪽 아래
			if (x == H - 1 && y == W - 1) {
				return cnt;
			}
			for (int i = 0; i < 4; i++) {
				int _x = x + dx[i];
				int _y = y + dy[i];
				if (_x >= 0 && _x < H && _y >= 0 && _y < W && matrix[_x][_y] == 0) {
					// 방문하지 않았거나 k번 미만으로 방문할 수 있는 경우 update
					if (visited[_x][_y] == -1 || visited[_x][_y] < k) {
						visited[_x][_y] = k;
						queue.offer(new Node(_x, _y, cnt + 1, k));
					}
				}
			}
			// 말의 움직임처럼 이동할 수 있는 횟수가 남은 경우
			if (k > 0) {
				for (int i = 0; i < 8; i++) {
					int _x = x + hdx[i];
					int _y = y + hdy[i];
					if (_x >= 0 && _x < H && _y >= 0 && _y < W && matrix[_x][_y] == 0) {
						// 방문하지 않았거나 k-1번 미만으로 방문할 수 있는 경우 update
						if (visited[_x][_y] == -1 || visited[_x][_y] < k - 1) {
							visited[_x][_y] = k - 1;
							queue.offer(new Node(_x, _y, cnt + 1, k - 1));
						}
					}
				}
			}

		}
		return -1;
	}

}

// x 좌표, y 좌표, 이동 횟수, 말을 따라서 이동할 수 있는 잔여 횟수
class Node {
	int x;
	int y;
	int cnt;
	int k;

	public Node(int x, int y, int cnt, int k) {
		super();
		this.x = x;
		this.y = y;
		this.cnt = cnt;
		this.k = k;
	}

}
