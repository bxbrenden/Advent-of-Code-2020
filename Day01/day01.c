/*
 * =====================================================================================
 *
 *       Filename:  day01.c
 *
 *    Description: Day 01 of Advent of Code 2020 
 *
 *        Version:  1.0
 *        Created:  11/14/2022 06:36:41 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define LINE_LEN 6
#define PUZZLE_INPUT "input.txt"

int count_newlines(FILE *inp);

void get_int_vals(char *filename, int *vals, int num_newlines);

int solve_puzzle(int *vals, int num_newlines);

int main(int argc, char *argv[]) {
  FILE *input = fopen(PUZZLE_INPUT, "r");
  int num_newlines = count_newlines(input);
  int vals[num_newlines];
  int answer;
  get_int_vals(PUZZLE_INPUT, &vals[0], num_newlines);
  answer = solve_puzzle(&vals[0], num_newlines);
  printf("The answer is %d\n", answer);
  return 0;
}

int count_newlines(FILE *inp) {
  int num_newlines = 0;
  char line[LINE_LEN];

  while (fgets(line, LINE_LEN, inp)) {
    num_newlines++;
  }

  return num_newlines;
}

void get_int_vals(char *filename, int *vals, int num_newlines) {
  FILE * inp = fopen(filename, "r");
  char line[LINE_LEN];

  for (int i=0; fgets(line, LINE_LEN, inp); i++) {
    int current_val = atoi(line);
    vals[i] = current_val;
  }
}

int solve_puzzle(int *vals, int num_newlines) {
  int outer, inner;

  for (outer=0; outer<num_newlines; outer++) {
    for (inner=0; inner<num_newlines; inner++) {
      if (vals[outer] + vals[inner] == 2020) {
        printf("%d + %d == 2020\n", vals[outer], vals[inner]);
        return vals[outer] * vals[inner];
      }
    }
  }
  return 0;
}
