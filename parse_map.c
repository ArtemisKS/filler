/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_map.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: akupriia <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 18:54:02 by akupriia          #+#    #+#             */
/*   Updated: 2018/03/25 18:54:03 by akupriia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "filler.h"

int				main(void)
{
	char	*line;
	t_map	*tm;

	tm = (t_map *)malloc(sizeof(t_map));
	line = NULL;
	get_next_line1(0, &line);
	if (ft_strstr(line, " p1 "))
		tm->player = PLAYER_1;
	else
		tm->player = PLAYER_2;
	tm->enemy = (tm->player == PLAYER_2) ? PLAYER_1 : PLAYER_2;
	while (1)
	{
		if (!make_map(tm, line))
			break ;
	}
	ft_memdel((void **)&tm);
	return (0);
}

void			calc_coords(t_map *tm, t_coord *tc)
{
	int		i;
	int		k;
	int		j;

	i = 0;
	j = 0;
	while (i < tm->p_y)
	{
		k = 0;
		while (k < tm->p_x)
		{
			if (tm->token[i][k] == '*')
			{
				tc->y[j] = i;
				tc->x[j] = k;
				j++;
			}
			k++;
		}
		i++;
	}
}

void			form_map(t_map *tm, char *line)
{
	int	i;

	i = 0;
	while (i <= tm->y_n)
	{
		get_next_line1(0, &line);
		if (i)
			tm->map[i - 1] = ft_strdup(line + 4);
		ft_strdel(&line);
		i++;
	}
}

void			form_token(t_map *tm, char *line)
{
	int	i;

	i = 0;
	while (i < tm->p_y)
	{
		get_next_line1(0, &line);
		tm->token[i] = ft_strdup(line);
		ft_strdel(&line);
		i++;
	}
}

int				count_pieces(t_map *tm)
{
	int		i;
	int		j;
	int		count;

	i = 0;
	count = 0;
	while (i < tm->p_y)
	{
		j = 0;
		while (j < tm->p_x)
		{
			if (tm->token[i][j] == '*')
				count++;
			j++;
		}
		i++;
	}
	return (count);
}
