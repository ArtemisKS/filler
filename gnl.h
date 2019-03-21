/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   gnl.h                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vdzhanaz <vdzhanaz@student.unit.ua>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/03/25 19:23:09 by akupriia          #+#    #+#             */
/*   Updated: 2019/03/21 21:43:33 by vdzhanaz         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GNL_H

# define GNL_H
# define BUFF_SIZE 100
# include <stdlib.h>
# include <stdio.h>
# include <fcntl.h>
# include <sys/types.h>
# include <sys/stat.h>
# include "libft/libft.h"

typedef struct		s_line
{
	int				fd;
	char			*str;
	struct s_line	*next;
}					t_line;

int					get_next_line(int fd, char **line);

#endif
