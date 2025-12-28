#ifndef MAIN_H
#define MAIN_H

#include "gba.h"

// TODO: Create any necessary structs

/*
* For example, for a Snake game, one could be:
*
* struct snake {
*   int heading;
*   int length;
*   int row;
*   int col;
* };
*
* Example of a struct to hold state machine data:
*
* struct state {
*   int currentState;
*   int nextState;
* };
*
*/

struct state {
    int currentState;
    int nextState;
};

struct ss {
    int row;
    int col;
} ss_image;

struct eggman {
    int row;
    int col;
    int speed;
} player;

struct collision_point {
    int row;
    int col;
    int width;
    int height;
} masterEmerald;

struct vertical_laser {
    struct collision_point v_stats[28];
};

struct horizontal_laser {
    struct collision_point h_stats[22];
};

struct timer {
    int row;
    int col;
    int seconds;
} time;

int collision(struct eggman p, struct collision_point x);
void getTime(void);

#endif
