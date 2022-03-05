package problem;

import java.util.*;

// 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성하시오.
public class SWEA_1238 {
	static int N, start, res; // 입력 받는 데이터, 길이, 결과
	static boolean[] visited; // 방문 처리 배열
	static int[][] matrix; // 인접행렬
	static Queue<Integer> queue; // bfs를 위한 큐

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int test_case = 1; test_case <= 10; test_case++) {
			// 입력
			N = sc.nextInt();
			start = sc.nextInt();
			res = Integer.MIN_VALUE; // 가장 작은 값
			visited = new boolean[101];
			matrix = new int[101][101];
			queue = new LinkedList<Integer>();

			for (int i = 1; i <= N / 2; i++) {
				int from = sc.nextInt();
				int to = sc.nextInt();
				matrix[from][to] = 1;
			}
			// solution
			bfs();
			// 결과
			System.out.println("#" + test_case + " " + res);
		}
	}

	private static void bfs() {
		// 초기 상태(시작점 값 삽입)
		queue.add(start);
		visited[start] = true;
		int tmp = -99; // 방문된 가장 큰 수를 저장하기 위한 변수
		while (!queue.isEmpty()) { // 큐가 비어있을 때까지 반복
			// 큐 사이즈만큼 반복하기 위함 -> for문에 바로 사용하게 되는 경우 poll문제로 오류 발생
			// 초기 2의 경우 7과 15를 갈 수 있기 떄문에 2가지 경우를 모두 poll하면서 탐색
			tmp = -99; // while이 반복될 때마다 값 초기화 (중요!!!)
			int size = queue.size();
			for (int i = 0; i < size; i++) {
				int cnt = queue.poll();
				// tmp값보다 현재 방문할 예정인 값이 더 크다면 tmp의 값을 바꿔줌
				tmp = tmp < cnt ? cnt : tmp;
				// cnt가 방문할 수 있는 모든 곳을 반복문으로 탐색
				for (int j = 1; j < matrix[cnt].length; j++) {
					// 갈 수 있는 곳이고 방문하지 않은 경우면
					if (matrix[cnt][j] == 1 && !visited[j]) {
						// 큐에 삽입하고 방문 처리
						queue.add(j);
						visited[j] = true;
					}
				}
			}
		}
		// 현재 출력 예정인 res보다 최근에 방문했던 tmp가 더 큰 경우 res 변경
		res = res < tmp ? tmp : res;
	}

}
