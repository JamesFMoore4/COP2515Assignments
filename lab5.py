#The code for this project represents my own, independent work. I
#have neither given nor received help on this assignment from other
#students.

#James Moore

import random

def create_board(snake_start,snake_end,ladder_start,ladder_end):
    used_spaces = []
    num_snakes = random.randint(2,8)
    num_ladders = random.randint(2,8)
    i = 0
    v = 0
    while i < num_snakes:
        snake_1 = random.randint(2,63)
        snake_2 = random.randint(2,63)
        if snake_2 < snake_1 and snake_1 not in used_spaces and snake_2 not in used_spaces:
            snake_start.append(snake_1)
            snake_end.append(snake_2)
            used_spaces.append(snake_1)
            used_spaces.append(snake_2)
            i += 1
        else:
            i=i
    while v < num_ladders:
        ladder_1 = random.randint(2,63)
        ladder_2 = random.randint(2,63)
        if ladder_2 > ladder_1 and ladder_1 not in used_spaces and ladder_2 not in used_spaces:
            ladder_start.append(ladder_1)
            ladder_end.append(ladder_2)
            used_spaces.append(ladder_1)
            used_spaces.append(ladder_2)
            v += 1
        else:
            v = v
    return num_snakes, num_ladders, snake_start, snake_end, ladder_start, ladder_end

def snake_or_ladder(pos, snake_start, snake_end, ladder_start, ladder_end):
    if pos in snake_start:
        new_pos = snake_end[snake_start.index(pos)]
        print("Snake!")
    elif pos in ladder_start:
        new_pos = ladder_end[ladder_start.index(pos)]
        print("Ladder!")
    else:
        new_pos = pos
    return new_pos

def take_turn(pos, snake_start, snake_end, ladder_start, ladder_end):
    roll = random.randint(1,6)
    if pos == pos_1:
        print('Player 1 rolls the die: ', end=" ")
        print(roll)
    elif pos==pos_2 and pos != pos_1:
        print('Player 2 rolls the die: ', end=" ")
        print(roll)
    new_pos = pos + roll
    if new_pos > 64:
        new_pos = pos
    elif new_pos < 64:
        new_pos = snake_or_ladder(new_pos,snake_start,snake_end,ladder_start,ladder_end)
    return new_pos

snake_start = []
snake_end = []
ladder_start = []
ladder_end = []
pos_1 = 1
pos_2 = 1

num_snakes, num_ladders, snake_start, snake_end, ladder_start, ladder_end = create_board(snake_start, snake_end, ladder_start, ladder_end)

print(f'{num_snakes} snakes')
print(f'{num_ladders} ladders')

for i in range(len(snake_start)):
    print(f'Snake #{i+1}: {snake_start[i]} to {snake_end[i]}')
for i in range(len(ladder_start)):
    print(f'Ladder #{i+1}: {ladder_start[i]} to {ladder_end[i]}')

while pos_1 < 100 and pos_2 < 100:
    print(f'Player 1 is on space {pos_1}')
    print(f'Player 2 is on space {pos_2}')
    pos_1 = take_turn(pos_1, snake_start, snake_end, ladder_start, ladder_end)
    if pos_1 == 64:
        print("Player 1 wins!!!")
        break
    print(f'Player 1 is on space {pos_1}')
    print(f'Player 2 is on space {pos_2}')
    pos_2 = take_turn(pos_2, snake_start, snake_end, ladder_start, ladder_end)
    if pos_2 == 64:
        print("Player 2 wins!!!")
        break
    
    
    




    
    


            
        
    


        



    
