import java.util.Scanner;

//변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
public class BOJ_2477 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int K = sc.nextInt();
		int matrix[] = new int[6];
		for (int i = 0; i < 6; i++) {
			int dir = sc.nextInt();
			int length = sc.nextInt();
			matrix[i] = length;
		}
		int largeArea = 0;
		int smallArea = 0;
		int idx = -1;
		for (int i = 0; i < 6; i++) {
			int tmp = matrix[i] * matrix[(i + 1) % 6];
			if (largeArea < tmp) {
				largeArea = tmp;
				idx = i;
			}
		}
		smallArea = matrix[(idx + 3) % 6] * matrix[(idx + 4) % 6];
		System.out.println(K * (largeArea - smallArea));
	}

}
