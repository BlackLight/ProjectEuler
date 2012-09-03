#include <iostream>
#include <vector>
using namespace std;

struct data  {
	int x;
	int y;
	int z;
	int n;
};

int main()  {
	int count = 0;

	for (int n=1; n < 500000; n++)  {
		vector<struct data> seq;

		for (int x=1; x < 100 && seq.size() < 2; x++)  {
			for (int step=1;  x - 2*step > 0 && seq.size() < 2; step++)  {
				int y = x-step;
				int z = y-step;
			
				if (x*x - y*y - z*z == n)  {
					struct data tmp;
					tmp.x = x; tmp.y = y; tmp.z = z; tmp.n = n;
					seq.push_back(tmp);
				}
			}
		}

		if (seq.size() == 1)  {
			count++;
			//cout << seq[0].x << ", " << seq[0].y << ", " << seq[0].z << " -> " << seq[0].n << endl;
		}
	}

	cout << count << endl;
	return 0;
}

