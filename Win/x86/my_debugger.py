# -*- coding: utf-8 -*-  
from ctypes import *  
from my_debugger_defines import *  
#from pydbg import *
kernel32 = windll.kernel32  

class debugger():  
      
    def __init__(self):  
        pass  
    def load(self, path_to_exe):  
        creation_flags = DEBUG_PROCESS  
        startupinfo = STARTUPINFO()  
        process_information = PROCESS_INFORMATION()  
        startupinfo.dwFlags = 0x1  
        startupinfo.wShowWindow = 0x0  
        startupinfo.cb = sizeof(startupinfo)  
        if kernel32.CreateProcessA(path_to_exe,  
                                    None,  
                                    None,  
                                    None,  
                                    None,  
                                    creation_flags,  
                                    None,  
                                    None,  
                                    byref(startupinfo),  
                                    byref(process_information)):  
            print "[*] we have successfully launched the process!"  
            print "[*] PID:%d" % process_information.dwProcessId  
        else:  
            print "[*] Error:0x%08x." % kernel32.GetLastError()
    # 获取进程的句柄，要调试当然要全部权限了         
    def open_process(self, pid):  
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, pid, False)  
        return h_process  
              
    def attach(self, pid):  
        self.h_process = self.open_process(pid)  
        #尝试附加到某个pid的程序上  
        if kernel32.DebugActiveProcess(pid):  
            self.debugger_active = True  
            self.pid = pid  
            self.run()  
        else:  
            print "[*] Unable to attach to the process."  
      
    #既然都附加上去了，等待调试事件咯  
    def run(self):  
        while self.debugger_active == True:  
            self.get_debug_event()  
  
    # 等待调试事件，获取调试事件  
    def get_debug_event(self):  
        debug_event = DEBUG_EVENT()  
        continue_status = DBG_CONTINUE  
        #INFINITE表示无限等待  
        if kernel32.WaitForDebugEvent(byref(debug_event), INFINITE):  
            #现在我们暂时不对事件进行处理  
            #现在只是简单地恢复进程的运行吧  
            raw_input("Press a key to continue...")  
            self.debugger_active = False  
            kernel32.ContinueDebugEvent(debug_event.dwProcessId,debug_event.dwThreadId, continue_status)  
  
    def detach(self):  
        if kernel32.DebugActiveProcessStop(self.pid):  
            print "[*] Finished debugging. Exiting..."  
        else:  
            print "There was an error"  
            return False    