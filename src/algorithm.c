/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   algorithm.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: akupriia <akupriia@student.unit.ua>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 18:50:17 by akupriia          #+#    #+#             */
/*   Updated: 2019/04/02 14:25:40 by akupriia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../includes/filler.h"

void			init_coord(t_coord *tc, t_map *tm)
{
	int i;

	i = 0;
	while (i < 100)
	{
		tc->x[i] = 0;
		tc->y[i] = 0;
		i++;
	}
	tm->opt_x = -1;
	tm->opt_y = -1;
	tm->len = 10000000;
}

int				check_coords(t_map *tm, int i, int j, t_coord *tc)
{
	int		k;
	int		count;
	int		count1;

	k = 0;
	count = 0;
	count1 = 0;
	while (k < tc->n)
	{
		if (i + tc->y[k] < 0 || j + tc->x[k] < 0
			|| i + tc->y[k] >= tm->y_n || j + tc->x[k] >= tm->x_n)
			return (0);
		if (tm->map[i + tc->y[k]][j + tc->x[k]] == tm->player)
			count++;
		if (tm->map[i + tc->y[k]][j + tc->x[k]] == tm->enemy)
			count1++;
		k++;
	}
	if (count != 1)
		return (0);
	if (count1)
		return (0);
	return (1);
}

int				point_map_valid(t_map *tm, t_coord *tc)
{
	int		i;
	int		j;
	int		fl;

	i = 0;
	fl = 0;
	while (i < tm->y_n)
	{
		j = 0;
		while (j < tm->x_n)
		{
			if (check_coords(tm, i, j, tc))
			{
				fl = 1;
				algorithm(tm, j, i);
			}
			j++;
		}
		i++;
	}
	if (!fl)
		return (0);
	return (1);
}

int				abs(int n)
{
	return (n >= 0 ? n : -n);
}

void			algorithm(t_map *tm, int x, int y)
{
	int		len;
	int		tx;
	int		ty;
	int		x2;
	int		y2;

	y2 = -1;
	while ((x2 = -1) == -1 && ++y2 < tm->y_n)
		while (++x2 < tm->x_n)
			if (tm->map[y2][x2] == tm->enemy && (ty = -1) == -1)
				while ((tx = -1) == -1 && ++ty < tm->p_y)
					while (++tx < tm->p_x)
						if (tm->token[ty][tx] == '*')
						{
							len = abs(y2 - (y + ty)) + abs(x2 - (x + tx));
							if (len < tm->len)
							{
								tm->opt_x = x;
								tm->opt_y = y;
								tm->len = len;
							}
						}
}
