# filler
Will you be the best?

Create your player program to compete against other students on the
famous (or not) Filler board. The principle is simple: two players take on each other on
a board, and take turns placing the piece that the master of the game (supplied in the
form of a Ruby executable) gives them, earning points. The game stops as soon as a
piece can no longer be placed. Little playful project!

# Usage

To be able to run filler with visualisation, make sure you have python not lower than 3.6 installed  
To check and/or update, here are some helpful commands:

```
python --version
which python
brew install python
```

And, of course, don't forget about ```man```

```
make
./assets/filler_vm -f assets/maps/map02 -p1 assets/players/akupriia.filler -p2 assets/players/abarriel.filler | python filler_vis.py
```
