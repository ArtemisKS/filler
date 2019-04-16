#!/usr/bin/env python3.7

import sys
import graphics as gr
import re
import time
import select

map_size_x, map_size_y = 0, 0
piece_size_x, piece_size_y = 0, 0
iter_ind = 0
PLAYER_1 = 'O'
PLAYER_2 = 'X'
player = PLAYER_1
init_round = True
BOX_SIZE = 20
Y_INDENT = 100
INIT_X = Y_INDENT
INIT_Y = Y_INDENT
SCR_WIDTH = 1200
SCR_HEIGHT = 1200
LINE_WIDTH = 1
player1_name = ''
player2_name = ''
RED = gr.color_rgb(200, 0, 0)
BLUE = gr.color_rgb(0, 0, 200)


# pl_map = []
arena = None
piece = []
init_coords = {'X' : [None, None], 'O': [None, None]}

win = gr.GraphWin('filler visualization', SCR_WIDTH, SCR_HEIGHT)
win.setBackground(gr.color_rgb(255, 255, 255))

def error_and_quit(mes):
	print('Error:', mes)
	quit()

if not select.select([sys.stdin,],[],[],0.0)[0]:
    error_and_quit('No data in stdin')

def make_rect(x1, y1, x2, y2, color, line_width):
	rect = gr.Rectangle(gr.Point(x1, y1), gr.Point(x2, y2))
	rect.setOutline(color)
	rect.setWidth(line_width)
	return rect

def parse_piece(stdin, piece_size_y):
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
	if not re.match("^-?[0-9]*$", str1) or not re.match("^-?[0-9]*$", str2):
		error_and_quit('wrong coords')
	return [int(str2), int(str1)]

def det_item_indices(item, x_pos):
	st_ind = item.index('*') + x_pos
	for j in range(piece_size_x - 1, -1, -1):
		if item[j] == '*':
			end_ind = x_pos + j
			return st_ind, end_ind
	return st_ind, None

def draw_line(x1, y1, x2, y2, color):
	line = gr.Line(gr.Point(x1, y1), gr.Point(x2, y2))
	line.setOutline(color)
	line.setWidth(LINE_WIDTH)
	line.draw(win)
	return line

def draw_lines(color):
	for i in range(map_size_y + 1):
		cur_y = INIT_Y + i * BOX_SIZE
		draw_line(INIT_X, cur_y, INIT_X + (map_size_x - 1) * BOX_SIZE, cur_y, color)
	for i in range(map_size_x):
		cur_x = INIT_X + i * BOX_SIZE
		draw_line(cur_x, INIT_Y, cur_x, INIT_Y + map_size_y * BOX_SIZE, color)

def draw_start_label(starter):
	text = gr.Text(gr.Point(win.getWidth()/2 - 25, SCR_HEIGHT - INIT_Y/2), 'Click on the screen to start')
	text.setTextColor(RED if starter == PLAYER_1 else BLUE)
	text.setSize(25)
	text.setStyle('italic')
	text.draw(win)
	return text

def draw_quit_label(winner):
	text = gr.Text(gr.Point(win.getWidth()/2 - 25, SCR_HEIGHT - INIT_Y/2), 'Click on the screen to quit')
	text.setTextColor(RED if winner == player1_name else BLUE)
	text.setSize(25)
	text.setStyle('italic')
	text.draw(win)

def draw_arena():
	global init_round
	init_round = False
	cur_y = INIT_Y
	print(f'map_size_y: {map_size_y}; map_size_x: {map_size_x}')
	for i in range(map_size_y):
		cur_x = INIT_X
		for j in range(map_size_x - 1):
			rect = make_rect(cur_x, cur_y, cur_x + BOX_SIZE, cur_y + BOX_SIZE, gr.color_rgb(0, 0, 0), LINE_WIDTH)
			arena[i][j] = rect
			cur_x += BOX_SIZE
		cur_y += BOX_SIZE
	print(f'init_coords: {init_coords}')
	draw_lines(gr.color_rgb(0, 0, 0))
	# for line in arena:
	# 	for rect in line:
	# 		print(f'rect: {rect}; ', end='')
	# 	print()
	rect_x = arena[init_coords['X'][0]][init_coords['X'][1]]
	rect_y = arena[init_coords['O'][0]][init_coords['O'][1]]
	print(f'rect_x: {rect_x}; rect_y: {rect_y}')
	rect_y.setFill(RED)
	rect_x.setFill(BLUE)
	rect_y.draw(win)
	rect_x.draw(win)
	# for line in arena:
	# 	for rect in line:
	# 		print(f'rect: {rect}', end='')
	# 		rect.draw(win)
	# 	print()
	label = draw_start_label(player)
	win.getMouse()
	label.undraw()	

def token_is_cor(piece, y, x):
	y_incr = 0
	for line in piece:
		for i in range(len(line)):
			if line[i] == '*':
				rect = arena[(y + y_incr) % map_size_y][(x + i) % map_size_x]
				if rect.canvas:
					return True
		y_incr += 1
	return False

def end_and_quit():
	win.close()
	quit()

def draw_coords(coords, piece):
	y, x = coords[0], coords[1]
	y_incr = 0
	# init_rect =  arena[y % map_size_y][x % map_size_x]
	# init_rect =  arena[y][x]
	if token_is_cor(piece, y, x):
		for line in piece:
			if win.checkKey() == 'Escape':
				end_and_quit()
			for i in range(len(line)):
				if line[i] == '*':
					rect = arena[(y + y_incr) % map_size_y][(x + i) % map_size_x]
					# rect = arena[(y + y_incr)][(x + i)]
					if not rect.canvas:
						rect.setFill(RED if player == PLAYER_1 else BLUE)
						rect.draw(win)
			y_incr += 1

def finish_the_game(player1_points, player2_points):

	# rect_up = make_rect(win.getWidth()/2 - 190, 20, win.getWidth()/2 + 170, Y_INDENT/2)
	rect = make_rect(win.getWidth()/2 - 230, INIT_Y/4, win.getWidth()/2 + 230, INIT_Y - INIT_Y/4, gr.color_rgb(0, 0, 0), LINE_WIDTH + 1)
	winner = player1_name if player1_points >= player2_points else player2_name
	max_points = max(player1_points, player2_points)
	min_points = min(player1_points, player2_points)
	print(f'Player {winner} is winner!')
	text = gr.Text(gr.Point(win.getWidth()/2 - 2, INIT_Y/2), f'Player \'{winner}\' won with {max_points} against {min_points}!')
	rect.setFill(RED if winner == player1_name else BLUE)
	text.setTextColor(gr.color_rgb(0, 0, 0))
	text.setSize(20)
	rect.draw(win)
	text.draw(win)
	# rect_up.draw(win)
	draw_quit_label(winner)
	win.getMouse()
	end_and_quit()

def indent_and_scale():
	global BOX_SIZE, INIT_X, INIT_Y
	width = SCR_WIDTH - (INIT_X + Y_INDENT/2) * 2
	height = SCR_HEIGHT - (INIT_Y + Y_INDENT/2) * 2
	max_val = max(map_size_x, map_size_x)
	max_dim = max(width, height)
	if BOX_SIZE * max_val > max_dim:
		while BOX_SIZE * max_val > max_dim:
			BOX_SIZE -= 1
	else:
		while BOX_SIZE * max_val < max_dim:
			BOX_SIZE += 1
	indent = 0
	wid_len = BOX_SIZE * map_size_x
	end_x = SCR_WIDTH - INIT_X
	while INIT_X + indent < end_x - wid_len - indent:
		indent += 1
	INIT_X += indent
	indent = 0
	end_y = SCR_HEIGHT - INIT_Y
	h_len = BOX_SIZE * map_size_y
	while INIT_Y + indent < end_y - h_len - indent:
		indent += 1
	INIT_Y += indent		

def display(coords, piece):
	if not coords:
		error_and_quit('no coords')
	# for line in piece:
	# 	print(line)		
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

def parse_map_and_display():
	global map_size_x, map_size_y, piece_size_x, piece_size_y, player
	# not_done_yet = True
	for line in sys.stdin:
		if win.checkKey() == 'Escape':
			end_and_quit()
		spl = line[:-1].split(' ')
		# print(f'spl: {spl}, i: {i}')
		if 'Plateau' in spl:
			if int(spl[1]) != map_size_y or int(spl[2][:-1]) != map_size_x:
				error_and_quit(f'new map_size({int(spl[1])}, {int(spl[2][:-1])}) is not equal to initial ({map_size_y}, {map_size_x})')
			continue
		elif re.match('^ +[0-9]+$', line) or re.match(f'^[0-9]+ .{{{map_size_x}}}$', line):
			# ar_line = spl[1]
			# if init_round and ('X' in ar_line or 'O' in ar_line):
			# 	key = 'X' if 'X' in ar_line else 'O'
			# 	init_coords[key][0] = arena_ind
			# 	init_coords[key][1] = ar_line.index(key)
			# pl_map.append(ar_line)
			# arena_ind += 1
			continue
		elif 'Piece' in spl:
			piece_size_y = int(spl[1])
			piece_size_x = int(spl[2][:-1])
			parse_piece(sys.stdin, piece_size_y)
			continue
		elif '<got' in spl:
			coords = get_coords(spl)
			player = spl[1][1]
			display(coords, piece)
			piece.clear()
			# print(f'curr_player: {player}')
			if player != PLAYER_1 and player != PLAYER_2:
				error_and_quit(f'your player\'s token is \'{player}\' and it isn\'t equal to \'{PLAYER_1}\' and \'{PLAYER_2}\'')
			# not_done_yet = True
			# time.sleep(3)
			continue
		elif spl[0] == '==' and (spl[1] == PLAYER_1 or spl[1] == PLAYER_2):
			spl_end = sys.stdin.readline().split(' ')
			finish_the_game(int(spl[-1]), int(spl_end[-1]))
		else:
			error_and_quit(f'Something\'s wrong in your input, guys. Here\'s the faulty line: \'{line}\'')
	return

def	init_parse_and_cycle():
	global player, map_size_x, map_size_y, player1_name, player2_name, piece, arena
	arena_ind = 0
	for line in sys.stdin:
		spl = line[:-1].split(' ')
		print(f'spl: {spl}')
		if 'p1' in spl or 'p2' in spl:
			pl_name = spl[4].split('/')[-1][:-1]
			if 'p1' in spl:
				player1_name = pl_name
			else:
				player2_name = pl_name
			continue
		elif 'Plateau' in spl:
			map_size_y = int(spl[1])
			map_size_x = int(spl[2][:-1])
			arena = [[gr.Rectangle(gr.Point(0, 0), gr.Point(0, 0))] * map_size_x for i in range(map_size_y)]
			continue
		elif re.match('^ +[0-9]+$', line):
			continue
		elif re.match(f'^[0-9]+ .{{{map_size_x}}}$', line):
			ar_line = spl[1]
			if 'X' in ar_line or 'O' in ar_line:
				key = 'X' if 'X' in ar_line else 'O'
				init_coords[key][0] = arena_ind
				init_coords[key][1] = ar_line.index(key)
			# pl_map.append(ar_line)
			arena_ind += 1
			continue
		elif line[0] == '#' or 'launched' in spl:
			continue
		elif 'Piece' in spl:
			piece_size_y = int(spl[1])
			# piece_size_x = int(spl[2][:-1])
			parse_piece(sys.stdin, piece_size_y)
			continue
		elif '<got' in spl:
			coords = get_coords(spl)
			print(f'piece: {piece}')
			player = spl[1][1]
			indent_and_scale()
			display(coords, piece)
			# del pl_map
			piece.clear()
			parse_map_and_display()
			# not_done_yet = True
			# time.sleep(3)
			continue
		else:
			error_and_quit(f'Something\'s wrong in your initial input, guys. Here\'s the faulty line: {line}')
	return

init_parse_and_cycle()
