import java.util.Arrays;
import java.util.Scanner;

public class SWEA_7193 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			int N = sc.nextInt();
			char[] X = sc.next().toCharArray();
			int tmp = 0;
			// 각 자리수 합을 구해 N-1의 나머지를 구하는 것이 가장 빠름(10진수로 변경해서 할 필요가 없음)
			for (char x : X) {
				tmp += Character.getNumericValue(x);
			}
			System.out.println("#" + test_case + " " + tmp % (N - 1));

		}
	}

}
