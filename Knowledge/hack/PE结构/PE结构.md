# PE结构
```
* PE结构
** PE的基本概念
全称为: Portable Executable, 是微软Win32环境可移植可执行文件(如exe、dll、vxd、sys和vdm等)的标准文件格式。
PE格式的定义主要位于windows中的w
innt.h中

** MS-DOS头
每一个PE文件是以一个DOS程序开始的, PE文件的第一个字节起始于一个MS-DOS头, 被称为: IMAGE_DOS_HEADER
结构体定义为:
#+BEGIN_SRC C++
typedef struct _IMAGE_DOS_HEADER {      // DOS .EXE
header
    WORD   e_magic;                     // Magic number (值为: 4D 5A, DOS可执行文件标记)
    WORD   e_cblp;                      // Bytes on last page of file
    WORD   e_cp;                        // Pages in file
    WORD   e_crlc;                      // Relocations
    WORD   e_cparhdr;                   // Size of header in paragraphs
    WORD   e_minalloc;                  // Minimum extra paragraphs needed
    WORD   e_maxalloc;                  // Maximum extra paragraphs needed
    WORD   e_ss;                        // Initial (relative) SS value
    WORD   e_sp;                        // Initial SP value
    WORD   e_csum;                      // Checksum
    WORD   e_ip;                        // Initial IP value 初始指令入口(IP指针的初值)
    WORD   e_cs;                        // Initial (relative) CS value 初始堆栈入口
    WORD   e_lfarlc;                    // File address of relocation table
    WORD   e_ovno;                      // Overlay number
    WORD   e_res[4];                    // Reserved words
    WORD   e_oemid;                     // OEM identifier (for e_oeminfo)
    WORD   e_oeminfo;                   // OEM information; e_oemid specific
    WORD   e_res2[10];                  // Reserved words
    LONG   e_lfanew;                    // File address of new exe header 指向PE文件头
} IMAGE_DOS_HEADER, *PIMAGE_DOS_HEADER;
#+END_SRC

** PE文件头(PE Header)
PE Header是PE相关结构NT映像头IMAGE_NT_HEADERS的简称
定义:
#+BEGIN_SRC C++
typedef struct _IMAGE_NT_HEADERS {
    DWORD Signature;
    IMAGE_FILE_HEADER FileHeader;
    IMAGE_OPTIONAL_HEADER32 OptionalHeader;
} IMAGE_NT_HEADERS32, *PIMAGE_NT_HEADERS32;
#+END_SRC

*** Signature字段
其中: Signature应该被置为0x00004550, 如果不是此值, 说明不是一个有效的PE文件
(0x00004550 对应的ascii码为: "PE\0\0")

*** FileHeader字段

定义:
#+BEGIN_SRC C++
typedef struct _IMAGE_FILE_HEADER {
    WORD    Machine;	//可执行程序的目标CPU类型, 具体见下方
    WORD    NumberOfSections;
    DWORD   TimeDateStamp;
    DWORD   PointerToSymbolTable;
    DWORD   NumberOfSymbols;
    WORD    SizeOfOptionalHeader;
    WORD    Characteristics;
} IMAGE_FILE_HEADER, *PIMAGE_FILE_HEADER;
#+END_SRC

**** Machine字段
可执行程序的目标CPU类型
 0x014c: x86
 0x0200: Intel Itanium
 0x8664: x64

**** NumberOfSections
区块的数目

**** TimeDateStamp
文件的时间戳(何时被创建的, 为UTC时间)

**** PointerToSymbolTable
COFF符号表的文件偏移位置, 现在基本没用了

**** NumberOfSymbols
如果有COFF符号表, 它代表其中的符号数目

**** SizeOfOptionalHeader
标记了IMAGE_OPTIONAL_HEADER的大小, 对于32位PE, 此值通常为0x00E0, 对于64位PE32+文件, 通常为0x00f0

**** Characteristics
文件属性, 是下面几个值的或运算的结果， 一般exe文件为0x0100, dll文件为0x0210
#+BEGIN_SRC C++
#define IMAGE_FILE_RELOCS_STRIPPED           0x0001  // Relocation info stripped from file.
#define IMAGE_FILE_EXECUTABLE_IMAGE          0x0002  // File is executable  (i.e. no unresolved external references).
#define IMAGE_FILE_LINE_NUMS_STRIPPED        0x0004  // Line nunbers stripped from file.
#define IMAGE_FILE_LOCAL_SYMS_STRIPPED       0x0008  // Local symbols stripped from file.
#define IMAGE_FILE_AGGRESIVE_WS_TRIM         0x0010  // Aggressively trim working set
#define IMAGE_FILE_LARGE_ADDRESS_AWARE       0x0020  // App can handle >2gb addresses
#define IMAGE_FILE_BYTES_REVERSED_LO         0x0080  // Bytes of machine word are reversed.
#define IMAGE_FILE_32BIT_MACHINE             0x0100  // 32 bit word machine.
#define IMAGE_FILE_DEBUG_STRIPPED            0x0200  // Debugging info stripped from file in .DBG file
#define IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP   0x0400  // If Image is on removable media, copy and run from the swap file.
#define IMAGE_FILE_NET_RUN_FROM_SWAP         0x0800  // If Image is on Net, copy and run from the swap file.
#define IMAGE_FILE_SYSTEM                    0x1000  // System File.
#define IMAGE_FILE_DLL                       0x2000  // File is a DLL.
#define IMAGE_FILE_UP_SYSTEM_ONLY            0x4000  // File should only be run on a UP machine
#define IMAGE_FILE_BYTES_REVERSED_HI         0x8000  // Bytes of machine word are reversed.
#+END_SRC

*** OptionalHeader字段
定义:
#+BEGIN_SRC C++

typedef struct _IMAGE_OPTIONAL_HEADER {
    //
    // Standard fields.
    //
    WORD    Magic;
    BYTE    MajorLinkerVersion;
    BYTE    MinorLinkerVersion;
    DWORD   SizeOfCode;
    DWORD   SizeOfInitializedData;
    DWORD   SizeOfUninitializedData;
    DWORD   AddressOfEntryPoint;
    DWORD   BaseOfCode;
    DWORD   BaseOfData;
    //
    // NT additional fields.
    //
    DWORD   ImageBase;
    DWORD   SectionAlignment;
    DWORD   FileAlignment;
    WORD    MajorOperatingSystemVersion;
    WORD    MinorOperatingSystemVersion;
    WORD    MajorImageVersion;
    WORD    MinorImageVersion;
    WORD    MajorSubsystemVersion;
    WORD    MinorSubsystemVersion;
    DWORD   Win32VersionValue;
    DWORD   SizeOfImage;
    DWORD   SizeOfHeaders;
    DWORD   CheckSum;
    WORD    Subsystem;
    WORD    DllCharacteristics;
    DWORD   SizeOfStackReserve;
    DWORD   SizeOfStackCommit;
    DWORD   SizeOfHeapReserve;
    DWORD   SizeOfHeapCommit;
    DWORD   LoaderFlags;
    DWORD   NumberOfRvaAndSizes;
    IMAGE_DATA_DIRECTORY DataDirectory[IMAGE_NUMBEROF_DIRECTORY_ENTRIES];
} IMAGE_OPTIONAL_HEADER32, *PIMAGE_OPTIONAL_HEADER32;
#+END_SRC

**** AddressOfEntryPoint
文件被执行时的入口地址, 是一个RVA地址

**** ImageBase
文件的优先装入地址, 当文件执行时, 如果可以, windows优先将其加载到此地址中, 如果此地址已经被占用, 则windows自行选择其他地址
exe文件使用独立的虚拟地址空间, 故优先装入地址不可能被占用
dll文件使用宿主exe的虚拟地址空间, 故可能被占用
默认 exe 的ImageBase为0x0040000, dll为0x1000000

**** SectionAlignment 和 FileAlignment
Sectionalignment 定义了被装入内存后的对其单位(x86架构一般为:0x1000)
FileAlignment 定义了存储在磁盘上的对其单位(默认为:0x0200)

**** Subsystem
指定使用界面的子系统
为下面几个值的或
#+BEGIN_SRC C++
#define IMAGE_SUBSYSTEM_UNKNOWN              0   // Unknown subsystem.
#define IMAGE_SUBSYSTEM_NATIVE               1   // Image doesn't require a subsystem.
#define IMAGE_SUBSYSTEM_WINDOWS_GUI          2   // Image runs in the Windows GUI subsystem.
#define IMAGE_SUBSYSTEM_WINDOWS_CUI          3   // Image runs in the Windows character subsystem.
#define IMAGE_SUBSYSTEM_OS2_CUI              5   // image runs in the OS/2 character subsystem.
#define IMAGE_SUBSYSTEM_POSIX_CUI            7   // image runs in the Posix character subsystem.
#define IMAGE_SUBSYSTEM_NATIVE_WINDOWS       8   // image is a native Win9x driver.
#define IMAGE_SUBSYSTEM_WINDOWS_CE_GUI       9   // Image runs in the Windows CE subsystem.
#define IMAGE_SUBSYSTEM_EFI_APPLICATION      10  //
#define IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER  11   //
#define IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER   12  //
#define IMAGE_SUBSYSTEM_EFI_ROM              13
#define IMAGE_SUBSYSTEM_XBOX                 14
#define IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION 16
#define IMAGE_SUBSYSTEM_XBOX_CODE_CATALOG    17
#+END_SRC

**** DataDirectory
数据目录表
PE中最重要的字段之一
由16个相同的IMAGE_DATA_DIRECTORY结构组成
定义如下:
#+BEGIN_SRC C++
typedef struct _IMAGE_DATA_DIRECTORY {
    DWORD   VirtualAddress;	//数据起始虚拟地址
    DWORD   Size;
} IMAGE_DATA_DIRECTORY, *PIMAGE_DATA_DIRECTORY;
#+END_SRC

这16个IMAGE_DATA_DIRECTORY的意义定义如下(例如, 数组第0个结构的意义为导出表)
#+BEGIN_SRC C++
#define IMAGE_DIRECTORY_ENTRY_EXPORT          0   // Export Directory 导出表
#define IMAGE_DIRECTORY_ENTRY_IMPORT          1   // Import Directory 导入表
#define IMAGE_DIRECTORY_ENTRY_RESOURCE        2   // Resource Directory 资源
#define IMAGE_DIRECTORY_ENTRY_EXCEPTION       3   // Exception Directory 
#define IMAGE_DIRECTORY_ENTRY_SECURITY        4   // Security Directory
#define IMAGE_DIRECTORY_ENTRY_BASERELOC       5   // Base Relocation Table 重定位表
#define IMAGE_DIRECTORY_ENTRY_DEBUG           6   // Debug Directory 调试信息
//      IMAGE_DIRECTORY_ENTRY_COPYRIGHT       7   // (X86 usage)
#define IMAGE_DIRECTORY_ENTRY_ARCHITECTURE    7   // Architecture Specific Data
#define IMAGE_DIRECTORY_ENTRY_GLOBALPTR       8   // RVA of GP
#define IMAGE_DIRECTORY_ENTRY_TLS             9   // TLS Directory
#define IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG    10   // Load Configuration Directory
#define IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT   11   // Bound Import Directory in headers
#define IMAGE_DIRECTORY_ENTRY_IAT            12   // Import Address Table
#define IMAGE_DIRECTORY_ENTRY_DELAY_IMPORT   13   // Delay Load Import Descriptors
#define IMAGE_DIRECTORY_ENTRY_COM_DESCRIPTOR 14   // COM Runtime descriptor
#+END_SRC

** 区块表
区块表紧挨着Optional Header, 故相对于PE文件开头的偏移地址为:
PE头地址 + 18h(Optional Header相对PE头偏移) + Optional Header大小
区块表的定义: (此结构大小为40), 区块表的个数由IMAGE_FILE_HEADER中NumberOfSections决定
#+BEGIN_SRC C++
#define IMAGE_SIZEOF_SHORT_NAME              8

typedef struct _IMAGE_SECTION_HEADER {
    BYTE    Name[IMAGE_SIZEOF_SHORT_NAME];
    union {
            DWORD   PhysicalAddress;
            DWORD   VirtualSize;
    } Misc;
    DWORD   VirtualAddress;
    DWORD   SizeOfRawData;
    DWORD   PointerToRawData;
    DWORD   PointerToRelocations;
    DWORD   PointerToLinenumbers;
    WORD    NumberOfRelocations;
    WORD    NumberOfLinenumbers;
    DWORD   Characteristics;
} IMAGE_SECTION_HEADER, *PIMAGE_SECTION_HEADER;
#+END_SRC

*** Name字段
区块名, 通常以.开头, 如".text"
如果第一个字符是$, 则所有此种区块会在载入时, 按照$后的字母顺序合并

*** VitrualSize
区块大小, 这是在区块没有进行对齐前的大小

*** VirtualAddress
该区块装载到内存中的虚拟地址
这个地址总是按照内存页进行对其的, 即总是SectionAlignment的整数倍

*** SizeOfRawData
该区块在磁盘中所占的大小, 在可执行文件中, 此字段已经被FileAlignment潜规则处理过

*** PointerToRawData
该区块在磁盘中的偏移(是从文件开头开始计算的)

*** PointerToRelocations
在exe中无意义, 在obj中表示本区块的重定位信息的偏移值

*** PointerToLinenumbers
调试信息, 行号表相关信息

*** NumberOfRelocations
在exe中无意义, 在obj中是本区块在重定位表中的重定位数目

*** NumberOfLinenumbers
调试信息, 该区块在行号表中的行号数目

*** Characteristics
该区块的属性, 为以下值的或(下面的列举为节选内容)
#+BEGIN_SRC C++
#define IMAGE_SCN_CNT_CODE                   0x00000020  // Section contains code.
#define IMAGE_SCN_CNT_INITIALIZED_DATA       0x00000040  // Section contains initialized data.
#define IMAGE_SCN_CNT_UNINITIALIZED_DATA     0x00000080  // Section contains uninitialized data.

#define IMAGE_SCN_LNK_OTHER                  0x00000100  // Reserved.
#define IMAGE_SCN_LNK_INFO                   0x00000200  // Section contains comments or some other type of information.
//      IMAGE_SCN_TYPE_OVER                  0x00000400  // Reserved.
#define IMAGE_SCN_LNK_REMOVE                 0x00000800  // Section contents will not become part of image.
#define IMAGE_SCN_LNK_COMDAT                 0x00001000  // Section contents comdat.
//                                           0x00002000  // Reserved.
//      IMAGE_SCN_MEM_PROTECTED - Obsolete   0x00004000
#define IMAGE_SCN_NO_DEFER_SPEC_EXC          0x00004000  // Reset speculative exceptions handling bits in the TLB entries for this section.
#define IMAGE_SCN_GPREL                      0x00008000  // Section content can be accessed relative to GP
#define IMAGE_SCN_MEM_FARDATA                0x00008000
//      IMAGE_SCN_MEM_SYSHEAP  - Obsolete    0x00010000
#define IMAGE_SCN_MEM_PURGEABLE              0x00020000
#define IMAGE_SCN_MEM_16BIT                  0x00020000
#define IMAGE_SCN_MEM_LOCKED                 0x00040000
#define IMAGE_SCN_MEM_PRELOAD                0x00080000

#define IMAGE_SCN_LNK_NRELOC_OVFL            0x01000000  // Section contains extended relocations.
#define IMAGE_SCN_MEM_DISCARDABLE            0x02000000  // Section can be discarded.
#define IMAGE_SCN_MEM_NOT_CACHED             0x04000000  // Section is not cachable.
#define IMAGE_SCN_MEM_NOT_PAGED              0x08000000  // Section is not pageable.
#define IMAGE_SCN_MEM_SHARED                 0x10000000  // Section is shareable.
#define IMAGE_SCN_MEM_EXECUTE                0x20000000  // Section is executable.
#define IMAGE_SCN_MEM_READ                   0x40000000  // Section is readable.
#define IMAGE_SCN_MEM_WRITE                  0x80000000  // Section is writeable.

#+END_SRC


** 区块
*** 区块名称的通常意义
.text 默认的代码区块, 如果使用的是Borland C++, 代码区块的名称为.code
.data 默认的读/写数据区块. 放置全局变量, 静态变量
.rdata 默认的只读数据区块, 存放说明字符串, 调试目录等
.idata 包含其他外来dll的函数和数据信息, 即输入表. 目前通常会将.idata合并到另一个区块, 通常合并到.rdata
.edata 输出表, 如果创建一个输出API或数据的可执行文件时, 链接器会创建一个.exp文件, 这个.exp文件就包含了一个.edata区块. 此区块也通常会被合并到.text或.tdata中
.rsrc 资源, 如图表, 位图等, 这个区块是只读的
.bss 未初始化数据, 很少使用, 通常采取将.data区块拓展到足够大以存放未初始化数据
.tls TLS为线程局部存储器, 用于支持通过___declspec(thread)声明的线程局部存储变量的数据
.reloc 可执行文件的基址重定位, 一般是dll文件才需要的
.sdata 可通过全局指针相对寻址的"短"可读/写数据.

*** 换算虚拟偏移地址(RVA)和文件偏移
当处理PE文件的时候, 任何RVA必须经过到文件偏移的换算, 才能用来定位并访问文件中的数据, 
但没有一个通用的公式来完成, 下面使用穷举法

1, 循环扫描区块表得出每个区块在内存中的起始RVA(根据IMAGE_SECTION_HEADER中的VirtualAddress字段)
并根据区块大小(SizeOfRawData字段)算出区块结束的RVA(VirtualAddress + SizeOfRawData), 判断目标RVA是否落在该区块内

2, 通过步骤1定位了目标RVA处于具体的某个区块后, 
用目标RVA减去该区块的起始RVA, 得到目标RVA相对于起始地址的偏移量RVA2

3, 在区块表中取得该区块在文件中的偏移地址(PointerToRawData字段), 将这个偏移值加上RVA2, 得到真正的文件偏移地址

** 输入表
*** 输入函数
输入函数就是被程序调用, 但是其代码不在程序中的函数
这些函数的代码在dll中

*** 输入表结构
**** 简介
PE文件头中的IMAGE_OPTIONAL_HEADER中的DataDirectory的第二个成员就是指向输入表的
而输入表是以一个IMAGE_IMPORT_DESCRIPTOR(简称IID)数组开始的
每个被PE文件链接进来的DLL文件都对应一个IID数组结构
这个IID数组并没有指明长度, 而是以一个全为0的IID结构作为结束标记

**** 具体结构
#+BEGIN_SRC C++
typedef struct _IMAGE_IMPORT_DESCRIPTOR {
    union {
        DWORD   Characteristics;            // 0 for terminating null import descriptor
        DWORD   OriginalFirstThunk;         // RVA to original unbound IAT (PIMAGE_THUNK_DATA)
    } DUMMYUNIONNAME;
    DWORD   TimeDateStamp;                  // 0 if not bound,
                                            // -1 if bound, and real date\time stamp
                                            //     in IMAGE_DIRECTORY_ENTRY_BOUND_IMPORT (new BIND)
                                            // O.W. date/time stamp of DLL bound to (Old BIND)

    DWORD   ForwarderChain;                 // -1 if no forwarders
    DWORD   Name;
    DWORD   FirstThunk;                     // RVA to IAT (if bound this IAT has actual addresses)
} IMAGE_IMPORT_DESCRIPTOR;
typedef IMAGE_IMPORT_DESCRIPTOR UNALIGNED *PIMAGE_IMPORT_DESCRIPTOR;
#+END_SRC

**** 结构成员解释
***** OriginalFirstThunk
指向first thunk，IMAGE_THUNK_DATA，该 thunk 拥有 Hint 和 Function name 的地址。

***** TimeDateStamp
该字段可以忽略。如果那里有绑定的话它包含时间/数据戳（time/data stamp）。如果它是0，就没有绑定在被导入的DLL中发生。
在最近，它被设置为0xFFFFFFFF以表示绑定发生。

***** ForwarderChain
一般情况下我们也可以忽略该字段。在老版的绑定中，它引用API的第一个forwarder chain（传递器链表）。
它可被设置为0xFFFFFFFF以代表没有forwarder。

***** Name
它表示DLL 名称的相对虚地址（译注：相对一个用null作为结束符的ASCII字符串的一个RVA，该字符串是该导入DLL文件的名称。
如：KERNEL32.DLL）。

***** FirstThunk
它包含由IMAGE_THUNK_DATA定义的 first thunk数组的虚地址，通过loader用函数虚地址初始化thunk。
在Orignal First Thunk缺席下，它指向first thunk：Hints和The Function names的thunks。

**** OriginalFirstThunk 和 FirstThunk的关系
#+CAPTION: title
#+LABEL: first thunk
[[file:./FirstThunk_OriginalFirstThunk.PNG]]


```