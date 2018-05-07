# 法1：创建一个全新的进程进行调试

CreateProcessA函数创建一个新的进程

	函数原型
	BOOL CreateProcess
	(
	LPCTSTR lpApplicationName, //可执行文件路径
	LPTSTR lpCommandLine,  //程序接受的命令行参数
	LPSECURITY_ATTRIBUTES lpProcessAttributes,
	LPSECURITY_ATTRIBUTES lpThreadAttributes,
	BOOL bInheritHandles,
	DWORD dwCreationFlags, //指定附加的、用来控制优先类和进程的创建的标志
	LPVOID lpEnvironment,
	LPCTSTR lpCurrentDirectory,
	LPSTARTUPINFO lpStartupInfo, //结构体STARINFO 进程的启动方式
	LPPROCESS_INFORMATIONlpProcessInformation //结构体PROCESS_INFORMATION 进程启动后相关状态信息
	);

# 法2：附加调试器至现有进程

OpenProcess函数根据进程PID获取进程句柄

	函数原型
	HANDLE OpenProcess(
	DWORD dwDesiredAccess, //渴望得到的访问权限（标志） PROCESS_ALL_ACCESS
	BOOL bInheritHandle, // 是否继承句柄
	DWORD dwProcessId// 进程标示符
	);

DebugActiveProcess函数使调试器附加到一个活动进程并且调试它

	BOOL WINAPI DebugActiveProcess(
	　　__in DWORD dwProcessId
	　　);
	参数dwProcessId：要被调试的进程标识。

WaitForDebugEvent获取调试事件

	WaiteForDebugEvent(
	LPDEBUG_EVENT _DEBUG_EVENT,
	DWORD dwMilliseconds)

	第一个参数指向event结构，这个结构描述了一个调试事件，第二个参数为等待事件的毫秒数。
	返回一个BOOL值

ContinueDebugEvent使调试器能够继续之前报告调试事件的线程。

	BOOL WINAPI ContinueDebugEvent（
	  _In_ DWORD dwProcessId，
	  _In_ DWORD dwThreadId，
	  _In_ DWORD dwContinueStatus
	）;

	dwProcessId,dwThreadId的取值可以来源于结构体DEBUG_EVENT中同名成员
	dwContinueStatus决定目标进程的下一步动作，继续执行(DBG_CONTINUE)还是处理捕获的异常事件(DBG_EXCEPTION_NOT_HANDLED)

DebugActiveProcessStop停止调试器调试指定的进程。

	BOOL WINAPI DebugActiveProcessStop（
	  _In_ DWORD dwProcessId
	）;




