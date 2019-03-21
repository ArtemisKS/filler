/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   visual.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vdzhanaz <vdzhanaz@student.unit.ua>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/03/21 21:44:38 by vdzhanaz          #+#    #+#             */
/*   Updated: 2019/03/21 22:38:38 by vdzhanaz         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef VISUAL_H
# define VISUAL_H

# include "../../includes/filler.h"
# define WIDTH 1200
# define HEIGHT 600
# define ECHAP	53
# define WINDOW_NAME "Filler_visual"
# define TITLE_IMAGE "../assets/fond.xpm"

typedef struct		s_env
{
	char			*p1;
	char			*p2;
	float			scorep1;
	float			scorep2;
	char			**map;
	int				h;
	int				l;
	int				r;
	int				v;
	int				b;
	int				map_size_x;
	int				map_size_y;
	char			*ret;
	void			*ret2;
	void			*win;
	void			*mlx;
	void			*img;
	void			*img2;
	int				bits_per_pixel;
	int				size_line;
	int				endian;
	int				pause;
}					t_env;

void				modif_color(int r, int v, int b, t_env *p);
void				draw_score(t_env *p);
void				calc_score(t_env *p);
void				draw_rectangle(int start_x, int start_y, t_env *p);
void				draw(t_env *p);
int					is_number(char c);
int					is_aly_adj(t_env *p, int i, int i2);
void				print_final(t_env *p);
void				draw_title(t_env *p);
void				draw_score(t_env *p);
int					is_number(char c);
void				get_map_size(char *line, t_env *p);
void				read_output(t_env *p);
void				modif_color(int r, int v, int b, t_env *p);
void				draw_square(int start_x, int start_y,
	int size, t_env *p);
void				draw_background(t_env *p);
void				draw_map(t_env *p);
void				draw_menu(t_env *p);

#endif
