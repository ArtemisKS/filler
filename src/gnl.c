/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   gnl.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vdzhanaz <vdzhanaz@student.unit.ua>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 19:19:53 by akupriia          #+#    #+#             */
/*   Updated: 2019/03/21 21:42:46 by vdzhanaz         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../includes/filler.h"

static int		ft_read(char *buff, t_line *curr)
{
	int		ret;
	char	*tmp;

	if (!(ret = read(curr->fd, buff, BUFF_SIZE)))
		return (0);
	buff[ret] = '\0';
	tmp = curr->str;
	curr->str = ft_strjoin(tmp, buff);
	ft_strdel(&tmp);
	return (ret);
}

static int		ft_ret_line(char **str, char **line)
{
	char	*tmp1;
	char	*tmp2;

	if (!ft_strlen(*str))
		return (0);
	tmp1 = ft_strchr(*str, '\n');
	*tmp1 = '\0';
	*line = ft_strdup(*str);
	tmp2 = *str;
	*str = ft_strdup(tmp1 + 1);
	ft_strdel(&tmp2);
	return (1);
}

static t_line	*ft_curr(t_line **list, const int fd)
{
	t_line	*tmp;
	t_line	*new;

	tmp = *list;
	while (tmp)
	{
		if (tmp->fd == fd)
			return (tmp);
		tmp = tmp->next;
	}
	new = (t_line*)malloc(sizeof(t_line));
	new->str = ft_strnew(0);
	new->fd = fd;
	new->next = *list;
	*list = new;
	return (new);
}

int				get_next_line(const int fd, char **line)
{
	static t_line	*list = NULL;
	t_line			*curr;
	char			buff[BUFF_SIZE + 1];
	int				xr;

	if (fd < 0 || line == NULL || BUFF_SIZE < 1)
		return (-1);
	ft_bzero(buff, BUFF_SIZE + 1);
	curr = ft_curr(&list, fd);
	while (1)
	{
		if (ft_strchr(curr->str, '\n'))
			return (ft_ret_line(&(curr->str), line));
		if ((xr = ft_read(buff, curr)) == -1)
			return (-1);
		if (xr == 0)
		{
			if (!ft_strlen(curr->str))
				return (0);
			*line = ft_strdup(curr->str);
			ft_bzero(curr->str, ft_strlen(curr->str));
			return (1);
		}
	}
	return (1);
}
