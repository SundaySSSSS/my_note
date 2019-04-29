
#ifndef _CRC_H_
#define _CRC_H_


//#include "sys.h"
#include "typedef.h"

u16 Crc16(u8 *puchMsg, u16 usDataLen) ;
u8 GetLRC(u8 *pSendBuf,u16 uLen );
u8 Crc8( u8 *p, u8 len );
u8 Crc81( u8 *p, u8 len );

uint16_t stream_crc16_calc(const uint8_t* pMsg, u32 nLen);

#endif
