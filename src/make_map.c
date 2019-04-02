/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   make_map.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: akupriia <akupriia@student.unit.ua>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 19:10:11 by akupriia          #+#    #+#             */
/*   Updated: 2019/04/02 14:25:44 by akupriia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../includes/filler.h"

static void		free_arr(void ***arr, size_t i)
{
	while (i != 0)
	{
		free((*arr)[--i]);
		(*arr)[i] = NULL;
	}
	free(*arr);
	*arr = NULL;
}

static int		free_structs(t_coord *tc, t_map *tm)
{
	ft_memdel((void **)&tc);
	free_arr((void ***)&(tm->map), tm->y_n + 1);
	free_arr((void ***)&(tm->token), tm->p_y + 1);
	return (1);
}

static void		read_msize(t_map *tm, char *line)
{
	int gnl;

	gnl = get_next_line(0, &line);
	tm->y_n = ft_atoi(line + 8);
	tm->x_n = ft_atoi(line + 11);
	if (gnl)
		ft_strdel(&line);
}

static void		read_tsize(t_map *tm, char *line)
{
	int gnl;

	gnl = get_next_line(0, &line);
	tm->p_y = ft_atoi(line + 6);
	tm->p_x = ft_atoi(line + 8);
	if (gnl)
		ft_strdel(&line);
}

int				make_map(t_map *tm, char *line)
{
	t_coord *tc;

	tc = (t_coord *)malloc(sizeof(t_coord));
	read_msize(tm, line);
	init_coord(tc, tm);
	tm->map = (char **)ft_memalloc(sizeof(char *) * (tm->y_n + 1));
	form_map(tm, line);
	if (!tm->map[0])
	{
		free_arr((void ***)&(tm->map), tm->y_n + 1);
		ft_memdel((void **)&tc);
		return (0);
	}
	read_tsize(tm, line);
	tm->token = (char **)ft_memalloc(sizeof(char *) * (tm->p_y + 1));
	form_token(tm, line);
	tc->n = count_pieces(tm);
	calc_coords(tm, tc);
	point_map_valid(tm, tc) == 0 ? (free_structs(tc, tm)
	&& ft_printf("%d %d\n", 0, 0)) : (free_structs(tc, tm)
	&& ft_printf("%d %d\n", tm->opt_y, tm->opt_x));
	return (1);
}
