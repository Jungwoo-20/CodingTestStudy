import java.io.*;
import java.util.*;

public class SWEA_5656 {

	static class Point {
		int r, c, cnt;

		public Point(int r, int c, int cnt) {
			super();
			this.r = r;
			this.c = c;
			this.cnt = cnt;
		}

	}

	static int[] dr = { -1, 1, 0, 0 };
	static int[] dc = { 0, 0, -1, 1 };
	static int N, W, H, min;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(in.readLine());
		for (int tc = 1; tc <= TC; tc++) {
			StringTokenizer st = new StringTokenizer(in.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			H = Integer.parseInt(st.nextToken());
			int[][] map = new int[H][W];
			for (int i = 0; i < H; i++) {
				st = new StringTokenizer(in.readLine(), " ");
				for (int j = 0; j < W; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			min = Integer.MAX_VALUE;
			go(0, map);
			System.out.println("#" + tc + " " + min);
		}
	}

	// 중복 순열을 이용하여 구슬을 던지기, 벽돌이 다 부서졌다면 true, 아니라면 false
	static boolean go(int count, int[][] map) {
		int result = getRemain(map);
		// 모든 벽돌이 부서졌다면
		if (result == 0) {
			min = 0;
			return true;
		}
		// 모든 구슬을 다 던졌다면
		if (count == N) {
			min = Math.min(min, result);
			return false;
		}
		int[][] newMap = new int[H][W];
		// 0열부터 W-1까지 구슬 던져보기
		for (int c = 0; c < W; c++) {
			// 구슬에 맞는 벽돌 찾기
			int r = 0;
			// 빈공간이면 계속해서 아래로
			while (r < H && map[r][c] == 0)
				++r;
			// 경계를 벗어나 끝난 경우 -> 해당 열은 벽돌이 없음
			if (r == H)
				continue;

			// 배열의 상태를 백업
			copy(map, newMap);

			boom(newMap, r, c);

			down(newMap);

			if (go(count + 1, newMap))
				return true;
		}
		return false;
	}

	// r,c 위치에서 주변의 가능한 모든 벽돌도 함께 부수는 처리
	static void boom(int[][] map, int r, int c) { // r,c 위치에서 주변의 가능한 모든 벽돌도 함께 부수는 처리 
		Queue<Point> queue = new LinkedList<Point>();
		if(map[r][c]>1) { // 벽돌크기가 2이상이면
			queue.offer(new Point(r,c,map[r][c]));
		}
		map[r][c] = 0; // 자신은 제거처리(빈 공간으로 ...) : visit 처리 역할
		
		while (!queue.isEmpty()) {
			Point p = queue.poll();
			
			for (int d = 0; d < 4; d++) {
				int nr = p.r, nc = p.c;
			
				for (int k = 1; k < p.cnt; k++) { // 벽돌의 크기-1만큼 반복
					nr += dr[d];
					nc += dc[d];
					if(nr>=0 && nr<H && nc>=0 && nc<W && map[nr][nc]>0) {
						if(map[nr][nc]>1) { // 주변 벽돌에 영향을 주는 벽돌이면
							queue.offer(new Point(nr, nc, map[nr][nc]));
						}
						map[nr][nc] = 0; //  제거 처리
					}
				}
			}
		}
	}
	static void down(int[][] map) {// 부서진 벽돌 정리,남은 벽돌 정리!!(공중에 떠있는 벽돌도 아래로 내리기)
		for (int c = 0; c < W; c++) {
			int r = H-1;// 아래행 시작
			while(r>0) {
				if(map[r][c]==0) { // 빈칸이면 내릴 벽돌 찾기
					int nr = r-1;
					while(nr>0 && map[nr][c]==0) nr--;
					
					map[r][c] = map[nr][c];
					map[nr][c] = 0;
				}
				r--;
			}
		}
	}

	static int getRemain(int[][] map) { // 남은 벽돌 수 리턴
		int count = 0;
		for (int r = 0; r < H; r++) {
			for (int c = 0; c < W; c++) {
				if(map[r][c]>0) ++count;
			}
		}
		return count;
	}
	static void copy(int[][] map, int[][] newMap) {
		for (int r = 0; r < H; r++) {
			for (int c = 0; c < W; c++) {
				newMap[r][c] = map[r][c];
			}
		}
	}

}
