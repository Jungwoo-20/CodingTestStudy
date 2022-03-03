package problem;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_1260 {
	static int N, M, V, matrix[][];
	static boolean[] visited;
	static Queue<Integer> queue;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		V = sc.nextInt();
		matrix = new int[N+1][N+1];
		queue = new LinkedList<Integer>();
		for (int i = 0; i < M; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			matrix[x][y] = matrix[y][x] = 1;
		}
		visited = new boolean[N + 1];
		dfs(V);
		System.out.println();
		bfs(V);
	}

	private static void bfs(int V) {
		// TODO Auto-generated method stub
		queue.add(V);
		visited[V] = false;
		while (!queue.isEmpty()) {
			V = queue.poll();
			System.out.print(V + " ");
			for (int i = 1; i <= N; i++) {
				if (visited[i] && matrix[V][i] == 1) {
					queue.add(i);
					visited[i] = false;
				}
			}
		}

	}

	private static void dfs(int V) {
		// TODO Auto-generated method stub
		visited[V] = true;
		System.out.print(V + " ");
		for (int i = 1; i <= N; i++) {
			if (!visited[i] && matrix[V][i] == 1) {
				dfs(i);
			}
		}
	}

}
