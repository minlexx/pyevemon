#define _CRT_SECURE_NO_WARNINGS
#include <Windows.h>
#include <Python.h>


/*int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPWSTR lpszCmdLine, int nShowCmd) {

	UNREFERENCED_PARAMETER(hInstance);
	UNREFERENCED_PARAMETER(hPrevInstance);
	UNREFERENCED_PARAMETER(lpszCmdLine);
	UNREFERENCED_PARAMETER(nShowCmd);

	int argc = 0;
	wchar_t **argv = CommandLineToArgvW(lpszCmdLine, &argc); */

int wmain(int argc, wchar_t **argv) {

	bool is_debug = false;
	bool is_console = false;

	if (argc > 0) {
		int i;
		for (i = 1; i < argc; i++) {
			const wchar_t *arg = argv[i];
			if (arg) {
				if (_wcsicmp(arg, L"--debug") == 0) is_debug = true;
				if (_wcsicmp(arg, L"--console") == 0) is_console = true;
			}
		}
	}

	wchar_t *progname = _wcsdup(argv[0]);
	Py_SetProgramName(progname);

	if (is_debug) {
		MessageBoxW(GetDesktopWindow(), Py_GetProgramName(), L"pyevemon: program name",
			MB_OK | MB_ICONINFORMATION);
		MessageBoxW(GetDesktopWindow(), Py_GetProgramFullPath(), L"pyevemon: full path",
			MB_OK | MB_ICONINFORMATION);
	}


	if (is_console) {
		// run interactive python interpreter
		// TODO: construct proper argc/argv, dropping out our own options
		//       (--debug, --console), instead of dropping all options
		wchar_t *fake_argv[1] = { L"" };
		Py_Main(0, fake_argv);
	} else {
		FILE *fp = fopen("main.py", "rt");
		if (fp) {
			Py_Initialize();

			// emulate cx_Freeze behaviour - set sys.frozen = True
			PyObject *bFrozen = PyBool_FromLong(TRUE);
			PySys_SetObject("frozen", bFrozen);

			PyThreadState

			// set sys.argv
			// PyObject *list = PyList_New(1);
			// PyList_SetItem(list, 0, PyUnicode_FromString(""));
			// PySys_SetObject("argv", list);
			// ^^ no need to do that
			PySys_SetArgvEx(argc, argv, FALSE);

			//PyRun_SimpleStringFlags("import sys\nprint(sys.argv)", NULL);
			PyRun_SimpleFileExFlags(fp, "main.py", 0, NULL);

			Py_Finalize();
			fclose(fp);
		}
		else {
			MessageBoxW(GetDesktopWindow(), L"Could not open main.py!", L"pyevemon",
				MB_OK | MB_ICONSTOP);
		}
	}

	free(progname);
	return 0;
}
