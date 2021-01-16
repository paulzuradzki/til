/* ttt.c

A simple Tic Tac Toe game from command line to practice C programming.

Learning concepts: 
  * basics - functions, conditions, arrays 
  * pointers for shared objects between functions (e.g., tracking current player and board state) 
  * user input with scanf and pointers

*/

#include <stdio.h>
#include <stdbool.h>

void print_board(char board[9]);
bool game_over(char board[9]);
void switch_player(char* current_player);

int main(void) {

    char board[9] = {'0', '1', '2',
                     '3', '4', '5',
                     '6', '7', '8'};

    char current_player = 'X';
    int turn_count = 0;
    print_board(board);
    
    int user_input;
    while (!game_over(board))
    {
        printf("\n%c's turn. \nEnter an integer position to place your mark (0-8).\n", current_player);
        scanf("%i", &user_input);
        board[user_input] = current_player;
        print_board(board);
        turn_count++;
        
        if (game_over(board))
        {
            printf("Player %c wins!\n", current_player);
            break;
        }

        if (turn_count==9)
            {
            printf("It's a tie. Game over.\n");
            break;
            }
        
        switch_player(&current_player);

    } // end while
} // end main

bool game_over(char board[9]) 
{
    if (
        // 3 in a row
        (board[0]==board[1] & board[1]==board[2]) |
        (board[3]==board[4] & board[4]==board[5]) |
        (board[6]==board[7] & board[7]==board[8]) |

        // 3 in a column
        (board[0]==board[3] & board[3]==board[6]) |
        (board[1]==board[4] & board[4]==board[7]) |
        (board[2]==board[5] & board[5]==board[8]) |

        // 3 in a diagonal
        (board[0]==board[4] & board[4]==board[8]) |
        (board[2]==board[4] & board[4]==board[6])         
        )

        {
            printf("GAME OVER!\n");
            return true;
        } // end if

        return false; 
} // end game_over

void print_board(char board[9]) 
{
    printf("Board state\n");
    for (int i=0; i<=8; i++)
    {
        if (board[i] == 'X' | board[i] == 'O')
            printf("%c ", board[i]);
        else 
            printf("_ ");
            // printf("%c ", board[i]);

        if (i==2)
            printf(" 0 1 2");

        if (i==5)
            printf(" 3 4 5");

        if (i==8)
            printf(" 6 7 8");

        if (i==2 | i==5 | i==8)
        {
            printf("\n");
        } // end if

    } // end for
} // end print_board

void switch_player(char* current_player)
{
    if (*current_player == 'X')
        *current_player = 'O';
    else
        *current_player = 'X';
} // end switch_player
