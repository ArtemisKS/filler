# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akupriia <akupriia@student.unit.ua>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/21 21:15:35 by akupriia          #+#    #+#              #
#    Updated: 2019/04/02 14:28:29 by akupriia         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME		:=	assets/players/akupriia.filler

LIBFT_DIR	:=	ft_printf
LIBFT		:=	$(LIBFT_DIR)/libftprintf.a
SCR			:=	src
INCLUDES	:=	includes
FILENAMES	:=	$(SCR)/make_map.c \
				$(SCR)/gnl.c		\
				$(SCR)/algorithm.c	 \
				$(SCR)/parse_map.c
OBJ			:=	$(FILENAMES:.c=.o)
FLAGS		:=	-Wall -Wextra -Werror -I./$(INCLUDES)
CC			:=	gcc

all: $(NAME)

$(NAME): $(LIBFT) $(OBJ)
	$(CC) -o $@ $(FLAGS) $^

$(LIBFT):
	make -C $(LIBFT_DIR)

clean:
	make -C $(LIBFT_DIR)
	rm -f $(OBJ)
	rm -rf obj/

fclean: clean
	make fclean -C $(LIBFT_DIR)
	rm -f $(OBJ)
	rm -f $(NAME)

re: fclean all

mclean:
	rm -f $(OBJ)

mfclean:
	rm -f $(NAME)

mre: mfclean all

.PHONY: all clean fclean re one two
