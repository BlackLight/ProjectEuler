#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

main()  {
	ifstream in("base_exp.txt");
	string s;
	float max=1.0;

	for (int line=1; getline(in,s); line++)  {
		int base,exp;
		sscanf (s.c_str(), "%d,%d", &base, &exp);
		
		float e = logf(base)*exp;

		if (e>max)  {
			max=e;
			cout << "max = " << max << " @ line " << line << endl;
		}
	}

	in.close();
}

