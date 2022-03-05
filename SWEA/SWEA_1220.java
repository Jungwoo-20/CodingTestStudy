import java.util.Scanner;

// 1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체를 의미하며 테이블의 윗 부분에 N극이 아랫 부분에 S극이 위치한다고 가정한다.
public class SWEA_1220 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);

		for (int test_case = 1; test_case <= 10; test_case++) {
			int[][] matrix = new int[100][100];
			int num = sc.nextInt();
			int res = 0;
			for (int i = 0; i < num; i++) {
				for (int j = 0; j < num; j++) {
					matrix[i][j] = sc.nextInt();
				}
			}
			for (int i = 0; i < num; i++) {
				int tmp = 0;
				for (int j = 0; j < num; j++) {
					// 위쪽이 N극이기 때문에 N극을 만났을때 저장 변수를 사용해야함. 반대의 경우 틀린 접근
					if (matrix[j][i] == 2 && tmp == 1) {
						res++;
						tmp = 0;
					} else if (matrix[j][i] == 1) {
						tmp = 1;
					}
				}
			}
			System.out.println("#" + test_case + " " + res);
		}
	}

}
