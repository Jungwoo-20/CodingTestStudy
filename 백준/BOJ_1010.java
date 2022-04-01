import java.util.Scanner;

public class BOJ_1010 {
	static Scanner sc;
	static double T, N, M;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		sc = new Scanner(System.in);
		T = sc.nextInt();
		for (int idx = 0; idx < T; idx++) {
			N = sc.nextInt();
			M = sc.nextInt();
			System.out.printf("%.0f\n", solution(M, N));

		}
	}

	private static double solution(double m, double n) {
		double x = 1;
		double y = 1;
		for (double i = m; i > m - n; i--) {
			x *= i;
		}
		for (double j = n; j >= 1; j--) {
			y *= j;
		}
		return x / y;
	}

}
