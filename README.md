# filler
Will you be the best?

Create your player program to compete against other students on the
famous (or not) Filler board. The principle is simple: two players take on each other on
a board, and take turns placing the piece that the master of the game (supplied in the
form of a Ruby executable) gives them, earning points. The game stops as soon as a
piece can no longer be placed. Little playful project!

## Usage

To be able to run filler with visualisation, make sure you have python not lower than 3.6 installed  
To check and/or update, here are some helpful commands:

```
python --version
which python
brew install python
```

And, of course, don't forget about ```man```
Then run

```
make
```

And everything's set up!

**To run the game**

Small map:
```
./assets/filler_vm -f assets/maps/map00 -p1 assets/players/akupriia.filler -p2 assets/players/abarriel.filler | python filler_vis.py
```

https://user-images.githubusercontent.com/35403190/156880161-946bc8ee-400e-47c4-a28e-6c6a4546eac9.mov

Medium map:
```
./assets/filler_vm -f assets/maps/map01 -p1 assets/players/akupriia.filler -p2 assets/players/abarriel.filler | python filler_vis.py
```

https://user-images.githubusercontent.com/35403190/156880156-5c816dae-7f32-4126-b6de-6f5b24d90570.mov

Big map:
```
./assets/filler_vm -f assets/maps/map02 -p1 assets/players/akupriia.filler -p2 assets/players/abarriel.filler | python filler_vis.py
```

https://user-images.githubusercontent.com/35403190/156879602-46a30bdd-7f74-4c13-baa5-a52f8bfc1012.mov

<img src="https://user-images.githubusercontent.com/35403190/156879613-8c19d884-722e-4bd7-aa3c-0720aea83211.JPG" width="650" height="650"/>
