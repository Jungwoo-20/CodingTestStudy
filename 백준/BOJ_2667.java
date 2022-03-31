import java.awt.Point;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_2667 {
	static Scanner sc = new Scanner(System.in);
	static int N;
	static int[][] matrix;
	static final int[] dx = { 0, 0, -1, 1 };
	static final int[] dy = { 1, -1, 0, 0 };
	static List<Integer> res;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		N = sc.nextInt();
		matrix = new int[N][N];
		res = new ArrayList<Integer>();
		for (int i = 0; i < N; i++) {
			String tmp = sc.next();
			for (int j = 0; j < N; j++) {
				matrix[i][j] = tmp.charAt(j) - '0';
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				// 단지번호 크기를 구하기 위한 카운팅 시작
				if (matrix[i][j] == 1) {
					bfs(i, j);
				}
			}
		}
		// 정렬
		Collections.sort(res);
		System.out.println(res.size());
		// 출력
		for(int i=0;i<res.size();i++) {
			System.out.println(res.get(i));
		}
		
		
	}

	private static void bfs(int i, int j) {
		Queue<Point> queue = new LinkedList<Point>();
		queue.add(new Point(i, j));
		matrix[i][j] = 0;
		int cnt = 1;
		while (!queue.isEmpty()) {
			Point point = queue.poll();
			int x = point.x;
			int y = point.y;
			for (int idx = 0; idx < 4; idx++) {
				int _x = x + dx[idx];
				int _y = y + dy[idx];
				if (_x >= 0 && _x < N && _y >= 0 && _y < N && matrix[_x][_y] == 1) {
					matrix[_x][_y] = 0;
					queue.add(new Point(_x,_y));
					cnt++;
				}
			}
		}
		res.add(cnt);
	}

}
