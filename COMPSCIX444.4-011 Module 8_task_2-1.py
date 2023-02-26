# This programme enables a Tic-Tac-Toe game:

status_play = ''

def show_current_state():
    
        print('Current State:')
        
        first_row = '|'.join(rows[:3])
        second_row = '|'.join(rows[3:6])
        third_row = '|'.join(rows[6:9])
        
        print('|' + first_row + '|')
        print('|' + second_row + '|')
        print('|' + third_row + '|')

        
def show_final_state():
    
        print('Final State:')
        
        first_row = '|'.join(rows[:3])
        second_row = '|'.join(rows[3:6])
        third_row = '|'.join(rows[6:9])
        
        print('|' + first_row + '|')
        print('|' + second_row + '|')
        print('|' + third_row + '|')


def show_box_number():
        box_numbers = ['0','1','2','3','4','5','6','7','8']
        print('Box number:')
        
        first_row = '|'.join(box_numbers[:3])
        second_row = '|'.join(box_numbers[3:6])
        third_row = '|'.join(box_numbers[6:9])
        
        print('|' + first_row + '|')
        print('|' + second_row + '|')
        print('|' + third_row + '|')

def wining_step(player, rows):
    
    if rows[0] != ' ':
        
        if rows[0] == rows[1] == rows[2]:
            print('Player ' + player + ' wins!')
            return 'game over'
        
        if rows[0] == rows[3] == rows[6]:
            print('Player ' + player + ' wins!')
            return 'game over'
     
        if rows[0] == rows[4] == rows[8]:
            print('Player ' + player + ' wins!')
            return 'game over'

    if rows[2] != ' ':
        if rows[2] == rows[5] == rows[8]:
            print('Player ' + player + ' wins!')
            return 'game over'

        
        if rows[2] == rows[4] == rows[6]:
            print('Player ' + player + ' wins!')
            return 'game over'  
    
    if rows[1] != ' ':
        
        if rows[1] == rows[4] == rows[7]:
            print('Player ' + player + ' wins!')
            return 'game over'
     
    if rows[3] != ' ':
        
        if rows[3] == rows[4] == rows[5]:
            print('Player ' + player + ' wins!')
            return 'game over'
  
    if rows[6] != ' ':
        
        if rows[6] == rows[7] == rows[8]:
            print('Player ' + player + ' wins!')
            return 'game over'

while status_play.lower() != 'n':

    valid_choice = ['0','1','2','3','4','5','6','7','8']
    rows = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player = 'A'
    status = 'ongoing'

    for i in range(0, 9):
        
        if player == 'A':
            if status != 'game over':
                    
                show_box_number()
                show_current_state()

                box_selected = input('Player A, please enter a box number.')

                while box_selected not in valid_choice:
                    box_selected = input('Player A, you entered a wrong box number. Try again.')

                rows[int(box_selected)] = 'X'

                valid_choice.remove(str(box_selected))

                status = wining_step(player, rows)

                player = 'B'

        elif player == 'B':
            if status != 'game over':
                    
                show_box_number()
                show_current_state()

                box_selected = input('Player B, please enter a box number.')

                while box_selected not in valid_choice:
                    box_selected = input('Player B, you entered a wrong box number. Try again.')

                rows[int(box_selected)] = 'O'

                valid_choice.remove(str(box_selected))        

                status = wining_step(player, rows)

                player = 'A'
                    
        if status == 'game over':
            show_final_state()
            
            break
            
    if status == 'ongoing':
        show_final_state()
        print('no winner')

    status_play = input('Would you want another round? Y/N')
    
    if status_play.lower() == 'n':
        print('Goodbye')
