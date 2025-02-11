#ifndef __SKIP_INTERNAL_FATBINARY_HEADERS
#include "fatbinary_section.h"
#endif
#define __CUDAFATBINSECTION  ".nvFatBinSegment"
#define __CUDAFATBINDATASECTION  ".nv_fatbin"
asm(
".section .nv_fatbin, \"a\"\n"
".align 8\n"
"fatbinData:\n"
".quad 0x00100001ba55ed50,0x0000000000000210,0x0000004001010002,0x0000000000000140\n"
".quad 0x000000000000013f,0x0000003400010007,0x0000000000000000,0x0000000000002011\n"
".quad 0x0000000000000000,0x0000000000000368,0x010102464c457fa2,0x0002660001000733\n"
".quad 0xf8210001007e00be,0x0701780031000702,0x00340534000ef500,0x0040000200380040\n"
".quad 0x68732e0000010006,0x2e00626174727473,0xf100086d79270008,0x0078646e68735f00\n"
".quad 0x6f666e692e766e2e,0x676c6c6163910009,0x7091000e68706172,0x657079746f746f72\n"
".quad 0x612e6c6572af000e,0x4c005d6e6f697463,0x0000328c0a00010f,0x1100010004000300\n"
".quad 0x000100052f00184e,0x0008ffffffff4001,0x0008fd130008fe13,0x010073fffffffc65\n"
".quad 0x0036050025116f00,0x0e008801112c0001,0x2e00010040220001,0x1f0001080030005d\n"
".quad 0x40009d2f0400400b,0x010e022c13111300,0x5000482400290400,0x0100082200680202\n"
".quad 0x015b016000182600,0x4813000100700000,0xa406000620110040,0x01880817018a0400\n"
".quad 0x4068130000400b1f,0x081b000100102a00,0x0500000006570008,0x08701b00010c02e0\n"
".quad 0x00380f00df081700,0x000000000000501c,0x0000005001010001,0x0000000000000040\n"
".quad 0x0000004000000039,0x0000003400080005,0x0000000000000000,0x0000000000002011\n"
".quad 0x0000000000000000,0x0000000000000044,0x0000000000000048,0x0000000000000000\n"
".quad 0x22f000032f2f0a3c,0x6f69737265762e0a,0x742e0a352e38206e,0x6d73207465677261\n"
".quad 0x6464612e0a32355f,0x7a69735f73736572,0x0a0a0a0a34362065,0x0000000000000000\n"
".text\n");
#ifdef __cplusplus
extern "C" {
#endif
extern const unsigned long long fatbinData[68];
#ifdef __cplusplus
}
#endif
#ifdef __cplusplus
extern "C" {
#endif
static const __fatBinC_Wrapper_t __fatDeviceText __attribute__ ((aligned (8))) __attribute__ ((section (__CUDAFATBINSECTION)))= 
	{ 0x466243b1, 1, fatbinData, 0 };
#ifdef __cplusplus
}
#endif
