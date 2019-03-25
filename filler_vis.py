import sys
import graphics as gr
import re
import time

map_size_x, map_size_y = 0, 0
piece_size_x, piece_size_y = 0, 0
iter_ind = 0
PLAYER_1 = 'X'
PLAYER_2 = 'O'
player = ''
init_round = True
player_assigned = False
BOX_SIZE = 20
Y_INDENT = 200
INIT_X = Y_INDENT + 20
INIT_Y = Y_INDENT + 20
SCR_WIDTH = 1200
SCR_HEIGHT = 1200
LINE_WIDTH = 2
player1_points = 1
player2_points = 1


pl_map = []
piece = []
init_coords = {'X' : [None, None], 'O': [None, None]}

win = gr.GraphWin('filler visualization', SCR_WIDTH, SCR_HEIGHT)
win.setBackground(gr.color_rgb(255, 255, 255))

def error_and_quit(mes):
	print('Error:', mes)
	quit()

def make_rect(x1, y1, x2, y2):
	return gr.Rectangle(gr.Point(x1, y1), gr.Point(x2, y2))

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

def	parse_init():
	global player, map_size_x, map_size_y, player_assigned
	for line in sys.stdin:
		spl = line[:-1].split(' ')
		if 'p1' in spl and not player_assigned:
			player = PLAYER_1
			player_assigned = True
			continue
		elif 'p2' in spl and not player_assigned:
			player = PLAYER_2
			player_assigned = True
			continue
		elif 'Plateau' in spl:
			map_size_y = int(spl[1])
			map_size_x = int(spl[2][:-1])
			arena = [[gr.Rectangle(gr.Point(0, 0), gr.Point(0, 0))] * map_size_x for i in range(map_size_y)]
			return arena
		elif 'exec' in spl or 'launched' in spl:
			continue
		elif line[0] == '#':
			continue
		else:
			error_and_quit(f'Something\'s wrong in your initial input, guys. Here\'s the faulty line: {line}')
		i += 1
	return None
	
if init_round:
	arena = parse_init()

def parse_map_and_display():
	global init_round, map_size_x, map_size_y, piece_size_x, piece_size_y, player
	arena_ind = 0
	# not_done_yet = True
	for line in sys.stdin:
		spl = line[:-1].split(' ')
		# print(f'spl: {spl}, i: {i}')
		if 'Plateau' in spl:
			if int(spl[1]) != map_size_y or int(spl[2][:-1]) != map_size_x:
				error_and_quit(f'new map_size({int(spl[1])}, {int(spl[2][:-1])}) is not equal to initial ({map_size_y}, {map_size_x})')
			continue
		# if not init_round and not_done_yet:
		# 	i = 0
		# 	for line in sys.stdin:
		# 		if i >= map_size_x:
		# 			break
		# 		i += 1
		# 	not_done_yet = False
		elif re.match('^ +[0-9]+$', line):
			continue
		elif re.match(f'^[0-9]+ .{{{map_size_x}}}$', line):
			ar_line = spl[1]
			if init_round and ('X' in ar_line or 'O' in ar_line):
				key = 'X' if 'X' in ar_line else 'O'
				init_coords[key][0] = arena_ind
				init_coords[key][1] = ar_line.index(key)
			pl_map.append(ar_line)
			arena_ind += 1
			continue
		elif 'Piece' in spl:
			piece_size_y = int(spl[1])
			piece_size_x = int(spl[2][:-1])
			parse_piece(sys.stdin)
			continue
		elif '<got' in spl:
			coords = get_coords(spl)
			display(coords, piece)
			pl_map.clear()
			piece.clear()
			player = PLAYER_1 if player == PLAYER_2 else PLAYER_2
			# not_done_yet = True
			# time.sleep(3)
			arena_ind = 0
			continue
		else:
			error_and_quit(f'Something\'s wrong in your input, guys. Here\'s the faulty line: {line}')
	return

def det_item_indices(item, x_pos):
	st_ind = item.index('*') + x_pos
	for j in range(piece_size_x - 1, -1, -1):
		if item[j] == '*':
			end_ind = x_pos + j
			return st_ind, end_ind
	return st_ind, None

def draw_arena():
	global init_round
	init_round = False
	cur_y = INIT_Y
	print(f'map_size_y: {map_size_y}; map_size_x: {map_size_x}')
	for i in range(map_size_y):
		cur_x = INIT_X
		for j in range(map_size_x - 1):
			rect = make_rect(cur_x, cur_y, cur_x + BOX_SIZE, cur_y + BOX_SIZE)
			rect.setOutline(gr.color_rgb(0, 0, 0))
			rect.setWidth(LINE_WIDTH)
			arena[i][j] = rect
			cur_x += BOX_SIZE
		cur_y += BOX_SIZE
	print(f'init_coords: {init_coords}')
	# for line in arena:
	# 	for rect in line:
	# 		print(f'rect: {rect}; ', end='')
	# 	print()
	rect_x = arena[init_coords['X'][0]][init_coords['X'][1]]
	rect_y = arena[init_coords['O'][0]][init_coords['O'][1]]
	print(f'rect_x: {rect_x}; rect_y: {rect_y}')
	rect_x.setFill(gr.color_rgb(255, 0, 0))
	rect_y.setFill(gr.color_rgb(0, 0, 255))
	for line in arena:
		for rect in line:
			print(f'rect: {rect}', end='')
			rect.draw(win)
		print()		

def draw_coords(coords, piece):
	global player1_points, player2_points
	y, x = coords[0], coords[1]
	y_incr = 0
	for line in piece:
		for i in range(len(line)):
			if line[i] == '*':
				rect = arena[(y + y_incr) % map_size_y][(x + i) % map_size_x]
				rect.setFill(gr.color_rgb(255, 0, 0) if player == 'X' else gr.color_rgb(0, 0, 255))
				rect.undraw()
				rect.draw(win)
				if player == PLAYER_1:
					player1_points += 1
				else:
					player2_points += 1
		y_incr += 1

def draw_quit_label(winner):
	text = gr.Text(gr.Point(win.getWidth()/2 - 25, SCR_HEIGHT - Y_INDENT), 'Click on the screen to quit')
	text.setTextColor(gr.color_rgb(255, 0, 0) if winner == PLAYER_1 else gr.color_rgb(0, 0, 255))
	text.setSize(25)
	text.setStyle('italic')
	text.draw(win)

def finish_the_game():
	rect_up = make_rect(win.getWidth()/2 - 190, 20, win.getWidth()/2 + 170, Y_INDENT/2)
	rect = make_rect(win.getWidth()/2 - 190, Y_INDENT/4, win.getWidth()/2 + 170, Y_INDENT - Y_INDENT/4)
	rect.setOutline(gr.color_rgb(0, 0, 0))
	rect.setWidth(LINE_WIDTH)
	rect_up.setOutline(gr.color_rgb(0, 0, 0))
	rect_up.setWidth(LINE_WIDTH)
	winner = PLAYER_1 if player1_points >= player2_points else PLAYER_2
	max_points = max(player1_points, player2_points)
	min_points = min(player1_points, player2_points)
	text = gr.Text(gr.Point(win.getWidth()/2 - 15, Y_INDENT/2), f'Player {winner} won with {max_points} against {min_points}!')
	rect.setFill(gr.color_rgb(255, 0, 0) if winner == PLAYER_1 else gr.color_rgb(0, 0, 255))
	rect_up.setFill(gr.color_rgb(255, 0, 0) if winner == PLAYER_1 else gr.color_rgb(0, 0, 255))
	text.setTextColor(gr.color_rgb(0, 0, 0))
	text.setSize(20)
	rect.draw(win)
	text.draw(win)
	# rect_up.draw(win)
	draw_quit_label(winner)
	win.getMouse()
	win.close()
	quit()


def display(coords, piece):
	if not coords:
		error_and_quit('no coords')

	for line in piece:
		print(line)		

	if len(pl_map) == 0 or not pl_map:
		finish_the_game()
	# print(f'len(pl_map): {len(pl_map)}')
	# res_arena = []
	# curr_y = coords[0]
	# init_x = coords[1]
	# res_arena += pl_map[:curr_y]
	# print(f'curr_y: {curr_y}')
	# for item in piece:
	# 	for line in pl_map:
	# 		print(line)
	# 	print(f'curr_y % map_size_y: {curr_y % map_size_y}')
	# 	line = pl_map[curr_y % map_size_y]
	# 	if '*' not in item:
	# 		res_arena.append(line)
	# 	else:
	# 		st_ind, end_ind = det_item_indices(item, init_x)
	# 		# print(f'st_ind: {st_ind}, end_ind: {end_ind}')
	# 		edited_part = ''.join(map(lambda x: player if x == '*' else x, item[st_ind-init_x:end_ind + 1-init_x]))
	# 		new_line = line[:st_ind] + edited_part + line[end_ind + 1:]
	# 		res_arena.append(new_line)
	# 	curr_y += 1
	# res_arena += pl_map[curr_y:]	

	# for line in res_arena:
	# 	print(line)
	if init_round:
		draw_arena()
	draw_coords(coords, piece)

parse_map_and_display()