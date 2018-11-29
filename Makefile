NAME		=	akupriia.filler
LIBFT_DIR	=	ft_printf
LIBFT		=	$(LIBFT_DIR)/libftprintf.a
FILENAMES	=	make_map.c \
				gnl.c		\
				algorithm.c	 \
				parse_map.c
OBJECTS		=	$(addprefix ./obj/, $(FILENAMES:.c=.o))
FLAGS		=	-Wall -Wextra -Werror
CC			=	gcc


all: $(NAME)

$(NAME): $(LIBFT) $(OBJECTS)
	$(CC) -o $@ $(FLAGS) $^

$(LIBFT):
	make -C $(LIBFT_DIR)/

obj:
	mkdir obj/

obj/%.o: ./%.c | obj
	$(CC) $(FLAGS) -c $< -o $@

clean:
	rm -rf obj/
	make -C $(LIBFT_DIR)/ fclean

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re one two
