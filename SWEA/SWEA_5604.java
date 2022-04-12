import java.util.Scanner;

public class SWEA_5604 {
	static long res;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();

		for (int test_case = 1; test_case <= T; test_case++) {

			long A = sc.nextLong();
			long B = sc.nextLong();
			res = 0;
			res = solution(A, B);
			System.out.println("#" + test_case + " " + res);
		}
	}

	private static long solution(long A, long B) {
		long digit = 1;
		while (A <= B) {
			while (A % 10 != 0 && A <= B) {
				calculator(A, digit);
				A++;
			}
			// 종료 조건
			if (A > B || (A == 0 && B == 0))
				break;
			while (B % 10 != 9 && A <= B) {
				calculator(B, digit);
				B--;
			}
			// 한자리수씩 내리기
			A /= 10;
			B /= 10;
			long tmp = (B - A + 1) * digit;
			digit *= 10;
			if (tmp == 0) {
				continue;
			}
			for (int i = 0; i < 10; i++) {
				res += tmp * i;
			}
		}
		return res;
	}

	private static void calculator(long num, long digit) {
		// TODO Auto-generated method stub
		while (num > 0) {
			// 1,10,100의자리에서 끝자리 부분 계산
			res += (num % 10) * digit;
			// 마지막 자리 숫자 제거
			num /= 10;
		}

	}

}
