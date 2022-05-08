import java.awt.Point;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_1697 {
	static Scanner sc = new Scanner(System.in);
	static int N, K;
	static boolean visited[];

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		N = sc.nextInt();
		K = sc.nextInt();
		visited = new boolean[100001];
		if (N == K) {
			System.out.println(0);
			return;
		} else {
			bfs();
		}
	}

	private static void bfs() {
		Queue<Point> queue = new LinkedList<Point>();
		queue.add(new Point(N, 0)); // 수빈이의 현재 위치와 이동 횟수를 기록
		while (!queue.isEmpty()) {
			Point point = queue.poll();
			int n = point.x;
			int cnt = point.y;
			if (n == K) {
				System.out.println(cnt);
				return;
			}
			visited[n] = true;
			// 모든 조건에 대해 방문한적이 없어야 함.
			// 왼쪽 한칸
			if (n - 1 >= 0 && !visited[n - 1]) {
				queue.add(new Point(n - 1, cnt+1));
			}
			// 오른쪽 한칸
			if (n + 1 <= 100000 && !visited[n + 1]) {
				queue.add(new Point(n + 1, cnt+1));
			}
			// 현재 위치의 두배 오른쪽 칸
			if (2 * n <= 100000 && !visited[2 * n]) {
				queue.add(new Point(2 * n, cnt+1));
			}
		}

	}

}
