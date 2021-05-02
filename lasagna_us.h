#define ROP_POPPC 0x00114aec
#define POP_R1PC 0x00151650
#define POP_R3PC 0x0011ed00
#define POP_R2R6PC 0x0011d0c4
#define POP_R4R6PC 0x0015ccc0 //: pop {r4, r5, r6, pc}
//      FAIL:				
#define POP_R4LR_BXR1 0x0010c5e8 // @@@@@@
//      FAIL:				#define POP_R4R8LR_BXR2 
#define POP_R4R5R6PC 0x00100e28
#define POP_R4FPPC 0x00100dd0
#define POP_R4R8PC 0x0010d020  // @@@@@@

#define ROP_STR_R1TOR0 0x0011272c
#define ROP_STR_R0TOR1 0x0013b098
#define ROP_LDR_R0FROMR0 0x0011703c
#define ROP_ADDR0_TO_R1 0x00125f68

#define MEMCPY 0x0015cfa4

//      FAIL:				
#define svcSleepThread 0x105954 // @@@@@@

#define GSPGPU_FlushDataCache 0x001370f4
#define GSPGPU_SERVHANDLEADR 0x001b49dc //EUR 0x001b49f4

#define IFile_Read 0x0011df78
#define IFile_Write 0x00125100

//      FAIL:				#define ROP_POPR3_ADDSPR3_POPPC 
#define POP_R0PC 0x0015be1c
#define ROP_LDRR1R1_STRR1R0 0x0013bebc
//      FAIL:				#define POP_R5R6PC 
//      FAIL:				#define ROP_CMPR0R1_ALT0 0x001451e4
#define ROP_CMPR0R1_ALT0 0x001451e4
#define MEMSET32_OTHER 0x0015ce58
#define svcControlMemory 0x0015a218
#define ROP_INITOBJARRAY 0x0015a4a5
#define svcCreateThread 0x001095c0 // @@@@@@
//      FAIL:				#define svcConnectToPort 
#define svcGetProcessId 0x0011bdf8
//      FAIL:				#define THROWFATALERR_IPC 
#define SRV_GETSERVICEHANDLE 0x00156ffc
//      FAIL:				#define CFGIPC_SecureInfoGetRegion 
#define ROP_COND_THROWFATALERR 0x00107350 // @@@@@@
#define GXLOW_CMD4 0x001371f8
#define GSP_SHAREDMEM_SETUPFRAMEBUF 0x00136ff0
#define GSPTHREAD_OBJECTADDR 0x001b3580
#define FS_MountSdmc 0x0011e030
#define FS_MountSavedata 0x00116b8c
#define IFile_Open 0x001521f8
#define IFile_Close 0x00151df4
#define IFile_Seek 0x00135190
