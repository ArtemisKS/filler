# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vdzhanaz <vdzhanaz@student.unit.ua>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/02/04 10:13:27 by lcharvol          #+#    #+#              #
#    Updated: 2019/03/21 22:42:47 by vdzhanaz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME		:= visual

LIBFT_DIR	:=	../ft_printf
LIBFT		:=	$(LIBFT_DIR)/libftprintf.a
SCR			:=	srcs
INCLUDES	:=	includes
SRCS 		:=	$(SCR)/draw.c \
				$(SCR)/parcing.c \
				$(SCR)/main.c \
				$(SCR)/other.c \
				$(SCR)/other2.c \

FLAGS		:= -Wall -Werror -Wextra -I./$(INCLUDES)

OBJ			:= $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	gcc -o $(NAME) $(FLAGS) $(OBJ) -L../$(INCLUDES)/mlx/ -lmlx -framework OpenGL -framework AppKit $(LIBFT)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all
