#ifndef __NODE_H__
#define __NODE_H__

#include "state.h"
#include <list>

class Node {

    Node * p;
    std::list<Node *> children;
    State state;
    int g;
    double (*f)(Node *);

    public:
        Node (Node * p, State state, int g, double (*f)(Node *)) {
            this->p = p;
            this->state = state;
            this->g = g;
            this->f = f;
        }
        void addChild(Node * child){
            this->children.push_back(child);
        }
        bool operator<(Node other) {
            return this->f(this) < other.f(this);
        }
        bool operator>(Node other) {
            return this->f(this) > other.f(this);
        }
        bool operator==(Node other) {
            return this->f(this) == other.f(this);
        }
};

#endif