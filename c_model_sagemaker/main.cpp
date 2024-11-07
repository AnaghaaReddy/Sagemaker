#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: ./a.out <file_path>\n";
        return 1;
    }

    // Open CSV file specified in argv[1]
    ifstream file(argv[1]);
    if (!file.is_open()) {
        cerr << "Could not open the file!" << endl;
        return 1;
    }

    vector<int> result;
    string line;

    // Process each line in the CSV file
    while (getline(file, line)) {
        istringstream ss(line);
        string val1, val2;
        
        // Read two comma-separated values from each line
        if (getline(ss, val1, ',') && getline(ss, val2, ',')) {
            int num1 = stoi(val1);
            int num2 = stoi(val2);
            result.push_back(num1 + num2); // Sum of the two columns
        }
    }
    file.close();

    // Output result as comma-separated values
    for (size_t i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i != result.size() - 1)
            cout << ',';
    }

    return 0;
}
