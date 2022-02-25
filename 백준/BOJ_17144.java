import java.util.*;

public class BOJ_17144 {
	static Scanner sc;
	static int[] dx = new int[] { -1, 1, 0, 0 };
	static int[] dy = new int[] { 0, 0, -1, 1 };
	static int R, C, T;
	static int[][] matrix;
	static int airUp, airDown;
	static int res;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		init();

		for (int cnt = 0; cnt < T; cnt++) {
			// 먼지 퍼지기
			spread();
			// 공기 청정기 동작
			// 1. 상단 (우 -> 상 -> 좌 -> 하)
			up();
			// 2. 하단 (우 -> 하 -> 좌 -> 상)
			down();
		}

		// 총합 계산
		sum();
		System.out.println(res);

	}

	private static void init() {
		sc = new Scanner(System.in);
		R = sc.nextInt();
		C = sc.nextInt();
		T = sc.nextInt();
		airUp = -1;
		airDown = -1;
		matrix = new int[R][C];
		res = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				matrix[i][j] = sc.nextInt();
			}
		}
		// 공기 청정기 위치 찾기
		for (int i = 0; i < R; i++) {
			if (matrix[i][0] == -1) {
				airUp = i;
				airDown = i + 1;
				break;
			}
		}
	}

	private static void spread() {
		// TODO Auto-generated method stub
		int[][] air = new int[R][C];
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				// 미세 먼지가 있어야 하고 공기청정기인 경우 불가능
				if (matrix[i][j] != 0 && matrix[i][j] != -1) {
					int density = 0; // 농도
					for (int idx = 0; idx < 4; idx++) {
						int _x = i + dx[idx];
						int _y = j + dy[idx];
						if (0 <= _x && _x < R && 0 <= _y && _y < C && matrix[_x][_y] != -1) {
							// 확산 배열에 저장
							air[_x][_y] += matrix[i][j] / 5;
							density += matrix[i][j] / 5;
						}
					}
					// 확산이 종료된 곳에 농도 감소
					matrix[i][j] -= density;
				}
			}
		}
		// 기존 배열과 확산된 배열의 값을 합쳐야함
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				matrix[i][j] += air[i][j];
			}
		}
	}

	private static void up() {
		// (우 -> 상 -> 좌 -> 하)
		int[] upDx = new int[] { 0, -1, 0, 1 };
		int[] upDy = new int[] { 1, 0, -1, 0 };
		int dire = 0; // 디폴트 우
		int startX = airUp;
		int startY = 1;
		int startAir = 0;
		while (true) {
			int _startX = startX + upDx[dire];
			int _startY = startY + upDy[dire];
			// 자기 자리로 복귀(종료 조건)
			if (_startX == airUp && _startY == 0) {
				matrix[startX][startY] = startAir;
				break;
			}
			// 배열 범위 확인
			if (_startX < 0 || _startX >= R || _startY < 0 || _startY >= C) {
				dire++; // 한 번 돌면 사이클이 끝나기 때문에 나머지 연산으로 하지 않아도 무방
				continue;
			}
			// 현재 위치의 값을 다음에 사용해야 하기 때문에 tmp에 미리 저장
			int tmp = matrix[startX][startY];
			// 이전에 농도를 현재 위치에 저장(1번쨰 위치는 0이되고, 2는 1번째를 가져옴)
			matrix[startX][startY] = startAir;
			// 그 부분을 구현
			startAir = tmp;
			// 포인터 이동
			startX = _startX;
			startY = _startY;

		}
	}

	private static void down() {
		// (우 -> 하 -> 좌 -> 상)
		int[] downDx = new int[] { 0, 1, 0, -1 };
		int[] downDy = new int[] { 1, 0, -1, 0 };
		int dire = 0; // 디폴트 우
		int startX = airDown;
		int startY = 1;
		int startAir = 0;

		while (true) {
			int _startX = startX + downDx[dire];
			int _startY = startY + downDy[dire];
			// 자기 자리로 복귀(종료 조건)
			if (_startX == airDown && _startY == 0) {
				matrix[startX][startY] = startAir;
				break;
			}
			// 배열 범위 확인
			if (_startX < 0 || _startX >= R || _startY < 0 || _startY >= C) {
				dire++; // 한 번 돌면 사이클이 끝나기 때문에 나머지 연산으로 하지 않아도 무방
				continue;
			}
			// 현재 위치의 값을 다음에 사용해야 하기 때문에 tmp에 미리 저장
			int tmp = matrix[startX][startY];
			// 이전에 농도를 현재 위치에 저장(1번쨰 위치는 0이되고, 2는 1번째를 가져옴)
			matrix[startX][startY] = startAir;
			// 그 부분을 구현
			startAir = tmp;
			// 포인터 이동
			startX = _startX;
			startY = _startY;
		}
	}

	private static void sum() {
		for (int[] ma : matrix) {
			for (int m : ma) {
				if (m > 0) {
					res += m;
				}
			}
		}
	}
}
