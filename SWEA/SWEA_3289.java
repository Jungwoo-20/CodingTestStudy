package problem;

import java.util.*;

public class SWEA_3289 {
	static int n, m, matrix[];

	public static void makeSet() {
		matrix = new int[n + 1];
		for (int i = 1; i <= n; i++) {
			matrix[i] = i;
		}
	}

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
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			// 입력 및 초기화
			n = sc.nextInt();
			m = sc.nextInt();
			makeSet();
			// 결과 출력
			System.out.print("#" + test_case + " ");
			for (int i = 0; i < m; i++) {
				int num = sc.nextInt();
				int a = sc.nextInt();
				int b = sc.nextInt();
				// 합집합은 0 a b의 형태로 입력이 주어진다.
				if (num == 0) { // union
					union(a, b);
				} else { // find a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.
					if (findSet(a) == findSet(b))
						System.out.print(1);
					else
						System.out.print(0);
				}
			}
			System.out.println();

		}
	}

}
