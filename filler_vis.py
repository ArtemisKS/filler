import sys
import graphics as gr
import re

map_size_x, map_size_y = 0, 0
piece_size_x, piece_size_y = 0, 0
iter_ind = 0
PLAYER_1 = '0'
PLAYER_2 = 'X'
player1 = ''
player2 = ''
init_round = True

pl_map = []
piece = []
coords = []

def parse_piece(stdin):
	i = 0
	for line in stdin:
		if i > map_size_y - 1:
			return
		piece.append(line)
		i += 1

def get_coords(spl):
	str1, str2 = spl[-1], spl[-2]
	str2 = str2[1:-1]
	str1 = str1[:-1]
	if not re.match("^[0-9]*$", str1) or not re.match("^[0-9]*$", str2):
		error_and_quit('wrong coords')
	return [int(str2), int(str1)]

def parse_map_init():
	i = 0
	for line in sys.stdin:
		spl = line.split(' ')
		if 'Plateau' in spl and not i and not init_round:
			map_size_y = spl[1]
			map_size_x = spl[2]
		elif 'p1' in spl and not i and init_round:
			player1 = PLAYER_1
		elif 'p2' in spl and not i and init_round:
			player1 = PLAYER_2
		elif 'Plateau' in spl and i and init_round:
			init_round = False
			map_size_y = spl[1]
			map_size_x = spl[2]
		elif re.match('^ +[0-9]+$', line):
			continue
		elif re.match(f'^[0-9]+ .{map_size_x}$', line):
			pl_map.append(line)
		elif 'Piece' in spl:
			piece_size_y = spl[1]
			piece_size_x = spl[2]
			parse_piece(sys.stdin)
		elif PLAYER_1 in spl or PLAYER_2 in spl:
			coords = get_coords(spl)
		else:
			error_and_quit(f'Something\'s wrong in your input, guys. Here\'s the faulty line: {line}')

def error_and_quit(mes):
	print('Error:', mes)
	quit()

if not coords:
	error_and_quit('no coords')

curr_y = coords[0]
for item in piece:
	pl_map[curr_y][coords[1]] = item
	curr_y += 1

for line in pl_map:
	print(line)
