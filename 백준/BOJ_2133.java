import java.util.Scanner;

public class BOJ_2133 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] dp = new int[31];

		dp[2] = 3;
		// 가로의 길이가 홀수인 경우 만들 수 없음.
		// dp[2] = 3, dp[4] = 11, dp[6] = 41
		// dp[4]의 경우 dp[2](고정값 = 3) 두번과 dp[4]에서 만들 수 있는 경우는 2가지 => 11개
		// 점화식 = dp[N] = dp[N-2] * 3 + dp[N-4]*2 ... + 2;
		for (int i = 4; i < N + 1; i += 2) {
			dp[i] = dp[i - 2] * 3; // 2
			for (int j = 0; j < i - 2; j++) {
				dp[i] += dp[j] * 2;
			}
			dp[i] += 2;
		}

		System.out.println(dp[N]);
	}

}
