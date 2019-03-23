import sys
import graphics as gr
import re
import time

map_size_x, map_size_y = 0, 0
piece_size_x, piece_size_y = 0, 0
iter_ind = 0
PLAYER_1 = 'O'
PLAYER_2 = 'X'
player = ''
init_round = True

pl_map = []
piece = []

def error_and_quit(mes):
	print('Error:', mes)
	quit()

def parse_piece(stdin):
	i = 0
	# print(f'piece_size_y: {piece_size_y}')
	for line in stdin:
		# print(f'line: {line[:-1]}, i: {i}')
		piece.append(line[:-1])
		if i == piece_size_y - 1:
			return
		i += 1

def get_coords(spl):
	str1, str2 = spl[-1], spl[-2]
	str2 = str2[1:-1]
	str1 = str1[:-1]
	if not re.match("^[0-9]*$", str1) or not re.match("^[0-9]*$", str2):
		error_and_quit('wrong coords')
	return [int(str2), int(str1)]

def parse_map_init():
	global init_round, map_size_x, map_size_y, piece_size_x, piece_size_y, player
	i = 0
	for line in sys.stdin:
		spl = line[:-1].split(' ')
		# print(f'spl: {spl}, i: {i}')
		if 'Plateau' in spl and not i and not init_round:
			map_size_y = int(spl[1])
			map_size_x = int(spl[2][:-1])
			continue
		elif re.match('^ +[0-9]+$', line):
			continue
		elif re.match(f'^[0-9]+ .{{{map_size_x}}}$', line):
			pl_map.append(spl[1])
			continue
		elif 'Piece' in spl:
			piece_size_y = int(spl[1])
			piece_size_x = int(spl[2][:-1])
			parse_piece(sys.stdin)
			continue
		elif '<got' in spl:
			coords = get_coords(spl)
			# print(f'coords: {coords}')
			continue
		elif 'p1' in spl and not i and init_round:
			init_round = False
			player = PLAYER_1
			continue
		elif 'p2' in spl and not i and init_round:
			init_round = False
			player = PLAYER_2
			continue
		elif 'Plateau' in spl and i and init_round:
			map_size_y = int(spl[1])
			map_size_x = int(spl[2])
			continue
		elif 'exec' in spl or 'launched' in spl:
			continue
		else:
			error_and_quit(f'Something\'s wrong in your input, guys. Here\'s the faulty line: {line}')
		i += 1
	return coords

def det_item_indices(item, x_pos):
	st_ind = item.index('*') + x_pos
	for j in range(piece_size_x - 1, 0, -1):
		if item[j] == '*':
			end_ind = x_pos + j
			return st_ind, end_ind
	return st_ind, None

def main():
	i = 0
	for line in sys.stdin:
		if i > 4:
			break
		i += 1
	coords = parse_map_init()
	if not coords:
		error_and_quit('no coords')

	for line in pl_map:
		print(line)

	for line in piece:
		print(line)		

	res_arena = []
	curr_y = coords[0]
	init_x = coords[1]
	res_arena += pl_map[:curr_y]
	for item in piece:
		line = pl_map[curr_y]
		st_ind, end_ind = det_item_indices(item, init_x)
		# print(f'st_ind: {st_ind}, end_ind: {end_ind}')
		edited_part = ''.join(map(lambda x: player if x == '*' else x, item[st_ind-init_x:end_ind + 1-init_x]))
		new_line = line[:st_ind] + edited_part + line[end_ind + 1:]
		res_arena.append(new_line)
		curr_y += 1
	res_arena += pl_map[curr_y:]	

	for line in res_arena:
		print(line)
main()
