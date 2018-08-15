say -v Karen "let the games begin!"

crosses="🔷 "
crosses_mini="🔹 "
noughts="🔶 "
noughts_mini="🔸 "
points="◽️ "

sed "s/O/$crosses/g" |
sed "s/X/$noughts/g" |
sed "/^0.. /s/x/$noughts_mini/g" |
sed "/^0.. /s/o/$crosses_mini/g" |
sed "/^0.. /s/\./$points/g"

# purple=$(printf "\033[34mX\033[0m")
# blue=$(printf "\033[35mO\033[0m")

# sed "s|X|$purple|g" |
# sed "s|O|$blue|g" |
# sed "/^0.. /s|x|$purple|g" |
# sed "/^0.. /s|o|$blue|g"

say -v Karen "Thanks for the game!"