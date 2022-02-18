class Solution {
    public int fib(int N) {
        int r=0;
		if (N == 0)
			r = 0;
		if (N == 1)
			r = 1;
		if (N > 1)
			r = fib(N - 1) + fib(N - 2);
		return r;
    }
}