import java.io.*;
import java.util.*;

public class JOL_2577 {
	static BufferedReader br;
	static int N, d, k, c, matrix[], left, right, res, selected[], count;
	static boolean flag;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		left = 0;
		right = 0;
		res = 0;
		count = 0;
		flag = true;
		matrix = new int[N];
		selected = new int[d + 1];
		for (int i = 0; i < N; i++) {
			matrix[i] = Integer.parseInt(br.readLine());
		}

//		// 시간 초과 코드
//		while (left != N) {
//			HashSet<Integer> set = new HashSet<>();
//			right = left + k;
//			for (int i = left; i <= right; i++) {
//				int temp = i % N;
//				set.add(matrix[temp]);
//				if (matrix[temp] == c) {
//					flag = false;
//				}
//			}
//			int cnt = set.size();
//			if (flag) {
//				++cnt;
//			}
//			if (cnt == k+1) {
//				res = cnt;
//				break;
//			}
//			res = Math.max(cnt, res);
//			left++;
//			set.clear();
//		}
//		System.out.println(res);
		
		// 해결
		// 슬라이딩 윈도우 문제(투 포인터로 단순하게 접근하기에는 데이터가 정렬된 상황이 아님)
		
		// 초기 상태에서 k개 만큼 먹기
		for (int i = 0; i < k; i++) {
			// 먹지 않은 경우 (종류가 하나 증가)
			if (selected[matrix[i]] == 0) {
				count++;
			}
			// 먹었던 경우는 그냥 먹은 개수만 증가
			selected[matrix[i]]++;
		}
		res = count;
		// start지점을 하나씩 뒤로 땡김
		for (int i = 0; i < N; i++) {
			// 먹을 수 있는 종류가 많아진 경우 데이터 업데이트
			
			if (res <= count) {
				// 쿠폰 음식을 먹지 않았기 때문에 하나를 더 먹을 수 있음
				if (selected[c] == 0) {
					res = count + 1;
					// k 종류개를 먹었는데 쿠폰으로 하나 더 먹어서 res가 k개수보다 하나 많은 경우
					// res를 출력하고 더이상 확인할 필요가 없으니 프로그램 종료
					if (res == k+1) {
						System.out.println(res);
						return;
					}
				} else {
					res = count;
				}
			}

			// 시작 지점의 음식을 하나 뱉음
			selected[matrix[i]]--;
			// 시작 지점의 음식을 먹지 않은 경우 -> 음식 종류 카운팅 하나를 제거
			if (selected[matrix[i]] == 0) {
				count--;
			}

			// 가장 오른쪽 음식이 먹지 않았던 종류인 경우 -> 음식 종류 카운팅 하나 추가
			if (selected[matrix[(i + k) % N]] == 0) {
				count++;
			}
			// 음식 선택 개수 추가
			selected[matrix[(i + k) % N]]++;
		}
		System.out.println(res);
	}

}
