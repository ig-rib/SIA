#ifndef __STATE_H__
#define __STATE_H__

#include <algorithm>
#include <iostream>

using namespace std;

class State {

    public:
        std::vector<std::pair<int, int>> boxes;
        std::pair<int, int> user;

        bool checkFinal(std::vector<std::pair<int, int>> goalSquares) {
            for (auto it = goalSquares.begin(); it != goalSquares.end(); it++){
                if(find(boxes.begin(), boxes.end(), *it) == boxes.end())
                    return false; 
            }
            return true;
        }

        bool operator==(State other) {
            for (auto box = boxes.begin(); box != boxes.end(); box++){
                if(find(other.boxes.begin(), other.boxes.end(), *box) != other.boxes.end())
                    return false;
            }
            if (user != other.user)
                return false;
            return true;
        }

        void printState(vector<vector<char>> maze) {
            for (int i = 0; i < maze.size(); i++) {
                for (int j = 0; j < maze[i].size(); j++) {
                    if (find(boxes.begin(), boxes.end(), pair<int, int>(i, j)) != boxes.end())
                        cout << '$';
                    else if (pair<int, int>(i, j) != user)
                        cout << maze[i][j];
                    else
                        cout << '@';
                }
            }
        }

        void hasUnmovableBox(vector<vector<char>> maze, vector<pair<int, int>> goalStates) {
            auto dirns = list<pair<int, int>>();
            int walls;
            list<pair<int, int>> d {};
            d.push_back(make_pair(-1, 0));
            d.push_back(make_pair(1, 0));
            d.push_back(make_pair(0, -1));
            d.push_back(make_pair(0, 1));
            for (auto b = boxes.begin(); b != boxes.end; b++) {
                dirns.clear();
                walls = 0;
                for (auto dir = d.begin(); dir != d.end(); dir++) {
                    if (maze[b->first + dir->first][b->second + dir->second] == '#')
                        dirns.push_back(*dir);
                }
                for (int i = 0; i < dirns.size(); i++) {
                    for (int j = 0; j < dirns.size(); j++ ) {
                        
                    }
                }
            }
        }
};

#endif