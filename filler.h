/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   filler.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: akupriia <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/11 20:28:42 by akupriia          #+#    #+#             */
/*   Updated: 2018/03/11 20:28:42 by akupriia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FILLER_H
# define FILLER_H

# define PLAYER_1 'O'
# define PLAYER_2 'X'

# include "libft/libft.h"
# include "libft/ft_printf/ft_printf.h"
# include "gnl.h"

typedef struct		s_map
{
	char			**map;
	char			**token;
	char			player;
	char			enemy;
	int				y_n;
	int				x_n;
	int				p_x;
	int				p_y;
	int				piece_num;
	int				epiece_num;
	int				opt_x;
	int				opt_y;
	int				len;
}					t_map;

typedef struct		s_coord
{
	int				x[100];
	int				y[100];
	int				n;
}					t_coord;

int					make_map(t_map *tm, char *line);
int					point_map_valid(t_map *tm, t_coord *tc);
void				init_coord(t_coord *tc, t_map *tm);
void				cycle_alg1(int *x, int *y, t_map *tm);
void				cycle_alg(int *x, int *y, t_map *tm);
void				algorithm(t_map *tm, int x, int y);
int					check_coords(t_map *tm, int i, int j, t_coord *tc);
int					point_map_valid(t_map *tm, t_coord *tc);
int					abs(int n);
void				form_map(t_map *tm, char *line);
void				form_token(t_map *tm, char *line);
int					count_pieces(t_map *tm);
void				calc_coords(t_map *tm, t_coord *tc);

#endif
