package problem;

import java.util.*;

public class SWEA_7465 {
	static int N, M, matrix[]; // 사람 수, 관계 수, 집합 배열
	static HashSet<Integer> set; // 몇 개의 무리가 존재하는지 계산

	public static int findSet(int x) {
		if (x == matrix[x])
			return x;
		return matrix[x] = findSet(matrix[x]);
	}

	public static boolean union(int x, int y) {
		int xRoot = findSet(x);
		int yRoot = findSet(y);
		if (xRoot == yRoot)
			return false;
		matrix[yRoot] = xRoot;
		return true;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();

		for (int test_case = 1; test_case <= T; test_case++) {
			// 초기화
			N = sc.nextInt();
			M = sc.nextInt();
			matrix = new int[N + 1];
			set = new HashSet<>();
			for (int i = 1; i <= N; i++) {
				matrix[i] = i;
			}
			for (int i = 0; i < M; i++) {
				int from = sc.nextInt();
				int to = sc.nextInt();
				union(from, to);
			}
			// 각 번호의 루트를 파악해서 그 루트를 set 자료구조에 삽입
			for (int i = 1; i <= N; i++) {
				set.add(findSet(i));
			}
			// set의 크기가 곧 결과
			System.out.println("#" + test_case + " " + set.size());
		}
	}

}
