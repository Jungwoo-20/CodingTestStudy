import java.io.*;
import java.util.*;

public class SWEA_3124 {
	static class Data implements Comparable<Data> {
		int vertex;
		long weight;

		public Data(int vertex, long weight) {
			super();
			this.vertex = vertex;
			this.weight = weight;
		}

		@Override
		public int compareTo(Data o) {
			// TODO Auto-generated method stub
			return (int) (this.weight - o.weight);
		}

	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());

		for (int test_case = 1; test_case <= T; test_case++) {
			st = new StringTokenizer(br.readLine(), " ");
			int V = Integer.parseInt(st.nextToken());
			int E = Integer.parseInt(st.nextToken());
			long res = 0;
			ArrayList<Data>[] arr = new ArrayList[V + 1];
			boolean[] dp = new boolean[V + 1];
			PriorityQueue<Data> queue = new PriorityQueue<>();
			ArrayDeque<Integer> dequeue = new ArrayDeque<>();

			for (int i = 0; i <= V; i++) {
				arr[i] = new ArrayList<>();
			}
			for (int i = 0; i < E; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				int A = Integer.parseInt(st.nextToken());
				int B = Integer.parseInt(st.nextToken());
				long C = Integer.parseInt(st.nextToken());
				arr[A].add(new Data(B, C));
				arr[B].add(new Data(A, C));
			}
			dequeue.add(1);
			while (!dequeue.isEmpty()) {
				int idx = dequeue.poll();
				dp[idx] = true;
				for (int i = 0; i < arr[idx].size(); i++) {
					int vertex = arr[idx].get(i).vertex;
					long weight = arr[idx].get(i).weight;
					if (dp[vertex])
						continue;
					queue.add(new Data(vertex, weight));
				}
				while (!queue.isEmpty()) {
					Data data = queue.poll();
					int vertex = data.vertex;
					long weight = data.weight;
					if (dp[vertex])
						continue;
					dp[vertex] = true;
					dequeue.add(vertex);
					res += weight;
					break;
				}
			}
			System.out.println("#" + test_case + " " + res);

		}
	}

}
