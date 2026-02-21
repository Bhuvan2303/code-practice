// WarshallTransitiveClosure.cpp
// Program to find Transitive Closure using Warshall's Algorithm

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Enter number of vertices: ";
    cin >> n;

    int graph[20][20];
    cout << "Enter adjacency matrix (0 for no edge, 1 for edge):\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> graph[i][j];
        }
    }

    // Warshall’s algorithm for transitive closure
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                graph[i][j] = graph[i][j] || (graph[i][k] && graph[k][j]);
            }
        }
    }

    // Print transitive closure matrix
    cout << "\nTransitive Closure Matrix:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << setw(3) << graph[i][j];
        }
        cout << endl;
    }

    return 0;
}
