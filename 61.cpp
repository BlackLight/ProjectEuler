#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

#define 	NUMBERS 	6

vector<int> triang;
vector<int> square;
vector<int> penta;
vector<int> hexa;
vector<int> hepta;
vector<int> octa;

bool checkSeq (vector<int> seq)  {
	bool has[NUMBERS] = { false };

	for (int i=0; i < seq.size(); i++)  {
		if (binary_search(triang.begin(), triang.end(), seq[i]))  {
			has[0] = true;
			continue;
		}
		
		if (binary_search(square.begin(), square.end(), seq[i]))  {
			has[1] = true;
			continue;
		}

		if (binary_search(penta.begin(), penta.end(), seq[i]))  {
			has[2] = true;
			continue;
		}
		
		if (binary_search(hexa.begin(), hexa.end(), seq[i]))  {
			has[3] = true;
			continue;
		}
		
		if (binary_search(hepta.begin(), hepta.end(), seq[i]))  {
			has[4] = true;
			continue;
		}
		
		if (binary_search(octa.begin(), octa.end(), seq[i]))  {
			has[5] = true;
			continue;
		}
	}

	for (int i=0; i < NUMBERS; i++)
		if (!has[i])
			return false;

	return true;
}

int main()  {
	for (int i=0; i < 1000; i++)  {
		triang.push_back(i*(i+1)/2);
		square.push_back(i*i);
		penta.push_back(i*(3*i-1)/2);
		hexa.push_back(i*(2*i-1));
		hepta.push_back(i*(5*i-3)/2);
		octa.push_back(i*(3*i-2));
	}

	vector<int> nums(NUMBERS);

	for (nums[0]=10; nums[0] < 100; nums[0]++)  {
		for (nums[1]=10; nums[1] < 100; nums[1]++)  {
			for (nums[2]=10; nums[2] < 100; nums[2]++)  {
				for (nums[3]=10; nums[3] < 100; nums[3]++)  {
					for (nums[4]=10; nums[4] < 100; nums[4]++)  {
						for (nums[5]=10; nums[5] < 100; nums[5]++)  {
							vector<int> seq(NUMBERS);
							stringstream ss[NUMBERS];

							ss[0] << nums[0] << nums[1];
							ss[0] >> seq[0];
				
							ss[1] << nums[1] << nums[2];
							ss[1] >> seq[1];
							
							ss[2] << nums[2] << nums[3];
							ss[2] >> seq[2];
							
							ss[3] << nums[3] << nums[4];
							ss[3] >> seq[3];
							
							ss[4] << nums[4] << nums[5];
							ss[4] >> seq[4];
							
							ss[5] << nums[5] << nums[0];
							ss[5] >> seq[5];

							if (checkSeq(seq))  {
								int sum = 0;

								for (int i=0; i < seq.size(); i++)  {
									sum += seq[i];
									cout << seq[i] << ", ";
								}

								cout << endl << sum << endl;
								return 0;
							}
						}
					}
				}
			}
		}
	}

	return 1;
}

