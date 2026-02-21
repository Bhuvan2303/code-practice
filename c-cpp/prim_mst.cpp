#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

// Function to find the vertex with minimum key value
int minKey(vector<int>& key, vector<bool>& mstSet, int V) {
    int min = INT_MAX, min_index;
    for (int v = 0; v < V; v++) {
        if (!mstSet[v] && key[v] < min) {
            min = key[v];
            min_index = v;
        }
    }
    return min_index;
}

// Print MST stored in parent[]
void printMST(vector<int>& parent, vector<vector<int>>& graph, int V) {
    int minCost = 0;
    cout << "Edges in Minimum Cost Spanning Tree:\n";
    for (int i = 1; i < V; i++) {
        cout << parent[i] << " -- " << i << " == " << graph[i][parent[i]] << endl;
        minCost += graph[i][parent[i]];
    }
    cout << "Minimum Cost of Spanning Tree: " << minCost << endl;
}

// Prim’s Algorithm
void primMST(vector<vector<int>>& graph, int V) {
    vector<int> parent(V);   // Store MST
    vector<int> key(V, INT_MAX); // Key values
    vector<bool> mstSet(V, false); // Included in MST?

    key[0] = 0;     // Start from first vertex
    parent[0] = -1; // First node is root

    for (int count = 0; count < V - 1; count++) {
        int u = minKey(key, mstSet, V);
        mstSet[u] = true;

        for (int v = 0; v < V; v++) {
            if (graph[u][v] && !mstSet[v] && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    printMST(parent, graph, V);
}

// Driver Code
int main() {
    int V;
    cout << "Enter number of vertices: ";
    cin >> V;

    vector<vector<int>> graph(V, vector<int>(V));
    cout << "Enter adjacency matrix (0 if no edge):\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            cin >> graph[i][j];
        }
    }

    primMST(graph, V);

    return 0;
}
