import java.awt.Point;
import java.util.*;

public class SWEA_1767 {
	static int N; // 배열로 주어지는 크기
	static int[][] matrix;
	// 최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이의 합을 구하고자 한다.
	static int coreCnt, coreLen;
	static List<Point> coreList;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();

		for (int test_case = 1; test_case <= T; test_case++) {
			N = sc.nextInt();
			matrix = new int[N + 1][N + 1];
			coreCnt = Integer.MIN_VALUE;
			coreLen = Integer.MAX_VALUE;
			coreList = new ArrayList<Point>();
			// 0은 빈 셀, 1은 코어 그 외의 숫자는 없다.
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					int val = sc.nextInt();
					matrix[i][j] = val;
					// 멕시노스의 가장자리에 위치한 Core는 이미 전원이 연결된 것으로 간주한다.와 0인 경우는 코어가 아니므로 탐색해야 하는 조거네 들어가지
					// 않음.
					if (i == 0 || i == N - 1 || j == 0 || j == N - 1 || val == 0) {
						continue;
					}
					coreList.add(new Point(i, j));
				}
			}
			dfs(0, 0, 0);
			System.out.println("#" + test_case + " " + coreLen);
		}
	}

	private static void dfs(int index, int cnt, int len) {
		// 모든 코어를 탐색했을 경우
		if (index == coreList.size()) {
			// 코어의 개수가 같은 경우 선의 길이가 가장 짧게 만들어야 함.
			if (cnt == coreCnt) {
				coreLen = Math.min(len, coreLen);
			} else if (cnt > coreCnt) { // 코어의 개수가 많으면 무조건 업데이트
				coreCnt = cnt;
				coreLen = len;
			}
			return;
		}
		// 4방위 탐색
		for (int idx = 0; idx < 4; idx++) {
			int count = 0; // 선의 개수를 위한 변수
			// 최초 위치 저장
			int x = coreList.get(index).x;
			int y = coreList.get(index).y;
			int _x = x;
			int _y = y;
			// 가장자리까지 이동할때까지 무한 반복 but, 다른 코어를 만나게 되면 선의 의미가 없으므로 길이는 0으로 바꿔서 나와야 한다.
			while (true) {
				_x += dx[idx];
				_y += dy[idx];
				if (_x < 0 || _x > N - 1 || _y < 0 || _y > N - 1) {
					break;
				}
				if (matrix[_x][_y] == 1) {
					count = 0;
					break;
				}
				count++;
//					matrix[_x][_y] = 1; // 지금 변경하면 탐색이 불가능함
			}
			// 여기서 다시 해결해야 함
			_x = x;
			_y = y;
			// 이동한 곳에 선을 그어줌
			for (int c = 0; c < count; c++) {
				_x += dx[idx];
				_y += dy[idx];
				matrix[_x][_y] = 1;
			}
			// count >0 이상인 경우 끝까지 만나지 않고 도달했다는 증거
			if (count == 0) {
				// 다음 코어의 위치로 좌표를 옮기는데 다른 코어와 선이 충돌되어 개수와 길이는 증가하지 않음.
				dfs(index + 1, cnt, len);
			} else if (count > 0) { // 선이 그어질 수 있는 곳
				dfs(index + 1, cnt + 1, len + count); // 다음 코어, 개수 하나 증가, 길이 증가

				// 재귀가 끝났으면 다음 방위 탐색을 위해 기존에 만들었던 선을 전부 회수해야 함.
				_x = x;
				_y = y;
				for (int c = 0; c < count; c++) {
					_x += dx[idx];
					_y += dy[idx];
					matrix[_x][_y] = 0;
				}
			}

		}
	}
}
