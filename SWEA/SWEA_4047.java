package problem;

import java.util.*;

public class SWEA_4047 {

	static String cardStr;
	static Map<Character, Integer> card; // 필요한 카드의 수를 담고 있는 Map
	static ArrayList<String> array; // 입력 카드 정보를 담기 위한 ArrayList
	static HashSet<String> hashSet; // 중복 검사를 위한 HashSet
	static ArrayList<Character> set; // SDHC저장 리스트
	static Scanner sc;

	public static void main(String[] args) {
		sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			System.out.print("#" + test_case + " ");
			// 초기화 및 입력
			init();

			soultion();
			System.out.println();
		}
	}

	private static void soultion() {
		// 입력받은 String을 3글자씩 잘라서 add
		for (int i = 0; i < cardStr.length(); i += 3) {
			array.add(cardStr.substring(i, i + 3));
			hashSet.add(cardStr.substring(i, i + 3));
		}
		// 두 size가 다른 경우 => 중복된 값이 있다는 것이므로 에러 출력
		if (array.size() != hashSet.size()) {
			System.out.print("ERROR");
		} else {
			for (int i = 0; i < array.size(); i++) {
				// 카드 정보를 담고 있는 곳에서 카드 모양의 숫자 -1을 수행
				char string = array.get(i).charAt(0);
				int num = card.get(string);
				num--;
				card.put(string, num);
			}
			// 결과 출력
			for (int i = 0; i < set.size(); i++) {
				System.out.print(card.get(set.get(i)) + " ");
			}
		}
	}

	private static void init() {
		cardStr = sc.next();
		card = new HashMap<Character, Integer>();
		card.put('S', 13);
		card.put('D', 13);
		card.put('H', 13);
		card.put('C', 13);
		set = new ArrayList<>();
		set.add('S');
		set.add('D');
		set.add('H');
		set.add('C');
		array = new ArrayList<>();
		hashSet = new HashSet<>();
	}

}
