# lasagnahax
- Secondary userland exploit for Garfield Kart EU and US

# Thanks
- Tuxsh for mentioning the exploitability of this title on discord. 
- Tuxsh [Universal Otherapp](https://github.com/TuxSH/universal-otherapp)
- Yellows8 [3ds_ropkit](https://github.com/yellows8/3ds_ropkit)

# Directions
0) These directions are intended for experienced 3DS homebrew users only. There are more convenient exploits at https://3ds.hacks.guide for the general public.
1) Copy the Garfield.sav release file and overwrite your current save file of the same name. Checkpoint and JKSV can do this. This will erase your save data.
2) Set up [SafeB9SInstaller](https://github.com/d0k3/SafeB9SInstaller/releases) to your SD card. The SafeB9SInstaller.bin file needs to be on the SD root.  
3) Make a boot9strap folder and put [boot9strap.firm](https://github.com/SciresM/boot9strap/releases/tag/1.3) and boot9strap.firm.sha inside of it.
4) Boot the game and a. tap the lower left icon b. tap garfield's head (not the X beside his head) c. tap the gear icon. This should load universal-otherapp and then safeB9SInstaller.
5) Proceed with installing boot9strap. You know what to do next since you're the experienced user noted in step 0.

# Exploit

Stack smash via long profile name string in savegame. <br>