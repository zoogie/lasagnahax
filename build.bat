make clean
make
COPY /B Garfield.sav.template + payload.bin + otherapp.bin Garfield.sav
py -3 sploit.py
cp Garfield.sav "G:\JKSV\Saves\Garfield Kart\tst"

pause