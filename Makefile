# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdzhanaz <vdzhanaz@student.unit.ua>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/21 21:15:35 by vdzhanaz          #+#    #+#              #
#    Updated: 2019/03/21 22:40:27 by vdzhanaz         ###   ########.fr        #
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

$(NAME): $(LIBFT) $(OBJ) $(VIS)
	$(CC) -o $@ $(FLAGS) $^

$(LIBFT):
	make -C $(LIBFT_DIR)

$(VIS):
	make -C visualisation

clean:
	make clean -C visualisation
	make -C $(LIBFT_DIR)
	rm -f $(OBJ)
	rm -rf obj/

fclean: clean
	make fclean -C visualisation
	make fclean -C $(LIBFT_DIR)
	rm -f $(OBJ)
	rm -f $(NAME)

re: fclean all

mclean:
	make clean -C visualisation
	rm -f $(OBJ)

mfclean:
	make fclean -C visualisation
	rm -f $(NAME)

mre: mfclean all

.PHONY: all clean fclean re one two
