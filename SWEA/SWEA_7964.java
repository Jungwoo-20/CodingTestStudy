package problem;

import java.util.*;

public class SWEA_7964 {
	static int city, dist; // 입력값
	static int cnt, distance; // 총 개수, 현재 거리

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			city = sc.nextInt();
			dist = sc.nextInt();
			cnt = 0;
			distance = 0;
			for (int i = 0; i < city; i++) {
				int num = sc.nextInt();
				// 남아있는 경우
				if (num == 1) {
					// 거리 초기화
					distance = 0;
				} else { // 파괴 당한 경우
					distance++; // 거리를 하나씩 늘려간다
					if (distance == dist) { // 더이상 늘릴 수 없는 경우
						// 하나 설치하고 거리를 초기화
						cnt++;
						distance = 0;
					}
				}
			}
			System.out.println("#" + test_case + " " + cnt);

		}
	}

}
