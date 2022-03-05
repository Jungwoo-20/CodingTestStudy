import java.util.*;

public class BOJ_1753 {
	static class Data implements Comparable<Data> {
		int end;
		int weight;

		public Data(int end, int weight) {
			super();
			this.end = end;
			this.weight = weight;
		}

		@Override
		public int compareTo(Data o) {
			// TODO Auto-generated method stub
			return this.weight - o.weight;
		}

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int V = sc.nextInt();
		int E = sc.nextInt();
		int K = sc.nextInt();
		ArrayList<Data>[] arr = new ArrayList[V + 1];
		for (int i = 0; i <= V; i++) {
			arr[i] = new ArrayList<>();
		}
		PriorityQueue<Data> queue = new PriorityQueue<>();
		int[] dp = new int[V + 1];
		for (int i = 0; i <= V; i++) {
			dp[i] = Integer.MAX_VALUE;
		}
		for (int i = 0; i < E; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			int w = sc.nextInt();
			arr[u].add(new Data(v, w));
		}
		dp[K] = 0;
		queue.add(new Data(K, 0));
		while (!queue.isEmpty()) {
			Data data = queue.poll();
			int vertex = data.end;
			int weight = data.weight;
			if (dp[vertex] < weight)
				continue;
			for (int i = 0; i < arr[vertex].size(); i++) {
				int _vertex = arr[vertex].get(i).end;
				int _weight = weight + arr[vertex].get(i).weight;
				if (dp[_vertex] > _weight) {
					dp[_vertex] = _weight;
					queue.add(new Data(_vertex, _weight));
				}
			}
		}
		for (int i = 1; i < dp.length; i++) {
			if (dp[i] == Integer.MAX_VALUE) {
				System.out.println("INF");
			} else {
				System.out.println(dp[i]);
			}
		}

	}

}
