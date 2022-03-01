import java.util.*;

public class BOJ_2292 {
	static Scanner sc;

	public static void main(String[] args) {
		sc = new Scanner(System.in);
		int N = sc.nextInt();
		int cnt = 1;
		int point = 1;
		while (N > point) {
			point += cnt * 6;
			cnt++;
		}
		System.out.println(cnt);

	}

}